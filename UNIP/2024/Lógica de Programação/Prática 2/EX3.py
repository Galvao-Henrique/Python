# Exercício 3) Fazer um programa que imprima na tela a média dos números ímpares que estão no intervalo entre 0 e 100.

soma = 0
cont = 0

for i in range(1, 101, 2):
     soma += i
     cont += 1

media = soma / cont
print(media)