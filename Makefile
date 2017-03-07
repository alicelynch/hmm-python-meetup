#!/usr/bin/env bash
THIS_MAKEFILE := $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
PROJECT_ROOT := $(realpath $(dir $(THIS_MAKEFILE)))

print-%: ; @echo $* = $($*)

.PHONY: all
all: install test

.PHONY: clean
clean:
	rm -rf ./dist
	rm -rf ./build
	python3 setup.py clean --all

.PHONY: install
install :
	make clean
	pip3 install --no-cache-dir -r requirements.txt
	python3 setup.py install --force

.PHONY: test
test :
	python3 setup.py test
