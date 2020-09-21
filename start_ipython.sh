#!/usr/bin/env bash

./fetch.sh

python main.py $@

./push.sh

