from cloudevents.http import CloudEvent, to_structured
import os
import requests


def lambda_handler(event, context):
    event_data = event["Records"][0]
    attributes = {
        "specversion": "1.0",
        "id": f"{event_data['responseElements']['x-amz-request-id']}.{event_data['responseElements']['x-amz-id-2']}",
        "type": f"com.amazonaws.s3.{event_data['eventName']}",
        "source": f"{event_data['eventSource']}.{event_data['awsRegion']}.{event_data['s3']['bucket']['name']}",
        "subject": f"s3://{event_data['s3']['bucket']['name']}/{event_data['s3']['object']['key']}",
        "time": event_data["eventTime"],
    }
    data = event_data

    cloudevent = CloudEvent(attributes, data)
    
    headers, body = to_structured(cloudevent)
    headers["aeg-sas-key"] = os.getenv("EVENTGRID_KEY")
    
    requests.post(os.getenv("EVENT_URL"), data=body, headers=headers)

    return {"statusCode": 200}
