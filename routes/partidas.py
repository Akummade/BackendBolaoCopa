from app import app
from database.connection import get_connection

@app.route("/api/partidas")
def partidas():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.id_partida,
            casa.nome AS time_casa,
            fora.nome AS time_fora,
            p.placar_casa,
            p.placar_fora,
            p.status,
            p.data_hora
        FROM partida p

        INNER JOIN selecao casa
        ON casa.id_selecao = p.id_time_casa

        INNER JOIN selecao fora
        ON fora.id_selecao = p.id_time_fora
    """)

    dados = cursor.fetchall()

    conn.close()

    return dados