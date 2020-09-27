import json
import redis
import os

from flask import Flask, request
from typing import Text, Optional, Dict, Any

app = Flask(__name__)

REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

def get_current_user() -> Optional[Dict[Text, Any]]:
    """Retrieve the current user from intermediate storage."""

    red = redis.StrictRedis(host="redis", port=6379, db=1, password=REDIS_PASSWORD)
    encoded_user = red.get("user")
    if encoded_user:
        return json.loads(encoded_user)
    else:
        return None


def store_user(user: Dict[Text, Any]) -> None:
    """Store a users details to our intermediate storage."""

    red = redis.StrictRedis(host="redis", port=6379, db=1, password=REDIS_PASSWORD)
    red.set("user", json.dumps(user))


@app.route('/', methods=["GET"])
def greet():
    """Send a welcoming message to the user."""

    user = get_current_user()
    if user is not None:
        return "Hello, {}!".format(user.get("name"))
    else:
        return "Hello, unknown stranger!"


@app.route('/', methods=["POST"])
def save_name():
    """Change a users details, most importantly his name."""

    user = request.json
    store_user(user)
    return "I'll try to remember your name, {}!".format(user.get("name"))


app.run(port=9090, host='0.0.0.0')

