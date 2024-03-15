from pessoa import Pessoa

class PessoaFisica(Pessoa):
    #Construtor da classe
    def __init__(self, cpf, nome, idade) -> None:
        super().__init__(nome,idade) #Chamada do construtor da classe Pessoa
        self.cpf = cpf

    def setCPF(self, cpf):
        self.cpf = cpf

    def getCPF(self):
        return self.cpf

    def imprimePessoaFisica(self):
        print('Olá ' + self.nome + '. Seja bem vindo ao curso de Python.')
        print('---------------------------')
        self.imprimeJunto()
        print('CPF: ' + self.cpf)