from flask import request
from app import app
from database.connection import get_connection

@app.route("/api/login", methods=["POST"])
def login():

    dados = request.json

    login = dados["login"]
    senha = dados["senha"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM usuario
        WHERE login = %s
        AND senha = %s
    """,(login, senha))

    usuario = cursor.fetchone()

    conn.close()

    if usuario:

        return {
            "success": True,
            "id": usuario["id_usuario"],
            "nome": usuario["nome"],
            "tipo": usuario["tipo_usuario"]
        }

    return {
        "success": False
    },401