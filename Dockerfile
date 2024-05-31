FROM python:3.11-slim

# Install Poetry
RUN pip install poetry==1.6.1

# Configure Poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Set the working directory
WORKDIR /code

# Copy only the requirements to cache them in Docker layer
COPY pyproject.toml README.md poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Install Uvicorn
RUN pip install uvicorn

# Copy the application code
COPY my-app/app ./my-app/app
COPY my-app/packages ./my-app/packages

# Copy the .env file and ensure it has Unix line endings
COPY .env .env
RUN apt-get update && apt-get install -y bash dos2unix && dos2unix .env

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/code/my-app/packages:/code/my-app/packages/rag-conversation:/code/my-app/packages/extraction-openai-functions:${PYTHONPATH}"

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["bash", "-c", "source .env && uvicorn my-app.app.server:app --host 0.0.0.0 --port 8080"]
