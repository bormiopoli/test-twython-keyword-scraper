import json


# Import the credentials stored in a json file
def openfile(path):
    with open(path, "r") as file:
        credentials = json.loads(file.read())['credentials']
        key = credentials['CONSUMER_KEY']
        secret = credentials['CONSUMER_SECRET']
        acc_token = credentials['ACCESS_TOKEN']
        acc_secret = credentials['ACCESS_SECRET']

    return key, secret, acc_token, acc_secret





