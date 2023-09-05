class Pessoa:
    #Construtor da classe Pessoa
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade
    
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    
    def imprime(self):
        print('Nome: ' + self.nome)
        print('Idade: ' + str(self.idade))