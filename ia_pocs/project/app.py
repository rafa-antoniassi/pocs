import json
from base64 import b64decode

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

rsa_key = RSA.generate(2048)
private_key = rsa_key
public_key = rsa_key.publickey().export_key().decode()

cipher_rsa = PKCS1_v1_5.new(private_key)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/public-key")
def public_key_route():
    return public_key, 200, {"Content-Type": "text/plain"}


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    encrypted = data.get("payload")

    if not encrypted:
        return {"error": "Missing payload"}, 400

    try:
        encrypted_bytes = b64decode(encrypted)
        sentinel = get_random_bytes(32)
        decrypted_bytes = cipher_rsa.decrypt(encrypted_bytes, sentinel)
        if decrypted_bytes == sentinel:
            return {"error": "Falha na descriptografia"}, 400

        decrypted_json = json.loads(decrypted_bytes.decode())
        return jsonify({"received": decrypted_json}), 200

    except Exception as e:
        return {"error": f"Erro na descriptografia: {str(e)}"}, 400


if __name__ == "__main__":
    app.run(debug=True)
