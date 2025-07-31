import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


# Criação da tabela User (se não existir)
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
    """
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/users", methods=["POST"])
def create_user():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        return "Campos obrigatórios: nome e e-mail", 400

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # INSERÇÃO VULNERÁVEL (sem parâmetros)
        cursor.executescript(
            f"""
            INSERT INTO user (name, email) VALUES ('{name}', '{email}');
        """
        )
        conn.commit()
        conn.close()
        return f"Usuário {name} criado com sucesso!"
    except Exception as e:
        return f"Erro: {e}", 500


@app.route("/search")
def search_user():
    q = request.args.get("q", "")
    results = []
    error = None

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        if q:
            # Consulta com filtro - vulnerável para testes
            cursor.executescript(f"SELECT * FROM user WHERE name LIKE '%{q}%';")
            cursor.execute(f"SELECT * FROM user WHERE name LIKE '%{q}%'")
        else:
            # Consulta sem filtro: traz todos os usuários
            cursor.executescript("SELECT * FROM user;")
            cursor.execute("SELECT * FROM user")
        results = cursor.fetchall()
        conn.close()
    except Exception as e:
        error = str(e)

    return render_template("search.html", results=results, q=q, error=error)


if __name__ == "__main__":
    app.run(debug=True)
