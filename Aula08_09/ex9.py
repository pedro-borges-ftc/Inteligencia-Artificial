#Escreva um algoritmo em Python que utiliza uma função que recebe um array 
# com múltiplos números inteiros e retorna o valor da soma dos elementos desse array. 
# Peça ao usuário para digitar os valores a serem inseridos no array.

def somaArray(a):
    soma = 0.0
    for i in range(0,10):
        soma += a[i]
    return soma

numeros = [] #[30.0, 35.0, 45.0, 25.0, 12.0, 15.0, 16.0, 17.0, 23.0, 28.0, 45.0, 65.0]

for i in range(0, 10):
    print(f'Digite um número {i + 1}:')
    numeros.append(float(input('')))

print(f'A soma dos elementos do Array é {somaArray(numeros)}:')