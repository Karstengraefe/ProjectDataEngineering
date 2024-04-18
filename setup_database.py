import pymongo

# MongoDB connection details
mongo_host = "localhost"
mongo_port = 27017
mongo_db = "iot_data"
collection_name = "sensor_data"

# Define the schema
schema = {
    "ts": {"bsonType": "double"},
    "device": {"bsonType": "string"},
    "co": {"bsonType": "double"},
    "humidity": {"bsonType": "double"},
    "light": {"bsonType": "bool"},
    "lpg": {"bsonType": "double"},
    "motion": {"bsonType": "bool"},
    "smoke": {"bsonType": "double"},
    "temp": {"bsonType": "double"}
}

def drop_collection_if_exists(db, collection_name):
    if collection_name in db.list_collection_names():
        db.drop_collection(collection_name)
        print(f"Collection '{collection_name}' dropped.")

def create_collection():
    client = pymongo.MongoClient(mongo_host, mongo_port)
    db = client[mongo_db]

    # Drop the existing collection if it exists
    drop_collection_if_exists(db, collection_name)

    # Create the collection with the specified schema
    db.create_collection(collection_name, validator={"$jsonSchema": {"bsonType": "object", "properties": schema}})
    print("Collection created successfully.")

if __name__ == "__main__":
    create_collection()

