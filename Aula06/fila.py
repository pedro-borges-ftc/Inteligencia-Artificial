from collections import deque

# Cria uma fila com três elementos.
fila = deque(["Banana", "Maçã", "Pera"])
print("Fila: ", fila)

# Adiciona um elemento ao final da fila.
fila.append("Uva")
print("Adicionando um elemento: ", fila)

# Remove o primeiro elemento adicionado à fila.
fila.popleft()
print("Removendo um elemento: ", fila)