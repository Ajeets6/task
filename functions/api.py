from app import app as flask_app
import json
import os
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    if request.method == 'OPTIONS':
        return Response("", status=200)

    with flask_app.request_context(request.environ):
        try:
            response = flask_app.dispatch_request()
            response_data = json.loads(response.data)
            return Response(json.dumps(response_data), content_type="application/json", status=response.status_code)
        except Exception as e:
            return Response(json.dumps({"error": str(e)}), content_type="application/json", status=500)

def handler(event, context):
    return application(event, context)
