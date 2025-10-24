# Exercício 4) Fazer um programa que exiba a janela de diálogo três vezes, em cada uma, o
# usuário irá entrar com um número inteiro. Após isso o programa deverá imprimir na tela o somatório dos valores.

soma = 0

for i in range(1, 4):
     num = int(input(f"Digite o {i}° número inteiro: "))
     soma += num

print(f"O somatório dos valores é: {soma}")
