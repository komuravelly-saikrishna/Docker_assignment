# # Use an official lightweight version of Python
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR .

# Copy the current directory contents into the container at /app
copy . .

# Command to run when starting the container
CMD ["python3", "app.py"]
RUN ["python3", "app.py"]
