# Use the official Python image.
FROM python:3.8-slim

# Set the working directory.
WORKDIR /app

# Install dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files.
COPY . .

# Run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
