# Project Data Engineering

This repository contains code for a data engineering project that involves processing telemetry data from IoT devices and storing it in a MongoDB database.

## Installation

Before running the project, ensure you have Docker installed on your system.

Install Python (version 3.9 or higher) and pip.

Install the required Python packages:
pip install pandas pymongo


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

4. Once the containers are built, the setup_database.py script will automatically run to initialize the MongoDB database and load the data from the iot_telemetry_data.csv file.

## Usage

To start the project, run the following command:

```bash
docker-compose up

