.PHONY: all build rust run test lint clean

UNAME := $(shell uname)
ifeq ($(UNAME), Darwin)
	LIB_EXT := dylib
else
	LIB_EXT := so
endif
PY_EXT_SUFFIX := $(shell uv run python -c "import sysconfig; print(sysconfig.get_config_var('EXT_SUFFIX'))")

all: build

rust:
	cargo build --manifest-path Cargo.toml

build: rust
	cp target/debug/lib_core.$(LIB_EXT) src/matrix/_core$(PY_EXT_SUFFIX)
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
