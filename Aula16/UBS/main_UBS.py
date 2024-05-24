# biblioteca Python que é usada principalmente para realizar cálculos em Arrays Multidimensionais
import numpy as np
# biblioteca Python que fornece ferramentas de análise de dados e estruturas de dados de alta performance
import pandas as pd  
# biblioteca Python para geração de gráficos 2D
import matplotlib.pyplot as plt

## Variáveis globais
CNES = []
UF = []
IBGE = []
NOME = []
LOGRADOURO = []
BAIRRO = []
LATITUDE = []
LONGITUDE = []

## Função de leitura dos dados no arquivo txt
def lerArquivo():
    print("Início da leitura do arquivo")
    ref_arq_UBS = open("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula16/UBS/UBS_Modificado.csv","r")
    #ref_arq_UBS = open("C:/Users/Pedro/Projetos VSCode/Inteligencia-Artificial/Aula16/UBS/UBS_Modificado.csv","r")
    for linha in ref_arq_UBS:
        linha = linha.strip()
        valores = linha.split(';')
        print(valores)
        if valores[0] != 'CNES':    #Esse teste pula a 1ª linha
            CNES.append(valores[0])
            UF.append(ufPorCodigoIBGE(valores[1]))
            IBGE.append(float(valores[2]))
            NOME.append(valores[3])
            LOGRADOURO.append(valores[4])
            BAIRRO.append(valores[5])
            LATITUDE.append(valores[6])     #será lido como texto
            LONGITUDE.append(valores[7])    #será lido como texto
 
    ref_arq_UBS.close()
    print("Fim da leitura do arquivo")

## Função para traduzir o código no nome da UF
def ufPorCodigoIBGE(uf = ''):
    if uf == '12':
        return 'Acre'
    elif uf == '27':
        return 'Alagoas'
    elif uf == '16':
        return 'Amapá'
    elif uf == '13':
        return 'Amazonas'
    elif uf == '29':
        return 'Bahia'
    elif uf == '23':
        return 'Ceará'
    elif uf == '53':
        return 'Distrito Federal'
    elif uf == '32':
        return 'Espírito Santo '
    elif uf == '52':
        return 'Goiás'
    elif uf == '21':
        return 'Maranhão'
    elif uf == '51':
        return 'Mato Grosso'
    elif uf == '50':
        return 'Mato Grosso do Sul'
    elif uf == '31':
        return 'Minas Gerais'
    elif uf == '15':
        return 'Pará'
    elif uf == '25':
        return 'Paraíba'
    elif uf == '41':
        return 'Paraná'
    elif uf == '26':
        return 'Pernambuco'
    elif uf == '22':
        return 'Piauí'
    elif uf == '24':
        return 'Rio Grande do Norte'
    elif uf == '43':
        return 'Rio Grande do Sul'
    elif uf == '33':
        return 'Rio de Janeiro'
    elif uf == '11':
        return 'Rondônia'
    elif uf == '14':
        return 'Roraima'
    elif uf == '42':
        return 'Santa Catarina'
    elif uf == '35':
        return 'São Paulo'
    elif uf == '28':
        return 'Sergipe'
    elif uf == '17':
        return 'Tocantins'

## Função para exibir os código das UF
def ImprimeUFsCodigos():    
    ref_arq_UFs = open("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula16/UBS/Tabela-Codigo-UF-IBGE.txt","r")
    for ln in ref_arq_UFs:
        ln = ln.strip()
        valores = ln.split('\t')
        print(valores)

    ref_arq_UFs.close()

## Função: Qual a quantidade de UBS por estado?
def quantidadeUbsPorUF(escolha = ''):
    if escolha == '':
        ImprimeUFsCodigos()
        escolha = input("Digite o Código da Unidade Federativa: -->")
    print(ufPorCodigoIBGE(escolha),": ",str(repr(UF).count(escolha)) , "UBSs")

## Função: Qual a quantidade de UBS por cidade?
def quantidadeUbsPorCidade(escolha = ''):
    if escolha == '':
        escolha = input("Digite o Código da cidade: -->")
    print(str(repr(IBGE).count(escolha)) , "UBSs")

## Função: Leitura
def processamentoDeDados():
    df = pd.read_csv("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula16/UBS/UBS_Modificado.csv")
    #df = pd.read_csv("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula16/UBS/UBS.csv")
    #df = pd.read_csv("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula16/UBS/distribuicao_respiradores.csv")

    # carregando uma amostra de 5 registros
    print(df.head())

    # quantidade de registros
    print(df.shape[0])

    # enumerando os atributos constantes no dataframe
    print(df.columns)

    #verificando os estados atendidos
    #print(len(df["UF"].unique()))    

######## INÍCIO DO PROGRAMA ########
print("######## Início do Programa Acesso Dados Portal Brasileiro ########")
opcao = 999

while opcao != 0:
    print("***********************************")
    print("Entre com a opcao:")
    print(" --- 0: Sair do programa")
    print(" --- 1: Ler o arquivo de dados - CSV")
    print(" --- 2: Qual a quantidade de UBS por estado?")
    print(" --- 3: Qual a quantidade de UBS na Bahia?")
    print(" --- 4: Qual a quantidade de UBS em Itabuna?")
    print(" --- 5: Processamento Dados")
    print(" --- 6: Qual a quantidade de UBS por cidade?")
    print("***********************************")
    opcao = int(input("-> "))

    if opcao == 1:
       lerArquivo()
    elif opcao == 2:
       quantidadeUbsPorUF()
    elif opcao == 3:
        quantidadeUbsPorUF('29')    #bahia
    elif opcao == 4:
        quantidadeUbsPorCidade('291480')    #itabuna
    elif opcao == 5:
        processamentoDeDados()
    elif opcao == 6:
        quantidadeUbsPorCidade()
    elif opcao == 0:
          break