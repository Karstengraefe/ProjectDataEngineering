# Project Data Engineering

This repository contains code for a data engineering project that involves processing telemetry data from IoT devices and storing it in a MongoDB database.

## Installation

Before running the project, ensure you have Docker installed on your system.

Install Python (version 3.9 or higher) and pip.


1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Karstengraefe/ProjectDataEngineering.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ProjectDataEngineering
    ```

3. Build the Docker containers:

    ```bash
    docker-compose up --build
    ```

4. Once the containers are built, the setup_database.py script will automatically run to initialize the MongoDB database.

## Usage

To start the project (when the containers are down), run the following command:

```bash
docker-compose up
```

Load the data from the iot_telemetry_data.csv file into the Database.

```bash
python load_data.py
```

## Checking Database Files with MongoDB Compass


    Launch MongoDB Compass.
    In the connection dialog, enter localhost as the host and 27017 as the port.
    Click "Connect" to establish a connection.
    Once connected, you'll see your databases listed on the left.
    Click on your database to expand it.
    Navigate through the collections and documents to view your data.

