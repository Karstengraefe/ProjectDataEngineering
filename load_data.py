import os
import pandas as pd
from pymongo import MongoClient

# MongoDB connection details
mongo_host = os.environ.get("MONGO_HOST", "localhost")
mongo_port = int(os.environ.get("MONGO_PORT", 27017))

client = MongoClient(f"mongodb://{mongo_host}:{mongo_port}/")
db = client["iot_data"]
collection = db["sensor_data"]

# file path to the csv location.
csv_file_path = "iot_telemetry_data.csv" 

# Read CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
data = df.to_dict(orient="records")

for document in data:
    collection.insert_one(document)
