# Escreva um algoritmo que leia o peso de 
# 3 pacientes e apresente na tela a média desses pesos.
peso_um     = float(input('Digite o peso do paciente um: '))
peso_dois   = float(input('Digite o peso do paciente dois: '))
peso_tres   = float(input('Digite o peso do paciente três: '))

media = (peso_um + peso_dois + peso_tres) / 3

print('A média dos pesos é igual a ' , media)