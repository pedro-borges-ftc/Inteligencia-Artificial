# Implementação Perceptron
from math import e
import sys 
import random

class Perceptron: 
## Primeira função de uma classe (método construtor de objetos) 
## self é um parâmetro obrigatório que receberá a instância criada 
    def __init__(self, amostras, saidas, taxa_aprendizado = 0.1, epocas = 1000, limiar = 1) -> None:
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)   #número de linas (amostras)
        self.n_atributos = len(amostras[0])     #número de atributos
        self.pesos = []

    ## Atribuição de treinamento para amostras e construção da matriz
    def treinar(self):
        # # Inserir o valor do limiar na posição "0" para cada amostra da lista “amostra” Ex.: [[0.72, 0.82], ...] vira [[1, 0.72, 0.82]
        for amostra in self.amostras:
            amostra.insert(0,self.limiar)

        # Gerar valores randômicos entre 0 e 1 (pesos) conforme o número de atributos
        for i in range(self.n_atributos):
            self.pesos.append(random.random())
        # Inserir o valor do limiar na posição "0" do vetor de pesos 
            self.pesos.insert(0,self.limiar)

        # Inicializar contador de épocas
        n_epocas = 0

        while True:
            # Inicializar variável erro 
            # (quando terminar loop e erro continuar False, é porque não tem mais diferença entre valor calculado e desejado 
            erro = False

            # Para cada amostra... 
            for i in range(self.n_amostras):
                # Inicializar potencial de ativação
                u = 0
                # Para cada atributo...
                for j in range(self.n_atributos + 1):
                    # Multiplicar amostra e seu peso e também somar com o potencial
                    u += self.pesos[j] * self.amostras[i][j]
                    # Obter a saída da rede considerando g a função sinal
                    y = self.sinal(u)

                # Verificar se a saída da rede é diferente da saída desejada 
                if y != self.saidas[i]:
                    # Calcular o erro
                    erro_aux = self.saidas[i] - y
                    # Fazer o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.n_atributos + self.limiar):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux
                    # Atualizar variável erro, já que erro é diferente de zero (e 
                    erro = True

            # Atualizar contador de épocas
            n_epocas += 1
            
            # Critérios de parada do loop: erro inexistente ou o número de épocas 
            if not erro or n_epocas >= self.epocas:
                break

    ## Testes para "novas" amostras
    def teste(self, amostra):
        # Inserir o valor do limiar na posição "0" para cada amostra da lista “amostra”
        amostra.insert(0,self.limiar)
        # Inicializar potencial de ativação 
        u = 0
        # Para cada atributo...
        for i in range(self.n_atributos + self.limiar):
            # Multiplicar amostra e seu peso e também somar com o potencial que já tinha
            u += self.pesos[i] * amostra[i]
            # Obter a saída da rede considerando g a função sinal
            y = self.sinal(u)
        print('Classe: %d' % y)

    ## Função sinal
    def sinal(self,valor):
        if valor >= 0:
            return 1
        else:
            return -1
# Fim do perceptron