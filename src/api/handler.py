import json
import requests

def handler(event, context):
    response = requests.get('https://api.github.com/orgs/Pontte/repos')
    print(response.text)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
