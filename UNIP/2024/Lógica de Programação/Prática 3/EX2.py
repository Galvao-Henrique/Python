# Exercício 2) Fazer um programa para que o usuário entre com um número inteiro. Após isso, o
# programa deve calcular o termo correspondente da sequência de Fibonacci.

n = int(input("Digite um número inteiro para calcular o termo correspondente da sequência de Fibonacci: "))

primeiro = 1
segundo = 1

print(primeiro)
print(segundo)

for i in range(1, n):
     soma = primeiro + segundo
     primeiro = segundo
     segundo = soma
     print(soma)