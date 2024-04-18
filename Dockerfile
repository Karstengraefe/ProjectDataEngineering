FROM mongo

# Create a directory to store CSV file
WORKDIR /data
COPY iot_telemetry_data.csv /data

# Import CSV file into MongoDB on container startup
CMD mongoimport --host 172.17.0.2 --db iot_db --collection telemetry_data --type csv --headerline --file iot_telemetry_data.csv








