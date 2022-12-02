FROM python:3.8

EXPOSE 8080

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*


COPY . .

# Python requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8080"]

# start the scraper
#CMD ["bash", "run_docker.sh"]
