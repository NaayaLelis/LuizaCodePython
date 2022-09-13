# from operator import add


#id_user = input("Insira o id do usuário: ")
# id_produto = input ("Insira o id do produto: ")
# price_produto = float (input("Insira o preço do produto: "))
# quantity_product =int (input("Insira a quantidade de produto: "))

from tkinter import N


produtos = (
    {'id':1 , 'Nome' : 'Perfume', 'preco' :115.00 },
    {'id':2 , 'Nome' : 'Creme de pentear','preco' :30.00 },
    {'id':3, 'Nome' : 'Vestido', 'preco' :59.00 },
    {'id':4 , 'Nome' : ' Tênis', 'preco' :95.00 },
)

cart =[]

def main_menu():
    print(''''
    1. Ver produtos
    2. Adicionar produto ao carrinho
    3.Remover produto do carrinho
    4. Ver todos os itens do carrinho
    5.Buscar item pelo id
    6.Sair
     ''')
    
main_menu()

def show_all_products():
  for p in produtos:
        print(
            'Id: {0} - Nome: {1} - Preço:{2}\n'.format(p['id'],p['nome'],p['preco']))

opcao = input ("Digite a opção desejada : ")    
if opcao == '1' :
       show_all_products()  
       print(id =int(input("Digite o id do produto desejado: ")) ) 
               
       

   



    

    
   
