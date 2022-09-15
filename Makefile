setup:
	python3 -m venv ~/.ml-env

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=. tests/test_*.py

format:
	black *.py tests/*.py

lint:
	#hadolint Dockerfile 
	pylint --disable=R,C,W1203 *.py tests/*.py

all: format lint test