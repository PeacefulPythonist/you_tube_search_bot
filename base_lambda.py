"""
base_lambda.py: Includes essential functions for working with AWS Lambda.

Functions:
- get_message(event, name="message", json_file=False): Extracts a specified message from an event or bot updates.
"""

import json

import tgbot


def get_message(event, name="message", json_file=False):
    if event is not None:
        body = event['body']
        if type(body) == dict:
            return body[name]
        return json.loads(body).get(name)
    if json_file:
        with open("message.json") as json_file:
            return json.load(json_file).get(name)
    else:
        res = tgbot.get_updates()
        # print(res)
        return res["result"][-1].get(name)
