FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

COPY . /code

# Copy only necessary files
# COPY / myapp/  # Adjust the path if your Django project is in a different directory
RUN apt-get update && apt-get install -y tini \
    libpq-dev gcc python3-dev zlib1g-dev libjpeg-dev && \
    python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip install --upgrade pip setuptools-scm && \
    pip install --no-cache-dir -r requirements.txt

# Create a non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN usermod -aG sudo appuser

# Change ownership of the app directory
RUN chown -R appuser:appuser /code

COPY entrypoint.sh /code
RUN chmod +x /code/entrypoint.sh

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# After setting up everything
# CMD ["/bin/bash"]

ENTRYPOINT ["/code/entrypoint.sh"]

