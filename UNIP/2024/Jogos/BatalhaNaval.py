import random

# Matriz
arena = []
for l in range(6):
    linha = []
    for c in range(6):
        linha.append('O')
    arena.append(linha)

# Matriz visível
arena2 = []
for l in range(6):
    linha2 = []
    for c in range(6):
        linha2.append('O')
    arena2.append(linha2)

# Navios
for i in range(10):
    lin = random.randrange(6)
    col = random.randrange(6)
    if arena[lin][col] != 'N':
        arena[lin][col] = 'N'

# Variável de jogadas
acertos = 0
jogadas = 0
# Escolha 
while True:
    jogadas += 1
    # Exibe a matriz visível após cada jogada
    for linha2 in arena2:
        print("[" + ", ".join(linha2) + "]")
    
    # Solicita a jogada
    n1 = int(input('Digite a linha de 0 a 5: '))
    n2 = int(input('Digite a coluna de 0 a 5: '))
    
    if 0 <= n1 <= 5 and 0 <= n2 <= 5:  
        if arena[n1][n2] == 'N':  
            print('Acertou!')
            print()
            arena2[n1][n2] = 'X'  # Marca um acerto
            acertos += 1
        else:
            print('Errou')
            print()
            arena2[n1][n2] = 'E'  # Marca um erro
    else:
        print('Fora do intervalo!')
    
    # Verifica se acertou todos os navios
    if acertos == 10:  
        print('Acertou todos!')
        print(f'Em {jogadas} tiros! ')
        print()
        break