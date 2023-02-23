.PHONY: install shell ipython test black lint count docker-build docker-push help
CODE=src/
ENTRYPOINTS=bin/
TESTS=tests/
DOCKER_IMG=docker_image_name
ENVIRONMENT?=dev
VERSION=$(shell poetry version --short)

ARTIFACT_REGISTRY=us-central1-docker.pkg.dev # Change this to your Artifact Registry
DOCKER_PROJECT=${{ENVIRONMENT}}-fixme # Change this to your gcloud project
DOCKER_TAG=${{ARTIFACT_REGISTRY}}/${{DOCKER_PROJECT}}/fixme/${{DOCKER_IMG}}


install: ## Install dependencies within a local virtual env
	poetry install
	test -f .env/env || /bin/cp .env/example .env/env
	@echo "\\n docker_image_name has been installed!\\nIn order to use all functionality, please populate the fixme's in .env/env"

shell: ## Spawn a shell that automatically sources the development venv
	poetry shell

ipython: ## Run ipython
	poetry run dotenv -f .env/env run ipython

test: ## Run all tests
	poetry run dotenv -f .env/test run pytest --cov-report term-missing --cov=src/ tests/

black: ## Auto-format all python code
	poetry run black $(CODE) $(ENTRYPOINTS) $(TESTS)

lint: ## Run pylint
	poetry run pylint src/

count: ## Count the lines of python, because y not
	find . -name "*.py" -type f | xargs wc -l

docker-build: ## Build the docker_image_name docker image
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker build . --tag=$(DOCKER_IMG)
	rm requirements.txt

docker-push: ## Push the docker_image_name image to GAR so Composer 2 can grab it
	gcloud auth configure-docker ${{ARTIFACT_REGISTRY}}
	docker tag $(DOCKER_IMG) $(DOCKER_TAG)
	docker tag $(DOCKER_IMG) $(DOCKER_TAG):$(VERSION)
	docker push $(DOCKER_TAG) --all-tags

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {{FS = ":.*?## "}}; {{printf "\\033[36m%-30s\\033[0m %s\\n", $$1, $$2}}'
