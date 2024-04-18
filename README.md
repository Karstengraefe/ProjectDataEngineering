# ProjectDataEngineering
# Sensor Data Importer

This project automates the process of importing sensor data into a MongoDB database using Docker and Python scripts.

## Setup Instructions

1. Clone the repository:
git clone <repository_url>

2. Navigate to the project directory:
cd ProjectDataEngineering

3. Build the Docker image:
docker build -t sensor-data-importer .

4. Run the Docker container:
docker run --name sensor-importer sensor-data-importer

## Usage

### setup_database.py

This script sets up the MongoDB database by creating a collection with a predefined schema.

1. To run the script, use the following command:
python setup_database.py

### load_data.py

This script loads sample sensor data into the MongoDB collection.

1. To run the script, use the following command:
python load_data.py

## Testing

Before running the scripts, ensure that MongoDB is running.

1. Test setup_database.py:
- Run the script to create the database collection.
- Verify in the MongoDB database that the collection `sensor_data` has been created with the correct schema.

2. Test load_data.py:
- Run the script to load sample data into the MongoDB collection.
- Verify in the MongoDB database that the `sensor_data` collection now contains the expected data.

## Notes

- Ensure that MongoDB is installed and running before executing the scripts.
- Modify the scripts or Dockerfile as needed to customize the setup for your environment.

For detailed instructions, please refer to the project documentation.

