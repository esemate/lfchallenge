# Python Base image 
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy of the Python script into the container
COPY logfilter.py .

# Execution of the Python script
CMD ["python","-u","logfilter.py"]