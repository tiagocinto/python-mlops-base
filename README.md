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

* `utilscli.py (predict)` also serves to query the /predict route of the ml microservice: `python utilscli.py predict --host http://127.0.0.1:8080/predict --preg 1 --plas 93 --pres 70 --skin 31 --test 0 --mass 30.4 --pedi 0.315 --age 23` (after `python app.py`).

![image](https://user-images.githubusercontent.com/1559328/190712202-ace3bb5d-a838-4c11-94d0-376fa9fd199d.png)

### Microservice

The ml microservice can be run in many ways.

#### Locally
You can run the microservice locally as follows: `python app.py`.

![image](https://user-images.githubusercontent.com/1559328/190715025-a6e3969f-18e4-434c-8379-2199a3ae9e90.png)

To serve a prediction against the application, run: `python utilscli.py predict`.

![image](https://user-images.githubusercontent.com/1559328/190717133-cf3c8d6e-2fee-4d2c-a2bf-caecaac3ff63.png)

#### Containerized Microservice
Prior to running this project as a containerized microservice, create a `private container` on AWS ECR like this:

<img src="https://user-images.githubusercontent.com/1559328/190718421-9d563d5c-262d-403a-925e-310ec54b2789.png" width="650" height="450">

This repo is configured for auto-deploy its container with GitHub Actions. As such, the workflow `aws-ecr.yml` uses the following parameters: `secrets.AWS_ACCESS_KEY_ID`, `secrets.AWS_SECRET_ACCESS_KEY`, and `secrets.REPO_NAME`. Configure them in the settings of this repo (`Secrets > Actions > New repo secret`). Those data must rely on an IAM user with appropriate permissions set. Create an IAM user on AWS like images below:

<img src="https://user-images.githubusercontent.com/1559328/190834440-98e95dd7-d56f-44fb-9ef6-ed6fe38a25b4.png" width="650" height="300">

<img src="https://user-images.githubusercontent.com/1559328/190834490-a1adf841-54fc-4ce4-b0c3-1234c0251157.png" width="650" height="300">

At the end, download the credentials as a `.csv` file. Input data from this file in the previous `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` parameters. The remaining `REPO_NAME` parameter is the repo's name defined during container creation.

At this point, you can pull the container wherever you want and run it.  For logging in AWS with docker use: `aws ecr get-login-password --region [account_region] | docker login --username AWS --password-stdin [aws_account_alias].dkr.ecr.[account_region].amazonaws.com` (prior to logging in, use `aws configure` and input the credentials of the IAM user previously created). To use the `aws` command outside the cloud, install it by clicking [here](https://awscli.amazonaws.com/AWSCLIV2.msi). Finally, pull the container and run it with:

`docker pull [aws_account_alias].dkr.ecr.[account_region].amazonaws.com/[ecr_container_name]:1`

`docker run [aws_account_alias].dkr.ecr.[account_region].amazonaws.com/[ecr_container_name]:1`
