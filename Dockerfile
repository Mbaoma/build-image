FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /action

# Copy the Python action code to the container
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Set the entry point for the action
ENTRYPOINT ["python", "/action/main.py"]
