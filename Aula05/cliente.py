from pessoafisica import PessoaFisica

class Cliente(PessoaFisica):
    #Construtor da classe
    def __init__(self, cpf, nome, idade, codigo) -> None:
        super().__init__(cpf, nome, idade)
        self.codigo = codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo
