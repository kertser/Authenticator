# Using the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container's /app directory
COPY . /app

# Install any Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for your server (not necessary for Compose, but for reference)
EXPOSE 5000

# No need to set environment variables here; they will be set in the Compose file

# Run your server.py script
CMD ["python3", "server.py"]

