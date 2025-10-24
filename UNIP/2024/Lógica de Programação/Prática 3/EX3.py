# Exercício 3) Muitos não sabem, mas o Real não foi a única moeda que circulou pelo Brasil. Antes
# do plano Real (1994-atualmente), o nome da nossa moeda era Cruzeiro Real (1993-1994) e antes
# disso era o Cruzeiro (1990-1993). Criar um programa que converta uma quantia em Real, para
# Cruzeiro Real e Cruzeiro.

# Para transformar o Real em Cruzeiro Real, basta multiplicar o valor em reais por 2.750.
# Para transformar o Cruzeiro Real em Cruzeiro, basta multiplicar o valor por 1.000.

real = float(input("Digite o valor em Reais (R$): "))
cruzeiro_real = real * 2750
cruzeiro = cruzeiro_real * 1000
print(f"O valor em Cruzeiro Real é: CR$ {cruzeiro_real}")
print(f"O valor em Cruzeiro é: Cr$ {cruzeiro}")
