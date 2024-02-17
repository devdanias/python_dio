#APRENDENDO A UTILIZAR DICIONÁRIOS EM PYTHON
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "333-2221"},
    "daniele@gmail.com": {"nome": "Daniele", "telefone": "3343-2561"},
    "bruno@gmail.com": {"nome": "Bruni", "telefone": "8989-3233", "extra": {"a":1}},
}
telefone = contatos["daniele@gmail.com"]["telefone"]
print(telefone)

extra = contatos["guilherme@gmail.com"]["extra"]["a"]
print(extra)

