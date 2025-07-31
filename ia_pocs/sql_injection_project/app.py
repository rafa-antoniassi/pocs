import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def init_db():
    """
    Inicializa o banco de dados e cria a tabela de usuários se ela não existir.
    """
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        conn.commit()


init_db()


@app.route("/")
def index():
    """
    Rota principal que exibe o formulário de cadastro de usuário.
    """
    return render_template("form.html")


@app.route("/users", methods=["POST"])
def create_user():
    """
    Cria um novo usuário com os dados fornecidos no formulário.
    Valida os campos e executa a inserção com segurança.
    """
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not email:
        return "Campos obrigatórios: nome e e-mail", 400

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO user (name, email) VALUES (?, ?);",
                (name, email)
            )
            conn.commit()
        return f"Usuário {name} criado com sucesso!"
    except sqlite3.IntegrityError:
        return "E-mail já cadastrado.", 400
    except Exception as e:
        return f"Erro: {e}", 500


@app.route("/search")
def search_user():
    """
    Realiza a busca por usuários com base na query string 'q'.
    Utiliza LIKE com parâmetro para evitar SQL Injection.
    """
    q = request.args.get("q", "").strip()
    results = []
    error = None

    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if q:
                cursor.execute("SELECT * FROM user WHERE name LIKE ?", (f"%{q}%",))
            else:
                cursor.execute("SELECT * FROM user")
            results = cursor.fetchall()
    except Exception as e:
        error = str(e)

    return render_template("search.html", results=results, q=q, error=error)


if __name__ == "__main__":
    app.run(debug=True)
