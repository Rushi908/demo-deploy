# Use an official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir streamlit

# Expose Streamlit's default port
EXPOSE 8501

# Set environment variables for Streamlit
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_RUN_ON_SAVE=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
