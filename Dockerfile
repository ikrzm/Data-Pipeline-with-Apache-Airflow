# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /project-root
WORKDIR /project-root

# Copy the current directory contents into the container at /project-root
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add the src directory to PYTHONPATH to ensure modules are found
ENV PYTHONPATH "${PYTHONPATH}:/project-root/src/db"

# Any other setup, like environment variables

# The command to run when the container starts
CMD ["python", "src/db/topostgres.py"]
