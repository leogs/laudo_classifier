FROM python:3.7-slim

RUN apt-get update

# Copy local code to the container image.
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

COPY ./src /app/src
COPY ./models /app/models

#Runs a single unvicorn process so we can handle replication at the cluster level
#Otherwise we can use gunicorn as a process manager
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]