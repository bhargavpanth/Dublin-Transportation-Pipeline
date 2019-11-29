FROM python:3.10.0a2-buster

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy source

# Run application
