async function send() {
  const message = document.getElementById("message").value;

  // Obtem a chave pública
const pubKey = await fetch("/public-key?ts=" + Date.now()).then(res => res.text());

  // Usa JSEncrypt para criptografar
  const encryptor = new JSEncrypt();
  encryptor.setPublicKey(pubKey);

  const encrypted = encryptor.encrypt(message);

  if (!encrypted) {
    alert("Erro ao criptografar.");
    return;
  }

  const payload = { payload: encrypted };

  const res = await fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();
  alert("Servidor respondeu: " + data.received);
}
