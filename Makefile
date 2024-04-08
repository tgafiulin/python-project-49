build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

install:
	poetry install

breain-games:
	poetry run brain-games