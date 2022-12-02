from random import randint, uniform # importa n aleatorios (int e float)
import re # modulo para trabalhar com expressões regulares
def gera_lancamentos():
 
    lancamentos = []
 
# gera um vetor com 100 valores (0 - 99), gerando valor
 
# aleatório entre 1 e 6 e inserindo como string no vetor
 
# para que a funcao 're' possa ser utilizada.
 
    for i in range(0, 100): 
 
        random = (randint(1, 6))
 
        lancamentos.append(str(random))
 
    return lancamentos