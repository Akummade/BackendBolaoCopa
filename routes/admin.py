from flask import request
from app import app
from database.connection import get_connection

@app.route(
    "/api/admin/partida/<int:id>",
    methods=["PUT"]
)
def atualizar_partida(id):

    dados = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE partida
        SET
            placar_casa = %s,
            placar_fora = %s,
            status = %s
        WHERE id_partida = %s
    """,
    (
        dados["placar_casa"],
        dados["placar_fora"],
        dados["status"],
        id
    ))

    conn.commit()
    conn.close()

    return {
        "success":True
    }