#FROM amopromo/python3.10
#ENV PYTHONUNBUFFERED=1
#RUN mkdir /code
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
#COPY . /code/
#RUN python manage.py migrate

# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations
RUN python manage.py migrate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=comment_app.settings

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]