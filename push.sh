gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
gsutil -m cp -r ipython gs://$GCP_PROJECT_IPYTHON