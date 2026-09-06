.PHONY: all build run lint clean

all: build

build:
	uv sync

run: build
	uv run matrix

lint: build
	uv run mypy src/matrix
	uv run flake8 src/matrix

clean:
	rm -rf target .mypy_cache
