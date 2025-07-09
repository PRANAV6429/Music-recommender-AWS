# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose port 5000 (Flask runs on this)
EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "application:app"]

