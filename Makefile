setup-dev:
	gcloud config set project {#PROJECT_NAME}
	gcloud auth application-default login

run-install:
	pip install -r requirements.txt

run:
	python gemini_helpers.py