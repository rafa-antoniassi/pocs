from base64 import b64decode

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Gera par de chaves RSA na inicialização
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

    try:
        encrypted_bytes = b64decode(encrypted)
        sentinel = get_random_bytes(32)  # fallback em caso de falha silenciosa
        decrypted_bytes = cipher_rsa.decrypt(encrypted_bytes, sentinel)

        if decrypted_bytes == sentinel:
            raise ValueError("Falha de descriptografia (sentinela detectada)")

        return jsonify({"received": decrypted_bytes.decode()}), 200
    except Exception:
        return {"error": "Decryption failed"}, 400


if __name__ == "__main__":
    app.run(debug=True)
