#!/usr/bin/env bash

gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
gsutil -m cp -r gs://$GCP_PROJECT/ipython/ sessions

python main.py $@
gsutil -m cp -r sessions gs://$GCP_PROJECT/ipython

