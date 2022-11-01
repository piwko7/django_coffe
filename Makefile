.DEFAULT_GOAL := all

run:
	docker-compose up -d

stop:
	docker-compose down

build:
	docker-compose build

toml_sort:
	toml-sort pyproject.toml --all --in-place

isort:
	pipenv run isort .

black:
	pipenv run black .

flake8:
	pipenv run flake8 .

pylint:
	pipenv run pylint src

dockerfile_linter:
	docker run --rm -i hadolint/hadolint < Dockerfile

validate_openapi_schema:
	pipenv run openapi-spec-validator example-project/docs/api/openapi.yaml

mypy:
	pipenv run mypy --install-types --non-interactive .

audit_dependencies:
	pipenv export --without-hashes -f requirements.txt | poetry run safety check --full-report --stdin

bandit:
	pipenv run bandit -r . -x ./tests,./test

test:
	pipenv run pytest

lint: toml_sort isort black flake8 pylint mypy validate_openapi_schema

audit: audit_dependencies bandit

tests: test

all: lint audit tests
