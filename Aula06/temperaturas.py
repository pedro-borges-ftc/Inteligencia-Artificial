#Em Python, vamos criar um programa que receba a temperatura média 
# de cada mês do ano e armazene-as em uma lista. 

#Após isto, calcule a média anual das temperaturas e mostre todas 
# as temperaturas acima da média anual, e em que mês elas ocorreram 
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import numpy as np 

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro' , 'Novembro' , 'Dezembro']
#print(meses)

temperaturas = [] #[30.0, 35.0, 45.0, 25.0, 12.0, 15.0, 16.0, 17.0, 23.0, 28.0, 45.0, 65.0]

for i in range(0, 12):
    print(f'Digite a temperatura de {meses[i]}:')
    temperaturas.append(float(input('')))
#print(temperaturas)

media = np.average(temperaturas)
print(f'A média anual é: {media} ºC')

for i in range(0, 12):
    if(temperaturas[i] > media):
        print(f'Temperatura acima da média anual em {meses[i]}: {temperaturas[i]}')