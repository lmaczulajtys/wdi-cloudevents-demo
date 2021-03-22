# WDI CloudEvents demo
Demo from [CloudEvents](https://cloudevents.io/) presentation on [Warszawskie Dni Informatyki 2021](https://warszawskiedniinformatyki.pl/) about sending events from cloud starages across multiple cloud providers.
1. GCP Cloud Storage -> GCP EventArc -> GCP Cloud Run
2. Azure Blob Storage -> Azure Event Grid -> GCP Cloud Run
3. AWS S3 -> AWS Lambda -> Azure Event Grid -> GCP Cloud Run
## 1. GCP Cloud Run
1. [Create storage bucket](https://cloud.google.com/storage/docs/quickstart-console)
1. [Prepare Container Registry](https://cloud.google.com/container-registry/docs/quickstart)
1. `export GCP_REGISTRY = YOUR_REGISTRY_PREFIX`
1. Build the Docker image:
```commandline
cd gcp-cloudevents-run
docker build -t $GCP_REGISTRY/wdi-gcp-cloudevents-run .
docker push $GCP_REGISTRY/wdi-gcp-cloudevents-run
```
5. [Deploy Cloud Run function](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#deploying_to)
1. [Create Eventarc trigger](https://cloud.google.com/eventarc/docs/run/quickstart#trigger-setup)
1. Authentication options:
> 1. [JWT](https://cloud.google.com/run/docs/authenticating/service-to-service#calling-from-outside-gcp)
> 1. [Cloud Endpoints](https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run)
8. Use Cloud Logging to see results
1. Want to see how you can build solution with reporting dashboard presented on conferrence? [Check my blog.](https://maczulajtys.com/posts/dealing-with-pandemic-google-cloud/)

## 2. Azure EventGrid
1. [Create Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal) 
1. [Create system topic for BLob Storage events](https://docs.microsoft.com/en-us/azure/event-grid/blob-event-quickstart-portal#enable-event-grid-resource-provider)
1. Create webhook subscription with Cloud Run url
1. [Create Event Grid Topic from events from AWS](https://docs.microsoft.com/en-us/azure/event-grid/custom-event-quickstart-portal#create-a-custom-topic)
1. Save access key for topic
1. Create webhook subscription with Cloud Run url
## 3. AWS Lambda
1. [Create S3 bucket](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html)
1. [Create ECR repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)
1. `export AWS_REPOSITORY = YOUR_ECR_REPOSITORY_PATH`
1. Build the Docker image:
```commandline
cd aws-cloudevents-fn
docker build -t $AWS_REPOSITORY .
docker push $AWS_REPOSITORY
```
5. Create Lambda from docker image
> 1. Set `EVENT_URL` variable giving Event Grid Topic URL
> 1. Set `EVENTGRID_KEY` variable giving Event Grid Topic access key