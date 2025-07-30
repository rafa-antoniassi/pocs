import json
from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

SECRET_KEY = b"0123456789abcdef"  # 16 bytes para AES-128


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    iv = b64decode(data["iv"])
    ciphertext = b64decode(data["payload"])

    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    decrypted_json = json.loads(decrypted.decode())

    return jsonify({"received": decrypted_json}), 200


if __name__ == "__main__":
    app.run(debug=True)
