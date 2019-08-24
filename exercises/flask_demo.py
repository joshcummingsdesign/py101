import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    res = {
        'name': 'messenger',
        'playstore': True,
        'company': "Facebook",
        'price': 100
    }
    return json.dumps(res)
