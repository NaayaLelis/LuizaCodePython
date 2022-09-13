##Welcome User##

from asyncio.proactor_events import _ProactorDuplexPipeTransport


userName = input("Por favor, digite seu nome:")
welcomeUser = f"Seja bem vinde a Loja Aya, {userName}"
lenWelcomeUser = len(welcomeUser)
print("#"*lenWelcomeUser)
print(welcomeUser)
print("#"*lenWelcomeUser)
##Market Place##

print("\n*****Marketplace*****")
products= (
    {'id':1,'nome':'Creme corporal','preco':35.00},
    {'id':2,'nome':'Creme de cabelo','preco':29.38},
    {'id':3,'nome':'Perfume','preco':59.90},
    {'id':4,'nome':'Vestido','preco':75.00},
    {'id':5,'nome':'Tênis','preco':85.00}
)

cart =[]

def marketplace():
    for p in products:
        print(
            ('Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'],p['nome'],p['preco']))
        )
         
marketplace()

toShop= 'sim'

toShop=input("Gostaria de prosseguir para realizar uma compra?(sim/não)")

if toShop == 'não':
    print('Esperamos que retorne em breve!Até a próxima.')  

    
if toShop == 'sim':
       
 def main_menu():
  print(''''
    1. Adicionar produto ao carrinho
    2.Remover produto do carrinho
    3. Ver todos os itens do carrinho e o valor total
    4.Buscar item pelo id
    5.Sair
     ''') 
main_menu()


## Options##

option ='1'

def productName(id):
 for p in products:
  if p['id'] == id:
     return p['nome']

while option !='5':
    main_menu()
    option = int(input('Digite uma opção:'))
      
if option == 1:
   def marketplace():
      for p in products:
          print(
            ('Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'],p['nome'],p['preco']))
        )       
marketplace()
id = int(input('Digite o identificador do produto: '))
quantidade = int(input('Digite a quantidade: '))
cart.append({'id': id, 'quantidade' : quantidade})   

if  option == '2':
    id = int(input('Digite o id do produto que deseja remover: '))
    temporarycart = []
    for item in cart:
        if item ['id'] != id:
            temporarycart.append(item)
            
if option =='3':
    for item in cart:
        somatorio = 0
        for p in products:
            if products['id'] == item['id']:
               somatorio= somatorio + (products['preco'] * item['quantidade'])
            break
           
        print('Nome : {0} - Quantidade {1}'.format(item['id'], item['quantidade']))
        print('Preço total: {0}'.format(somatorio))
        
        if option == '4':
            input=('Tem certeza que deseja esvaziar seu carrinho?')
            if input =='sim':
                
             cart=[]
            else:
                main_menu()
            
    


 


 
 
          


