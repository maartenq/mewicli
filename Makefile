# Makefile

.PHONY: poetry
poetry: ## Install the poetry environment and install the pre-commit hooks.
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry run pre-commit install
	@poetry shell

.PHONY: tag
tag: ## Set annotated tag from Poetry's version on this commit.
	@echo "🚀 Setting annotated tag from Poetry version on this commit."
	$(eval $@_VERSION := $(shell poetry version --short))
	@git tag --force --annotate "$($@_VERSION)" --message "$($@_VERSION)"

.PHONY: poetry-clean
poetry-clean: ## Remove the poetry environment.
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry env remove --all

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry lock --check
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy src/

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --verbose --cov --cov-config=pyproject.toml --cov-report=xml

.PHONY: htmlcov
htmlcov: ## Create HTML coverage report
	@echo "🚀 Create HTML coverage report"
	@poetry run coverage html

.PHONY: cov
cov: test htmlcov ## Test, make coverage html and open
	@echo "🚀 Openeing coverage report"
	open htmlcov/index.html

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: clean-git-ls
clean-git-ls: ## Dry run removing untracked files from the working tree (using `git clean`).
	@echo "🚀 Dry run removing untracked files from the working tree (using `git clean`)."
	git clean --dry-run -x -d

.PHONY: clean-git
clean-git: ## Remove untracked files from the working tree (using `git clean`).
	@echo "🚀 Removing untracked files from the working tree (using `git clean`)."
	git clean --force -x -d

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts.
	@echo "🚀 Removing Python file artifacts."
	find . -name '*.pyc' -exec rm -f {} + || true
	find . -name '*.pyo' -exec rm -f {} + || true
	find . -name '*~' -exec rm -f {} + || true
	find . -name '__pycache__' -exec rm -rf {} + || true

.PHONY: clean
clean: clean-build clean-pyc clean-git  ## Clean all

.PHONY: publish
publish: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "🔸 \033[36m%-20s\033[0m ▫️  %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
