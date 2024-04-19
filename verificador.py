def verificar_ganhador():
    # Verificando linhas e colunas
    for i in range(3):
        # Verificando linhas
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]  # Retorna o símbolo do jogador vencedor
        # Verificando colunas
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]  # Retorna o símbolo do jogador vencedor
    
    # Verificando diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]  # Retorna o símbolo do jogador vencedor
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]  # Retorna o símbolo do jogador vencedor
    
    # Verificando empate
    for linha in tabuleiro:
        if " " in linha:
            return None  # Ainda há espaços em branco, o jogo continua
    return "Empate"  # Todos os espaços foram preenchidos e não há vencedor
