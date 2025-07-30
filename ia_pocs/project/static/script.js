async function send() {
  const msg = document.getElementById("message").value;

  // Chave e IV precisam ser as mesmas do servidor
  const key = new TextEncoder().encode("0123456789abcdef"); // 16 bytes
  const iv = crypto.getRandomValues(new Uint8Array(16));

  const enc = new TextEncoder();
  const data = enc.encode(msg);

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
    data
  );

  const payload = {
    iv: btoa(String.fromCharCode(...iv)),
    payload: btoa(String.fromCharCode(...new Uint8Array(encrypted)))
  };

  fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  })
  .then(res => res.json())
  .then(data => alert("Servidor respondeu: " + data.received));
}
