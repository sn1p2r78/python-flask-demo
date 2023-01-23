import os
import sys
import socket

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    version = sys.version_info
    res = (
        "<h1>Hello my friends</h1>"
        f"<h2>{os.getenv('ENV')}</h2></br>"
        f"Running Python: {version.major}.{version.minor}.{version.micro}<br>"
        f"Hostname: {socket.gethostname()}"
    )
    return res
