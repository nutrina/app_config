FROM python:3.9

# Add user that will be used in the container.
# RUN useradd app_config

# Port used by this container to serve HTTP.
EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Install the project requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# RUN chown app_config:app_config /app

# Copy the source code of the project into the container.
# COPY --chown=app_config:app_config . .
COPY . .

# Use user "app_config" to run the build commands below and the server itself.
# USER app_config

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

CMD gunicorn mysite.wsgi:application
