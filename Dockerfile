# Use the official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files
COPY . .

# Expose port 8501 (default for Streamlit)
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "app.py"]
