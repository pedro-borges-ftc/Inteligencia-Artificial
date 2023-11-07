import numpy as np
import statistics
import matplotlib.pyplot as plt

## Variáveis globais
idades = []
sexos = []
pesos = []
temperaturas = []
nomes = []

## Função de leitura dos dados no arquivo txt
def lerArquivo():
    print("Início da leitura do arquivo")
    ref_arq_hospital = open("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula12/hospital.txt","r")
    #ref_arq_hospital = open("C:/Users/Pedro/Projetos VSCode/Inteligencia-Artificial/Aula11/hospital.txt","r")
    for linha in ref_arq_hospital:
        valores = linha.split()
        print(valores)
        nomes.append(valores[1])
        idades.append(float(valores[2]))
        sexos.append(valores[3])
        pesos.append(float(valores[4]))
        temperaturas.append(float(valores[6]))
 
    ref_arq_hospital.close()
    print("Fim da leitura do arquivo")

## Função de impressão dos dados lidos no arquivo
def imprimirDados():
    print("******DADOS LIDOS NO ARQUIVO*******")
    print("Nomes: ",nomes)
    print("Idades: ",idades)
    print("Sexos: ",sexos)
    print("Pesos: ",pesos)
    print("Temperaturas: ",temperaturas)

## Função para o cálculo das médias
def calcularMedias():
    print("******Médias*******")
    print("Idades: ",np.average(idades))
    print("Pesos: ",np.average(pesos))
    print("Temperaturas: ",np.average(temperaturas))

## Função para o cálculo do desvio padrão
def calcularDesvioPadrao():
    print("******Desvio Padrão*******")
    print("Idades: ",np.std(idades))
    print("Pesos: ",np.std(pesos))
    print("Temperaturas: ",np.std(temperaturas))

## Função para o cálculo das variâncias
def calcularVariancias():
    print("******Variâncias*******")
    print("Idades: ",np.var(idades))
    print("Pesos: ",np.var(pesos))
    print("Temperaturas: ",np.var(temperaturas))

## Função para o cálculo das modas
def calcularModas():
    print("******Modas*******")
    print("Sexos: ") 
    print(statistics.mode(sexos))
    print("Nomes: ") 
    print(statistics.mode(nomes))

## INÍCIO DO PROGRAMA
print("Início do Programa Hospital")
opcao = 999

while opcao != 0:
    print("***********************************")
    print("Entre com a opcao:")
    print(" --- 0: Sair do programa")
    print(" --- 1: Ler o arquivo de dados")
    print(" --- 2: Imprimir os dados lidos")
    print(" --- 3: Calcular médias")
    print(" --- 4: Calcular modas")
    print(" --- 5: Calcular desvio padrão")
    print(" --- 6: Calcular variâncias")
    print(" --- 7: Gráfico Idades X Pesos")
    print(" --- 8: Gráfico Nomes X Temperaturas")
    print("***********************************")
    opcao = int(input("-> "))

    if opcao == 1:
       lerArquivo()
    elif opcao == 2:
       imprimirDados()
    elif opcao == 3:
       calcularMedias()
    elif opcao == 4:
       calcularModas()
    elif opcao == 5:
       calcularDesvioPadrao()
    elif opcao == 6:
       calcularVariancias()
    elif opcao == 7:
        #Gráfico X , Y
        plt.xlabel('Idades')
        plt.ylabel('Pesos')
        plt.plot(idades, pesos, 'go')
        plt.show()
    elif opcao == 8:
        #Gráfico X , Y
        plt.xlabel('Nomes')
        plt.ylabel('Temperaturas')
        plt.plot(nomes, temperaturas)
        plt.show()
    elif opcao == 0:
          break