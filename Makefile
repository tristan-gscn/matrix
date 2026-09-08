.PHONY: all build rust run test lint clean

all: build

rust:
	cargo build --manifest-path Cargo.toml

build: rust
	uv sync --reinstall-package matrix

run:
	uv run matrix $(ARGS)

test:
	uv run pytest

lint: build
	uv run mypy src/matrix
	uv run flake8 src/matrix

clean:
	rm -rf target .mypy_cache
