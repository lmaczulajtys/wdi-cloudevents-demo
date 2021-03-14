from cloudevents.http import from_http
from flask import make_response


def handle_request(request):
    if request.method == "OPTIONS":
        response = make_response()
        # For demo purposes only. Read about abuse protection at
        # https://github.com/cloudevents/spec/blob/v1.0/http-webhook.md#4-abuse-protection
        response.headers["WebHook-Allowed-Origin"] = request.headers[
            "WebHook-Request-Origin"
        ]
        response.headers["WebHook-Allowed-Rate"] = "*"
        return response
    else:
        event = from_http(request.headers, request.get_data())
        handle_cloudevent(event)
        return "", 204


def handle_cloudevent(cloudevent):
    print(f"subject:{cloudevent['subject']}")
