#Problema: Escreva um algoritmo em Python que recebe o peso e a 
# altura e informa a classificação dela segundo a tabela do IMC abaixo.
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

if (imc < 18.5):
    print("Você está abaixo do peso")
elif (imc < 25):
    print("Você está no peso ideal")
elif (imc < 30 ):
    print("Você está com sobrepeso")
elif (imc < 35):
    print("Opa! Você está com obesidade grau I")
elif (imc < 40):
    print("Opa! Você está com obesidade grau II")
else:
    print("Opa! Você está com obesidade grau III")