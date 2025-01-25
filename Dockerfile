# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Cloud Run will use
ENV PORT=8080

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
