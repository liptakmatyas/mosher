.PHONY: clean

clean:
	find . -type d -name '__pycache__' -print0 | xargs -0 rm -rf
	find . -type d -name '*.egg-info' -print0 | xargs -0 rm -rf
	rm -rf .pytest_cache

test:
	pip install -e .
	pytest

