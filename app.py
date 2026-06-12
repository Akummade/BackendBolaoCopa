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
    
from database.connection import get_connection

@app.route("/db-test")
def db_test():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT 1")

    resultado = cursor.fetchone()

    conn.close()

    return {
        "database": "conectado",
        "resultado": resultado
    }
