# biblioteca Python que é usada principalmente para realizar cálculos em Arrays Multidimensionais
import numpy as np
# biblioteca Python que fornece ferramentas de análise de dados e estruturas de dados de alta performance
import pandas as pd  
# biblioteca Python para geração de gráficos 2D
import matplotlib as mpl
import matplotlib.pyplot as plt
# é uma interface em Python estruturada para obter informações da API de dados abertos do Banco Central do Brasil.
from bcb import sgs     #https://wilsonfreitas.github.io/python-bcb/sgs.html
from bcb import currency     #https://wilsonfreitas.github.io/python-bcb/currency.html

## Variáveis globais
#UF = []

## Função: IPCA dos últimos 12 meses
def IPCA_12_meses():
    print('*** IPCA dos últimos 12 meses ***')
    df = sgs.get(('IPCA', 433),last=12)
    print(df)    

## Função: IPCA acumulado 12 meses
def IPCA_acumulado():
    print('*** IPCA acumulado 12 meses ***')
    mpl.style.use('bmh')
    df = sgs.get({'IPCA': 433}, start='2002-02-01')
    df.index = df.index.to_period('M')
    print("IPCA 1",df.head())
    dfr = df.rolling(12)
    i12 = dfr.apply(lambda x: (1 + x/100).prod() - 1).dropna() * 100
    print("IPCA Acumulado",i12.head())
    i12.plot(figsize=(12,6))
    plt.title('Fonte: https://dadosabertos.bcb.gov.br', fontsize=10)
    plt.suptitle('IPCA acumulado 12 meses - Janela Móvel', fontsize=18)
    plt.xlabel('Data')
    plt.ylabel('%')
    plt.legend().set_visible(False)
    plt.show()

## Função: Conversor de Moedas    #https://pt.wikipedia.org/wiki/ISO_4217
def ConversorMoedas():
    print('*** Conversor de Moedas ***')
    df = currency.get(['USD', 'EUR', 'CNY', 'GBP'],     
                  start='2023-01-01',
                  end='2023-11-01',
                  side='ask')
    print(df.head())
    df.plot(figsize=(12, 6))
    plt.title('Fonte: https://dadosabertos.bcb.gov.br', fontsize=10)
    plt.suptitle('Conversor de Moedas - Janela Móvel', fontsize=18)
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.show()

######## INÍCIO DO PROGRAMA ########
print("######## Início do Programa Acesso a API de dados abertos do Banco Central do Brasil ########")
opcao = 999

while opcao != 0:
    print("***********************************")
    print("Entre com a opção:")
    print(" --- 0: Sair do programa")
    print(" --- 1: IPCA dos últimos 12 meses")
    print(" --- 2: IPCA acumulado")
    print(" --- 3: Conversor de Moedas")
    print("***********************************")
    opcao = int(input("-> "))

    if opcao == 1:
        IPCA_12_meses()
    elif opcao == 2:
        IPCA_acumulado()
    elif opcao == 3:
        ConversorMoedas()
    elif opcao == 0:
          break