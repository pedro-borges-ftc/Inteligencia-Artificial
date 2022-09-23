# Criado por: prof. Pedro Borges
# pborges.ita@ftc.edu.br

from no import No
from arvore import Tree

arv = Tree()
print("Programa Arvore Binaria")
opcao = 999
while opcao != 0:
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 0: Sair do programa")
     print(" --- 1: Inserir")
     print(" --- 2: Excluir")
     print(" --- 3: Pesquisar")
     print(" --- 4: Imprimir")
     print(" --- 5: Somar")
     print(" --- 6: Média")
     print("***********************************")
     opcao = int(input("-> "))
     if opcao == 1:
          x = int(input(" Informe o valor -> "))
          arv.inserir(x)
     elif opcao == 2:
          x = int(input(" Informe o valor -> "))
          if arv.remover(x) == False:
               print(" Valor nao encontrado!")
     elif opcao == 3:
          x = int(input(" Informe o valor -> "))
          if arv.buscar(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")	 
     elif opcao == 4:
          arv.imprimir()
     elif opcao == 5:
          print(" A soma dos elementos da ABB é: %d" %(arv.somarNos(arv.root)))
     elif opcao == 6:
          print(arv.media())
     elif opcao == 0:
          break