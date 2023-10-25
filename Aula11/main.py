from perceptron import Perceptron

## Função de leitura das amostras no arquivo txt
def leituraAmostras():
        # Leitura do arquivo de dados de amostras
    ref_arq_amostras = open("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula11/amostras.txt","r")
    amostras = []
    for linha in ref_arq_amostras:
        amostra = []
        valores = linha.split()
        amostra.insert(0,float(valores[0]))
        amostra.insert(1,float(valores[1]))
        amostras.append(amostra)
    ref_arq_amostras.close()
    print('Amostras: ')
    print(amostras)
    return amostras

## Função de leitura das saídas no arquivo txt
def leituraSaidas():
    # Leitura do arquivo de saídas
    ref_arq_saidas = open("/Users/viniciussouza/Documents/Inteligencia-Artificial/Aula11/saidas.txt","r")
    saidas = []
    for linha in ref_arq_saidas:
        valores = linha.split()
        saidas.append(float(valores[0]))
    ref_arq_saidas.close()
    print('Saídas: ')
    print(saidas)
    return saidas

print("Início do Programa Perceptron")
amostras = []
saidas = []
opcao = 999

while opcao != 0:
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 0: Sair do programa")
     print(" --- 1: Ler os arquivos de dados")
     print(" --- 2: Treinar")
     print(" --- 3: Testar")
     print(" --- 4: Ler e treinar")
     print("***********************************")
     opcao = int(input("-> "))

     if opcao == 1:
        amostras = leituraAmostras()
        saidas = leituraSaidas()

        # Chamar classe e fazer input das amostras e saídas
        rede = Perceptron(amostras, saidas)

     elif opcao == 2:
        # Treinando a rede com 100 épocas
        rede.treinar()

     elif opcao == 3:
        # Entrando com amostra para teste
        x = float(input(" Informe o valor 1 da amostra -> "))
        y = float(input(" Informe o valor 2 da amostra -> "))
        rede.teste([x, y])

     elif opcao == 4:
        amostras = leituraAmostras()
        saidas = leituraSaidas()

        # Chamar classe e fazer input das amostras e saídas
        rede = Perceptron(amostras, saidas)
        rede.treinar()

     elif opcao == 0:
          break