##O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

# Entrada do texto
texto = input()

# Verifica se o comprimento do texto é menor ou igual a 140
if len(texto) <= 14:
    print("Postado!")
else:
    print("Ultrapassou a quantidade de caracteres permitido (max:40)")
