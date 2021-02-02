FROM python:3.8
WORKDIR /Python-exercise
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir twython 
CMD ["pip", "install", "requirements.txt"]
CMD ["python", "main.py"]

