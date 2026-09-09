.PHONY: all build rust run test lint clean

all: build

rust:
	cargo build --manifest-path Cargo.toml

build: rust
	cp target/debug/lib_core.dylib src/matrix/_core.cpython-312-darwin.so
	uv sync --reinstall-package matrix

run:
	uv run matrix $(ARGS)

test:
	uv run pytest

lint:
	uv run mypy src/matrix
	uv run flake8 src/matrix

clean:
	rm -rf target .mypy_cache
