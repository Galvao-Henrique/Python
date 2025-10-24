# Exercício 1) Fazer um programa para calcular o fatorial de um número. Para se calcular o fatorial
# de um número, é necessário multiplicar ele por todos os seus antecessores até chegar número 1.
# Exemplo: para calcular o fatorial de 5 é necessário multiplicar 5 x 4 x 3 x 2 x 1.

fatorial = int(input("Digite um número para calcular o fatorial: "))

for i in range(1, fatorial):
     fatorial *= i

print(f"O fatorial do número é: {fatorial}")