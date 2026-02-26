# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements first (better caching for CI/CD)
COPY requirements.txt .

# Install dependencies and clean up cache in one layer
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Documentation for the port
EXPOSE 5000

# Run using Gunicorn
# --timeout 120 helps if your EC2 is a smaller instance (t2.micro)
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]