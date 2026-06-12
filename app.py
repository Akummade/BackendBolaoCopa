from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

from routes.auth import *
from routes.ranking import *
from routes.partidas import *
from routes.admin import *


@app.route("/")
def arquivoprincipal():
    return {
        "status":"online",
        "projeto":"Bolão Copa 2026"
    }
