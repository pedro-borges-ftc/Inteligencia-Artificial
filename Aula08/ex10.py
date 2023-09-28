#Problema: Em Python, faça um programa que simule um lançamento de dados. 
#Lance o dado 100 vezes e armazene os resultados em um vetor . 
#Depois, mostre quantas vezes cada valor foi conseguido. 
#Dica: use um vetor de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
from random import randint

def geraNumeroAleatorio():
    return randint(1,6)

def lancarDados():
    dados = [0,0,0,0,0,0,0]
    num = 0
    for i in range(0,100):
        num = geraNumeroAleatorio()
        dados[num] += 1
    return dados

#MAIN
contDados = lancarDados()
for i in range(1, 7):
    print(f'{i}',f'foi sorteado {contDados[i]} vezes')