# Instalação Pre-commit
```
pip install pre-commit # instala biblioteca
pre-commit install # instala hooks no pre-commit (de acordo com o conteúdo do .pre-commit-config.yaml
```

## ℹ️ Como rodar todos os hooks manualmente

```bash
pre-commit run --all-files
```

# Hooks configurados no `.pre-commit-config.yaml`

Este projeto utiliza o [pre-commit](https://pre-commit.com/) para garantir a qualidade do código antes de cada commit. Abaixo está a descrição de cada hook configurado.

---

## 🔹 Hooks do repositório `pre-commit-hooks`

| Hook                     | Descrição                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| `check-yaml`             | Verifica se arquivos `.yaml` e `.yml` estão com sintaxe válida.          |
| `check-json`             | Verifica se arquivos `.json` estão bem formatados e válidos.             |
| `check-added-large-files`| Bloqueia arquivos maiores que 500KB para evitar commits acidentais.     |
| `end-of-file-fixer`      | Garante que todos os arquivos tenham uma **única quebra de linha** no final. |
| `trailing-whitespace`    | Remove espaços em branco no final das linhas.                            |

---

## 🐍 Hooks Python

| Hook       | Descrição                                                                                     |
|------------|-----------------------------------------------------------------------------------------------|
| `flake8`   | Verifica o estilo do código Python com base no PEP8. Usa também `flake8-print` para alertar sobre uso de `print()`. Ignora `W503`, `E402`, `F401`. |
| `black`    | Formata automaticamente o código Python de forma padronizada. Configurado com `--line-length=88`. |
| `isort`    | Organiza automaticamente os imports em ordem (bibliotecas padrão, de terceiros e locais).     |

---

## 📘 Markdown

| Hook          | Descrição                                                                                      |
|---------------|-----------------------------------------------------------------------------------------------|
| `markdownlint`| Verifica se os arquivos `.md` seguem boas práticas de escrita em Markdown. Usa `--fix` para corrigir automaticamente onde possível. |

---

