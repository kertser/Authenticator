# This is a placeholder for future library, that will generate the GUI template for client UI
import json


def get_template(user_token=None, path='templates/sample_template.json'):
    if user_token is None:  # return base template
        # return json string from file
        file = open(path, 'r')
        # decode json string
        return json.loads(file.read())
