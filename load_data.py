from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["iot_data"]
collection = db["sensor_data"]
import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv("iot_telemetry_data.csv")
data = df.to_dict(orient="records")
for document in data:
    collection.insert_one(document)
