# Base image: Python 3.12 slim
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]