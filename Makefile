build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

install:
	poetry install

brain-games:
	poetry run brain-games

all:
	poetry build
	poetry publish --dry-run
	python -m pip install dist/*.whl

lint:
	poetry run flake8 brain_games