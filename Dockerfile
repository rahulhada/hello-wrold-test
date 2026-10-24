# Use a lightweight official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Define the command to run; ENTRYPOINT allows passing runtime arguments
ENTRYPOINT ["python", "app.py"]