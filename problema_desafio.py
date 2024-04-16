def distancia_edicao(a, b):
    m, n = len(a), len(b)


    # Inicializa uma matriz para armazenar os resultados parciais
    dp = [[0] * (n + 1) for _ in range(m + 1)]


    # Inicializa a primeira coluna da matriz com valores de 0 a m
    for i in range(m + 1):
        dp[i][0] = i
    # Inicializa a primeira linha da matriz com valores de 0 a n
    for j in range(n + 1):
        dp[0][j] = j


    # Preenche a matriz dp com os custos mínimos de edição
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Se os caracteres atuais de a e b são iguais, o custo é o mesmo que o custo anterior
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # Caso contrário, o custo é 1 mais o mínimo dos custos das operações de inserção, remoção e substituição
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])


    # O valor final na última célula da matriz representa a distância de edição entre a e b
    return dp[m][n]


# Exemplos
print(distancia_edicao("asar", "casa"))  # Saída: 2
print(distancia_edicao("inserir", "inserção"))  # Saída: 3



