import getpass
from os import system
from sqlite3 import Time
import time


class Info ():
    def _init_(self, nome , idade,altura) -> None:

        self.nome = nome
        self.idade = idade
        self.altura = altura
   
    
    def setNome(self,nome):
        
        self.nome= nome
        return self.nome 
        
    def setIdade(self,idade):

        self.idade= idade
        return self.idade

    def setAltura (self,altura):

        self.altura=altura
        return altura

    

class PessoaFisica(Info):

            def _init_(self,cpf,nome,idade,altura) -> None:
                super()._init_(nome,idade,altura)
                self.cpf =cpf
                


            def setCPF (self,cpf):
                self.cpf= cpf
                return self.cpf           
                    
     

class PessoaJuridica(Info):

            def _init_(self,cnpj,nome,idade,altura) -> None:
                super()._init_(nome,idade,altura)
                self.cnpj = cnpj


            def setCNPJ (self,cnpj):
                self.cnpj= cnpj
                return self.cnpj


def menu():

    try:
        print('''\n                                                     Olá  
                                        Por favor , selecione a opção desejada

                                                __________
                                                    Pessoa fisia click    - [1]
                                                    Pessoa Juridica click - [2]
                                                __________

                                                                                                                    ''')
        op = int(input('Digite opção :'))
        system('cls')
                        

        if op == 1 :            
                                print('                   Pessaoa Fisica')
                                nome = input('\n\nDigite seu nome :')     
                                idade = int(input('Digite sua idade :'))
                                cpf = int(getpass.getpass('Digite seu CPF :'))
                                altura = float(input('digite sua altura :'))

                                pessoa_1 = PessoaFisica(cpf,nome,idade,altura)
                                system('cls')
                                print('Olá' , pessoa_1.nome , 'Seja bem vindo ao futuro')

                                op0 = input('\n\n                         deseja exibir seus dados na tela ? sim[s] x não [n]\n\n:')


                                if op0 == 's' :
                                    system('cls')
                                    print('                           Seus dados')
                                    print('\n\nNome -',pessoa_1.nome,'\nidade -',pessoa_1.idade,'\naltura -',pessoa_1.altura,'\nCPF -',pessoa_1.cpf, '\n\n')




        elif op == 2 :
                                print('                   Pessaoa Juridica')
                                nome = input('\n\nDigite seu nome :')     
                                idade = int(input('Digite sua idade :'))
                                cnpj = int(getpass.getpass('Digite seu CNPJ :'))
                                empresa = input('nome da empresa :')

                                pessoa_1 = PessoaJuridica(cnpj,nome,idade,empresa)
                                system('cls')
                                print('\n\n\n                    Olá' , pessoa_1.nome , 'Seja bem vindo ao futuro')
                                                                                                                


                                op2 = input('\n\ndeseja exibir seus dados na tela ? sim[s] x não [n]\n\n :')
                                

                                if op2 == 's' :
                                    system('cls')
                                    print('                           Seus dados')
                                    print('\nNome - ',pessoa_1.nome,'\nidade - ',pessoa_1.idade,'\nCNPJ -',pessoa_1.cnpj,'\nEmpresa - ',empresa,'\n\n\n')

        else:
            print('opção incorreta')
            return menu()
    except ValueError :
        print('opção invalida')
        time.sleep(2)
        
        system('cls')
        return menu()

menu()