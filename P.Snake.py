import os

from prettytable import PrettyTable
clear = lambda: os.system('cls')


#Declaração da variável de sessão
modo = True
#Declaração de Registros
class Funcionario:
    def __init__(self, name, password,afirma):
     self.name = name
     self.password = password
     self.afirma = afirma
funcionarios = []

class Cliente:
    def __init__(self, name, cpf, divid):
     self.name = name
     self.divid = divid
     self.cpf = cpf
    
clientes = []


class Produto:
    def __init__(self, name, preco, estoque,custo):
     self.name = name
     self.preco = preco
     self.estoque = estoque
     self.custo = custo

produtos = []
lucro_bruto =0
gastos=0
dividas=0


#Declaração de Funções
def VerificNumber(x,y):
     if(y>0):
        while(x>y or x<=0):
            x =  int(input("Opção Inválida, tente novamente: "))
     else:
       while(x<0):
            x =  int(input("Opção Inválida, tente novamente: "))

     return x

def Afirmacao(x):
    while(x!="S" and x!="N" and x!="s" and x!="n"):
       x =  input("Opção Inválida Tente novamente: ") 
    return x

def Registro_Cliente():
    name = input("Digite o nome do cliente: ")



    cpf = input("Digite o CPF do cliente:")
    while(len(cpf)!=14):
        cpf = input("CPF inválido ou preenchido incorretamente, tente novamente: ")

    clientes.append(Cliente(name,cpf,0))
    
def Tabela_clientes():
 myTable_ = PrettyTable(["ID","NOME"," CPF","DÍVIDAS"]) 
                
 for i in range(len(clientes)):
    myTable_.add_row([i+1,clientes[i].name,clientes[i].cpf,f"R${clientes[i].divid}"])
                
 print(myTable_)

def Tabela_Produtos():
 myTable_ = PrettyTable(["ID","DESCRIÇÃO","PREÇO","ESTOQUE"]) 
                
 for i in range(len(produtos)):
    myTable_.add_row([i+1,produtos[i].name,f"R${produtos[i].preco}",produtos[i].estoque])

                
 print(myTable_)

def Tabela_Registro_Produtos():
    myTable_ = PrettyTable(["ID","DESCRIÇÃO","PREÇO","CUSTO","ESTOQUE"]) 
                
    for i in range(len(produtos)):
        myTable_.add_row([i+1,produtos[i].name,f"R${produtos[i].preco}",produtos[i].custo,produtos[i].estoque])

                
    print(myTable_)
compras=0



   
#Interface

