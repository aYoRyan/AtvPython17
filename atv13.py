# 13-João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de 
# R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável 
# peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos 
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados 
# do programa com as mensagens adequadas.

def calcular_excesso_multa(peso):
    limite_peso = 50.0
    excesso = max(peso - limite_peso, 0)  # O excesso é zero se o peso não ultrapassar o limite
    multa = excesso * 4.0
    return excesso, multa

peso_peixes = float(input("Digite o peso de peixes (em quilos): "))

excesso, multa = calcular_excesso_multa(peso_peixes)

print(f"Você excedeu o limite de peso em {excesso:.2f} kg.")
print(f"A multa a ser paga é de R$ {multa:.2f}.")