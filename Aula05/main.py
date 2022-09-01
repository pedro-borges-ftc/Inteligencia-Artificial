from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica
from cliente import Cliente

#Leia o nome, idade e CPF de uma pessoa 
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
cpf = input('Digite o seu cpf: ')

#Importação da classe Pessoa Física
pessoa_teste = PessoaFisica(cpf,nome,idade)
cliente_teste = Cliente(cpf,nome,idade,1)

#Mostre uma mensagem de boas-vindas de acordo com o valor digitado.
pessoa_teste.imprimePessoaFisica()
cliente_teste.setNome('Fulano')
cliente_teste.imprimePessoaFisica()