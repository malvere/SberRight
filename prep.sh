#!/bin/bash
poetry install
playwright install firefox
playwright install-deps firefox