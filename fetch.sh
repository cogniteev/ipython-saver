#!/usr/bin/env bash

gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
gsutil -m cp -r gs://$GCP_PROJECT_IPYTHON/ipython/ .