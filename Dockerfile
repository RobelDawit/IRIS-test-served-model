FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libcairo2-dev \
    libgirepository1.0-dev \
    build-essential \
    gcc \
    default-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Cython before running requirements.txt
RUN pip install --no-cache-dir Cython

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install specific scikit-learn version and other dependencies
RUN pip install scikit-learn==1.4.2 fastapi uvicorn

# Expose the necessary port
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["uvicorn", "FASTAPI:app", "--host", "0.0.0.0", "--port", "8000"]