async function send() {
  const nome = document.getElementById("nome").value;
  const idade = document.getElementById("idade").value;
  const obs = document.getElementById("obs").value;

  const dataObj = { nome, idade, observacao: obs };
  const dataStr = JSON.stringify(dataObj);

  const key = new TextEncoder().encode("0123456789abcdef"); // 16 bytes
  const iv = crypto.getRandomValues(new Uint8Array(16));
  const enc = new TextEncoder();
  const encoded = enc.encode(dataStr);

  const cryptoKey = await crypto.subtle.importKey(
    "raw",
    key,
    { name: "AES-CBC" },
    false,
    ["encrypt"]
  );

  const encrypted = await crypto.subtle.encrypt(
    { name: "AES-CBC", iv: iv },
    cryptoKey,
    encoded
  );

  function toBase64(arr) {
    return btoa(String.fromCharCode(...new Uint8Array(arr)));
  }

  const payload = {
    iv: toBase64(iv),
    payload: toBase64(encrypted),
  };

  fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  })
    .then((res) => res.json())
    .then((data) => alert("Servidor respondeu:\n" + JSON.stringify(data.received, null, 2)))
    .catch((e) => alert("Erro: " + e));
}
