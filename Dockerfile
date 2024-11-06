#Specifies the starting environment
FROM python:3.10-slim  

#Sets a folder for the project inside the container
WORKDIR /app

# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean

#Moves files (e.g., requirements.txt, project code) into the container
COPY requirements.txt .

# Installs necessary libraries, like using pip install.
RUN pip install -r requirements.txt

COPY . .

#Opens a port (like 8000 for Django) for access
EXPOSE 8000

#Starts the app, for Django, typically python manage.py runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]