# Imports fora de ordem — será corrigido pelo isort
import json
import os  # ordem alfabética incorreta

def carregar_configuracoes(caminho_config):
    with open(caminho_config, 'r') as f:
        return json.load(f)  # Correto

def exibir_boas_vindas(usuario):
    print(f"Bem-vindo, {usuario}!")  # flake8-print: uso de print deve ser evitado
    print("Sistema iniciado com sucesso.")  # flake8-print novamente

# Falta uma linha em branco no fim do arquivo — corrigido pelo end-of-file-fixer
# Espaço em branco no final da linha abaixo — corrigido pelo trailing-whitespace  
if __name__ == "__main__":
    config = carregar_configuracoes("config.json")
    exibir_boas_vindas(config.get("usuario", "Convidado"))  