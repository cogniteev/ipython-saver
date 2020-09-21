#!/usr/bin/env bash

./fetch.sh

python main.py $@
gsutil -m cp -r ipython gs://$GCP_PROJECT_IPYTHON

