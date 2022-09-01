# from operator import add


#id_user = input("Insira o id do usuário: ")
# id_produto = input ("Insira o id do produto: ")
# price_produto = float (input("Insira o preço do produto: "))
# quantity_product =int (input("Insira a quantidade de produto: "))

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
    
opcao = input ("Digite a opção desejada : ")
    
def show_all_products():
    for p in produtos:
        print(
            produtos
        )    
    if opcao == '1' :
        print(produtos )             
    show_all_products()    
  
   



    

    
   
