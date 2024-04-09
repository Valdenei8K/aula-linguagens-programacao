nome_completo = input("Digite seu nome e sobrenome: ")


nome, sobrenome = nome_completo.split()


#nome_formatado = nome.capitalize()
#sobrenome_formatado = sobrenome.capitalize()


nome_formatado = nome_formatado[0].lower() + nome_formatado.upper()[1:]
sobrenome_formatado = sobrenome_formatado[0].upper() + sobrenome_formatado[1:]


print(nome_formatado, sobrenome_formatado)  