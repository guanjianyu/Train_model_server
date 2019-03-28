# Demo of how client training a model on server

## train_model_server
it contains files to build a demo server which can train the model when client upload
training data. And return trained model with url http://...../download where client can
download model.

there is also a [docker image](https://cloud.docker.com/u/guanjianyu/repository/docker/guanjianyu/train_model_server) for this server.

* you can run this server either locally or with docker:
  * locally:
    1. git clone this repository
    2. python model_server.py

  * docker:
    1. docker pull guanjianyu/train_model_server
    2. docker run -p 80:80 --name=train_server guanjianyu/train_model_server (first run)
    3. docker run -i train_server (rerun)

go to url http://127.0.0.1:80 to upload train file and train model


## test_client
* run jupyter notebook to download the trained model and test it.
