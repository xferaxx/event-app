# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install system dependencies, including Tkinter and mysqlclient dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /desktop-app

# Copy the current directory contents into the container
COPY . /desktop-app

# Install any needed Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the display environment variable for GUI applications
# Adjust this for Windows and VcXsrv
ENV DISPLAY=host.docker.internal:0

# Run your Tkinter application
CMD ["python", "Tkinter.py"]
