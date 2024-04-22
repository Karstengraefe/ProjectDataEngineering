FROM python:3.9

# Set the working directory in the container
WORKDIR /app


# Copy the Python scripts into the container at /app
COPY setup_database.py /app
COPY load_data.py /app
COPY iot_telemetry_data.csv /app

# Set environment variables
ENV MONGO_HOST=mongo
ENV MONGO_PORT=27017

# Command to run the Python scripts
CMD ["python", "setup_database.py"]













