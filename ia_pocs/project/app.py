from base64 import b64decode

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from flask import Flask, render_template, request

app = Flask(__name__)

# A mesma chave usada no JS (16, 24 ou 32 bytes)
SECRET_KEY = b"0123456789abcdef"


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

    return {"received": decrypted.decode()}, 200


if __name__ == "__main__":
    app.run(debug=True)
