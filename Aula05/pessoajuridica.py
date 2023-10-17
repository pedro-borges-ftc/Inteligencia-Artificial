from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    #Construtor da classe
    def __init__(self, cnpj, nome, idade) -> None:
        super().__init__(nome,idade) #Chamada do construtor da classe Pessoa
        self.cnpj = cnpj

    def setCNPJ(self, cnpj):
        self.cnpj = cnpj

    def getCNPJ(self):
        return self.cnpj

    def imprimePessoaJuridica(self):
        print('Olá ' + self.nome + '. Seja bem vindo ao curso de Python.')
        print('---------------------------')
        self.imprime()
        print('CNPJ: ' + self.cnpj)