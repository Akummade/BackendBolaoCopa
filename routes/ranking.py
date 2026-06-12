from app import app
from database.connection import get_connection

@app.route("/api/ranking")
def ranking():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            u.nome,
            r.pontuacao_total
        FROM ranking_usuario r
        INNER JOIN usuario u
        ON u.id_usuario = r.id_usuario
        ORDER BY r.pontuacao_total DESC
    """)

    resultado = cursor.fetchall()

    conn.close()

    return resultado