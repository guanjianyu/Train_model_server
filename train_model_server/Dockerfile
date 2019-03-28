FROM tensorflow/tensorflow:nightly-py3 

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","model_server.py"]