# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the ports FastAPI and Streamlit will run on
EXPOSE 8000
EXPOSE 8501

# Run both FastAPI and Streamlit together
CMD uvicorn FASTAPI:app --host 0.0.0.0 --port 8000 & streamlit run streamlit_app.py --server.port 8501 --server.enableCORS false
