import os

mensagens = []

nome = input("Nome: ")

while True:
    # Limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

     print("______________")

     texto = input("mensagens: ")
  if texto == "FIM":
    break

 # Adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
