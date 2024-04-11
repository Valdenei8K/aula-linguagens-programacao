def decapitalize(s):
    if len(s) == 0:
        return s
    else:
        return s[0].lower() + s[1:].upper()

texto = "Arlene Silva"
texto_formatado = decapitalize(texto)
print(texto_formatado)  # Saída: "exemplo de Texto"

textocaptalizado= texto_formatado.capitalize()
print(textocaptalizado)