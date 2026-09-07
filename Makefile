.PHONY: all build rust run lint clean

all: build

rust:
	cargo build --manifest-path Cargo.toml

build: rust
	uv sync --reinstall-package matrix

run:
	uv run matrix

lint: build
	uv run mypy src/matrix
	uv run flake8 src/matrix

clean:
	rm -rf target .mypy_cache
