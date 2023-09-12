# Using the official nicegui image
FROM zauberzeug/nicegui:latest

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container's /app directory
COPY . /app

# Install any Python dependencies specified in requirements.txt
# RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run your server.py script
CMD ["python", "main.py"]

