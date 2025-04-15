# Implementação Perceptron
from math import e
import sys 
import random

class Perceptron: 
## Primeira função de uma classe (método construtor de objetos) 
## self é um parâmetro obrigatório que receberá a instância criada 
    def __init__(self, amostras, saidas, taxa_aprendizado = 0.01, epocas = 10000, limiar = 1) -> None:
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)         #número de linhas (amostras)
        self.n_atributos = len(amostras[0])     #número de atributos
        self.pesos = []     #[0.7599999999999998, 0.3536072912712085, 0.28763390535841715]

    ## Atribuição de treinamento para amostras e construção da matriz
    def treinar(self):     

        # Gerar valores randômicos entre 0 e 1 (pesos) conforme o número de atributos
        if(len(self.pesos) == 0):
             # # Inserir o valor do limiar na posição "0" para cada amostra da lista “amostra” Ex.: [[0.72, 0.82], ...] vira [[1, 0.72, 0.82]
            for amostra in self.amostras:
                amostra.insert(0,self.limiar)
            
            for i in range(self.n_atributos):
                self.pesos.append(random.random())
            # Inserir o valor do limiar na posição "0" do vetor de pesos 
            self.pesos.insert(0,self.limiar)

        print(self.amostras)
        print(self.pesos)
        
        # Inicializar contador de épocas
        n_epocas = 0
        erro_aux = [0,0,0,0,0,0]

        while True:
            # Inicializar variável erro
            erro = 0
            # (quando terminar loop e erro continuar False, é porque não tem mais diferença entre valor calculado e desejado
            
            # Para cada amostra... 
            for i in range(self.n_amostras):
                
                #self.amostras[i][0] = self.limiar

                # Inicializar potencial de ativação
                u = 0
                # Para cada atributo...
                for j in range(self.n_atributos + 1):
                    # Multiplicar amostra e seu peso e também somar com o potencial
                    u += self.pesos[j] * self.amostras[i][j]
                # Obter a saída da rede considerando g a função sinal
                y = self.sinal(u)
                
                if(y >= 0):
                    print('Laranja y: ' + str(y) + ' saída: ' + str(self.saidas[i]))
                elif(y <= 0):
                    print('Maçã y: ' + str(y) + ' saída: ' + str(self.saidas[i]))

                # Verificar se a saída da rede é diferente da saída desejada 
                if y != self.saidas[i]:
                    # Calcular o erro
                    erro_aux[i] = self.saidas[i] - y
                    # Fazer o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = self.pesos[j] + (self.taxa_aprendizado * erro_aux[i])
                    # Atualizar variável erro, já que erro é diferente de zero (e 
                    erro += 1

            # Atualizar contador de épocas
            n_epocas += 1

            print('')
            print('Época: %d' % n_epocas)
            #print(self.amostras)
            print('Pesos: ' + str(self.pesos))
            print('Erros: ' + str(erro_aux))
            
            # Critérios de parada do loop: erro inexistente ou o número de épocas 
            if erro == 0 or n_epocas > self.epocas:
                break

    ## Testes para "novas" amostras
    def teste(self, amostra):
        # Inserir o valor do limiar na posição "0" para cada amostra da lista “amostra”
        amostra.insert(0,self.limiar)
        print(amostra)
        print(self.pesos)
        # Inicializar potencial de ativação 
        u = 0
        # Para cada atributo...
        for i in range(self.n_atributos + 1):
            # Multiplicar amostra e seu peso e também somar com o potencial que já tinha
            u += self.pesos[i] * amostra[i]
        # Obter a saída da rede considerando g a função sinal
        y = self.sinal(u)
        print('Classe: ' + str(y) + ' u: ' + str(u))

    ## Função sinal
    def sinal(self,valor):
        if valor >= 0.0:
            return 1
        else:
            return -1   
        
# Fim do perceptron