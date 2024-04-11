# Recebe o nome do usuário e a posição desejada para adicionar uma letra
nome = input("Digite seu nome: ")
posicao = int(input("Digite a posição onde deseja adicionar uma letra: "))

# Verifica se a posição indicada é válida
if posicao < 0 or posicao >= len(nome):
    print("Posição inválida.")
else:
    # Verifica a letra na posição indicada
    letra = nome[posicao]

    # Substitui a letra conforme as condições
    if letra == 'r':
        nome = nome[:posicao] + 'S' + nome[posicao + 1:]
    elif letra == 'm':
        nome = nome[:posicao] + 'N' + nome[posicao + 1:]
    else:
        # Remove a letra se não for 'm' ou 'r'
        nome = nome[:posicao] + nome[posicao + 1:]

    # Exibe o nome modificado
    print("Nome modificado:", nome)
