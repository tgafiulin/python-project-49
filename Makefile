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

brain-even:
	poetry run brain-even

all:
	poetry install
	poetry build
	poetry publish --dry-run
	python -m pip install dist/*.whl

lint:
	poetry run flake8 brain_games