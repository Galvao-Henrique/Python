# Exercício 5) Fazer um programa para calcular o Índice de Massa Corporal. O programa deverá
# exibir a janela de diálogo duas vezes, na primeira vez o usuário deverá fornecer o peso e na
# segunda a altura. Em seguida, o programa deverá imprimir na tela o valor do IMC. A fórmula de
# cálculo do IMC é peso/(altura*altura).

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

IMC = peso / (altura * altura)
print(f"Seu Índice de Massa Corporal (IMC) é: {IMC}")