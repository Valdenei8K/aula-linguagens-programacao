
nome = input("Digite seu nome: ")
posicao = int(input("Digite a posição onde deseja adicionar uma letra: "))


if posicao < 0 or posicao >= len(nome):
    print("Posição inválida.")
else:

    letra = nome[posicao]

    
    if letra == 'r':
        nome = nome[:posicao] + 'S' + nome[posicao + 1:]
    elif letra == 'm':
        nome = nome[:posicao] + 'N' + nome[posicao + 1:]
    else:
      
        nome = nome[:posicao] + nome[posicao + 1:]

   
    print("Nome modificado:", nome)