while(modo == True):
    #Menu de login
     clear()
     print("=========================================")
     print("|       BEM VINDO AO P.SNAKE            |")
     print("=========================================")
     print("| 1 - Entrar como funcionário           |")
     print("| 2 - Registrar funcionário             |")
     print("| 3 - Encerrar                          |")
     print("=========================================\n")
     
     login = int(input("Escolha: "))
     login = VerificNumber(login,3)
     #Caso deseje entrar com um funcionário já registrado
     if(login==1):
        print("\n------------------------------------------------------------")
        if(len(funcionarios)==0):
           print("Nenhum funcionário registrado, o login não é possível :(")
           print("-------")
           escolha = input("T e c l e   E n t e r   p a r a   c o n t i n u a r ")

        else:
          id_funcionario = int(input("ID: "))
          id_funcionario = VerificNumber(id_funcionario,len(funcionarios))
          name = input("Usuário: ")
          password = input("Senha: ")

          while(name != funcionarios[id_funcionario-1].name or password != funcionarios[id_funcionario-1].password):
             print("\n Dados incorretos, tente novamente")
             id_funcionario = int(input("ID: "))
             id_funcionario = VerificNumber(id_funcionario,len(funcionarios))
             name = input("Usuário: ")
             password = input("Senha: ")

          clear()
          logado=True
          while(logado==True):
            #Menu de operações
             clear()
             print("=============================================")
             print("| P.Snake - 2023                            |")
             print("+-------------------------------------------+")
             print("| 1 - Listagem de Clientes                  |")
             print("| 2 - Registrar Compras                     |")
             if(funcionarios[id_funcionario-1].afirma == "S" or funcionarios[id_funcionario-1].afirma == "s"):
              print("| 3 - Listagem de Produtos                  |")
              print("| 4 - Resumo de Caixa                       |")
              print("| 5 - Sair                                  |")
             else:
              print("| 3 - Sair                                  |")
            
             print("=============================================")
             escolha=int(input(f"Escolha uma opção, {name}: "))
             if(funcionarios[id_funcionario-1].afirma == "S" or funcionarios[id_funcionario-1].afirma == "s"):
                escolha = VerificNumber(escolha,5)
             else:
                escolha = VerificNumber(escolha,3)
            #Caso deseje consultar a lista de clientes registrados
             if(escolha==1):
                loop=True
                while(loop==True):
                    clear()
                    if(len(clientes)==0): 
                        
                        print("==================================================================")    
                        print("| NENHUM CLIENTE REGISTRADO NO SISTEMA                           |")
                        print("==================================================================")
                    else:
                     Tabela_clientes()
                     print("\n==================================================================")
                    
                    print("1 - Adicionar Cliente")
                    print("2 - Remover Cliente")
                    print("3 - Retornar")
                    print("----------------")
                    tecle = int(input("Tecle: "))
                    tecle = VerificNumber(tecle,3)
                    #Caso queira adicionar um novo cliente
                    if(tecle==1):
                     Registro_Cliente()
                    #Caso queira remover um cliente da listagem
                    elif(tecle==2):
                        if(len(clientes)==0):
                            print("Nenhum cliente pode ser remvido, pois não se possui nenhum cliente")
                            print("==========")
                            resp = input("T e c l e   E n t e r   p a r a   c o n t i n u a r ")
                        else:
                         id_remove = int(input("Digite o ID do cliente que deseja remover: "))
                         id_remove = VerificNumber(id_remove,len(clientes))
                         clientes.pop(id_remove-1)
                    #Caso queira retornar ao menu
                    else:
                        loop=False    
                        
                    
                

               
            #Caso deseje realizar a venda de algum produto
             elif(escolha==2):
               
               clear()
               if(len(produtos)==0):
                 print("==============================================")
                 print("|          Nenhum produto registrado         |")
                 print("==============================================")
               else:
                 Tabela_Produtos()

               print("\n--------")
               if(len(produtos)==0):
                 print("1 - Cancelar")
               else:
                 print("1 - Adicionar item a compra")
                 print("2 - Cancelar")
                 print("--------")

               tecle = int(input("Escolha: "))

               if(len(produtos)==0):
                  VerificNumber(tecle,1)
               else:
                  VerificNumber(tecle,2)  
                  if(tecle==1):
                    adendo = True
                    lista = []
                    soma = 0
                    while(adendo==True):
                     id_produto = int(input("Digite o ID do produto: "))
                     id_produto = VerificNumber(id_produto,len(produtos))
                     quantidade = int(input("Quantas unidades do produto serão compradas?: "))
                     quantidade = VerificNumber(quantidade,produtos[id_produto-1].estoque)
                     quantidade,produtos[id_produto-1].estoque-quantidade
                     lista.append(f"-{produtos[id_produto-1].name} X{quantidade} -> R${quantidade*produtos[id_produto-1].preco}")
                     soma+= float(quantidade*produtos[id_produto-1].preco)
                     gastos+=float(quantidade*produtos[id_produto-1].custo)

                     print("-------------")
                     print("Produto Adicionado!")
                     adendo = input("Deseja adicionar mais algum produto? S/N: ")
                     adendo = Afirmacao(adendo)
                     
                     if(adendo == "S" or adendo=="s"):
                        adendo=True
                        clear()
                        Tabela_Produtos()
                     else:
                        adendo= False
                    #Método de pagamento
                    if(len(clientes)>0):
                         Tabela_clientes()
                    else:
                      print("NENHUM CLIENTE REGISTRADO")
               #Menu de venda
                    print("=========================================")
                    print("| 1 - Realizar compra local             |")
                    print("| 2 - Adicionar cliente para compra     |")
                    if(len(clientes)>0):
                     print("| 3 - Inserir ID de cliente            |")
                     print("| 4 - Retonar                          |")
                    else:
                     print("| 3 - Retornar                          |")

                    print("=========================================")
                    tecle = int(input("Escolha: "))
                    if(len(clientes)>0):
                     tecle = VerificNumber(tecle,4)
                    else:
                     tecle = VerificNumber(tecle,3)

                    if(tecle==1):
                      comprador = Cliente("Local","XXX",0)

               
                    elif(tecle==2):
                       Registro_Cliente()
                       comprador = clientes[len(clientes)-1]
                 
                    if(len(clientes)>0):
                     if(tecle==3):
                       print("--------")
                       id_comprador = int(input("Digite o ID do cliente: "))
                       id_comprador = VerificNumber(id_comprador,len(clientes))
                       comprador = clientes[id_comprador-1]

                    clear()
                    print("====================================")
                    for i in lista:
                        print(i)
                    print(f"Totoal: R${soma}")
                    print("------------------------------------")
                    print("|1 - Realizar pagamento á vista    |")
                    print("|2 - Realizar pagamento em cartão  |")
                    print("====================================")
                    tecle = int(input("Escolha: "))
                    tecle = VerificNumber(tecle,2)
                    print("\n------------")
                    if(tecle==1):
                        dinheiro_fornecido=float(input("Dinheiro recebido: "))
                        if(dinheiro_fornecido>=soma):
                            print("A compra foi realizada com sucesso")
                            print(f"Troco: R${dinheiro_fornecido-soma}")
                            lucro_bruto+=dinheiro_fornecido
                        else:
                            print("O cliente está em dívida")
                            print(f"Dívida: R${soma-dinheiro_fornecido}")
                            comprador.divid+=soma-dinheiro_fornecido
                            dividas+=soma-dinheiro_fornecido
                    else:
                        print("Pagamento realizado com sucesso!")
                        print("Taxa aplicada: 0.10%")
                        lucro_bruto+=soma*0.001

                    compras+=1
                    escolha = input("\nT e c l e   E n t e r   p a r a   c o n t i n u a r ")
            
                
               
            #Verificação de "adm", pois caso o funcionário não tenha adm em seu registro, ele não terá ceertas opções do menu
             if(funcionarios[id_funcionario-1].afirma == "S" or funcionarios[id_funcionario-1].afirma == "s"):
                  #Caso queira consultar ou registrar produtos no sistema
                  if(escolha==3):
                   loop=True
                   while(loop==True):
                    clear()
                    if(len(produtos)==0):
                        print("=========================================")
                        print("|     NENHUM PRODUTO FOI REGISTRADO     |")
                        print("=========================================")
                    else:
                        Tabela_Registro_Produtos()
                    print("\n-----------")
                    print("1 - Adicionar Produto")
                    print("2 - Remover Produto")
                    print("3 - Sair")
                    print("-----------")
                    tecle = int(input("Escolha: "))
                    tecle=VerificNumber(tecle,3)
                    clear()
                    #Caso queira adicionar um produto a listagem
                    if(tecle==1):
                            print("-----------")
                            descricao = input("Digite a descrição do produto: ")
                            custo = float(input("Digite o custo unitário do produto: "))
                            preco = float(input("Digite o preço unitário para o produto: "))
                            estoque = int(input("Digite a quantidade de unidades disponíveis: "))
                            estoque = VerificNumber(estoque,0)
                            produtos.append(Produto(descricao,preco,estoque,custo))
                            print("====================================")
                            print("|    PRODUTO ADICIONADO A LISTA    |")
                            print("====================================")
                            print("\n----------")
                            escolha = input("T e c l e   E n t e r   p a r a   c o n t i n u a r ")
                    #Caso queira remover um produto da listagem
                    elif(tecle==2):
                        if(len(produtos)==0):
                            print("Nenhum item pode ser removido, pois a lista não possui nenhum produto")
                            print("==========")
                            escolha = input("T e c l e   E n t e r   p a r a   c o n t i n u a r ")
                        else:
                            Tabela_Registro_Produtos()
                            print("\n----------")
                            id_remove = int(input("Digite o ID do produto que deseja remover: "))
                            id_remove = VerificNumber(id_remove,len(produtos))
                            produtos.pop(id_remove-1)
                    #Caso queira retornar ao menu principal
                    else:
                        loop=False
                        

                  #Caso queira verificar o Fluxo de caixa feito no sistema
                  elif(escolha==4):
                    clear()
                    print("=========================================")
                    if(compras>0):
                        Resun = PrettyTable(["SETORES","VALORES"])
                        Resun.add_row({"Lucro Bruto",f"R${lucro_bruto}"})
                        Resun.add_row({"Custos",f"R${custo}"})
                        Resun.add_row({"Dívidas",f"R${dividas}"})
                        Resun.add_row({"TOTAL",f"R${lucro_bruto-(custo+dividas)}"})
                        print(Resun)
                    else:
                        print("O Caixa está vazio no momento, pois nenhuma compra foi feita")
                    print("\n-----------")
                    escolha = input("T e c l e   E n t e r   p a r a   c o n t i n u a r ")
                 #Caso deseje retornar a tela de login
                  elif(escolha==5):
                     logado=False
             else:
                if(escolha==3):
                    logado=False
            
          

       

          

     #Caso deseje registrar um funcionário
     elif(login==2):
          print("------------------------------------------------------------")
          name = input("Nome do funcionário: ")
          password = input("Nova Senha: ")
          adm = input("É adm? S/N: ")
          adm = Afirmacao(adm)
          funcionarios.append(Funcionario(name,password,adm))
          print("===================")
          print(f"O ID do funcionário é: {len(funcionarios)}")
          print("===================")
          escolha = input("T e c l e   E n t e r   p a r a   c o n t i n u a r ")

     #Caso deseje encerrar a sessão
     else:
         modo=False

         




