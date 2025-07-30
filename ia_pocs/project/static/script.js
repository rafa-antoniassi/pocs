async function send() {
  const nome = document.getElementById("nome").value;
  const idade = document.getElementById("idade").value;
  const obs = document.getElementById("obs").value;

  const dataObj = { nome, idade, observacao: obs };
  const dataStr = JSON.stringify(dataObj);

  const pubKey = await fetch("/public-key?ts=" + Date.now()).then((res) => res.text());

  const encryptor = new JSEncrypt();
  encryptor.setPublicKey(pubKey);

  const encrypted = encryptor.encrypt(dataStr);

  if (!encrypted) {
    alert("Erro ao criptografar.");
    return;
  }

  const payload = { payload: encrypted };

  const res = await fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const data = await res.json();
  if (data.received) {
    alert("Servidor respondeu:\n" + JSON.stringify(data.received, null, 2));
  } else {
    alert("Erro: " + JSON.stringify(data));
  }
}
