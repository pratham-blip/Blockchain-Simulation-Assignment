# Use an official lightweight Python image
FROM python:3.12-slim  

# Set the working directory inside the container
WORKDIR /app  

# Copy project files into the container
COPY . /app  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Define environment variable
ENV NAME BlockchainSimulation  

# Run main.py when the container starts
CMD ["python", "main.py"]
