# wdi-cloudevents-demo
Demo from CloudEvents presentation on Warszawskie Dni Informatyki 2021.

## GCP Cloud Run
Build the Docker image:

```commandline
cd gcp-cloudevents-run
docker build -t YOUR_REGISTRY/wdi-gcp-cloudevents-run .
docker push YOUR_REGISTRY/wdi-gcp-cloudevents-run
```