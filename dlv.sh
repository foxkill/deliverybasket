#!/usr/bin/env bash

set -e
source ~/code/deliverybasket/.venv/bin/activate
python3.9 ./main.py $@
deactivate
