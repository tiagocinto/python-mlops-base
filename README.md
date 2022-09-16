# Python MLOps Base

### Setup and install env
Prior to testing the ml's pipeline:
1. clone or fork it
1. cd into it
1. run `make setup` to create a virtual env: default is `~/.ml-env` (update `Makefile` to change it)
1. activate the virtual env: `source ~/.ml-env/bin/activate`
1. run `make install` to install requirements

### CLI Tools

There are two cli tools:
* `cli.py` is the endpoint that serves out predictions. To predict whether a patient has diabetes use the following: `python cli.py --preg 1 --plas 93 --pres 70 --skin 31 --test 0 --mass 30.4 --pedi 0.315 --age 23` (for further details on parameters, refer to `pima.names` in data dir).

![image](https://user-images.githubusercontent.com/1559328/190708598-8811110c-cefb-4088-a5b4-366ddf228ecb.png)

* `utilscli.py (retrain)` serves as the entry point to do more things on the model, e.g., retraining it: `python utilscli.py retrain --test_size 0.2 --criterion gini --max_depth 5 --min_samples_split 2 --min_samples_leaf 1 --max_features 4` (for further details on the parameters, refer to [sklearn's docs of the RandomForest classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)).

![image](https://user-images.githubusercontent.com/1559328/190710421-36dfa6fe-a3de-425d-b14a-e17f70e179d8.png)

* `utilscli.py (predict)` also serves to query the /predict route of the ml microservice: `python utilscli.py predict --host http://127.0.0.1:8080/predict --preg 1 --plas 93 --pres 70 --skin 31 --test 0 --mass 30.4 --pedi 0.315 --age 23` (after python `app.py`).

![image](https://user-images.githubusercontent.com/1559328/190712202-ace3bb5d-a838-4c11-94d0-376fa9fd199d.png)

### Microservice

The ml microservice can be run in many ways.

#### Locally
You can run the microservice locally as follows with the commmand: `python app.py`:

![image](https://user-images.githubusercontent.com/1559328/190715025-a6e3969f-18e4-434c-8379-2199a3ae9e90.png)

To serve a prediction against the application, run the `python utilscli.py predict`:

![image](https://user-images.githubusercontent.com/1559328/190717133-cf3c8d6e-2fee-4d2c-a2bf-caecaac3ff63.png)

#### Containerized Microservice
Prior to running this project a containerized microservice, create a `private container` on AWS ECR like this:

![image](https://user-images.githubusercontent.com/1559328/190718421-9d563d5c-262d-403a-925e-310ec54b2789.png)

This repo is configured for auto-deploy its container with GitHub Actions. Check `aws-ecr.yml`...
