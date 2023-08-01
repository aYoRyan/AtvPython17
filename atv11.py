# 11-Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

altura = float(input("Digite sua altura em metros: "))
peso_ideal = calcular_peso_ideal(altura)
print(f"Seu peso ideal é: {peso_ideal:.2f} kg")