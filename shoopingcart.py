##Welcome User##

from asyncio.proactor_events import _ProactorDuplexPipeTransport


userName = input("Por favor, digite seu nome:")
welcomeUser = f"Seja bem vinde a Loja Aya, {userName}"
lenWelcomeUser = len(welcomeUser)
print("#"*lenWelcomeUser)
print(welcomeUser)
print("#"*lenWelcomeUser)
##Market Place##

products= (
    {'id':1,'nome':'Creme corporal','preco':35.00},
    {'id':2,'nome':'Creme de cabelo','preco':29.38},
    {'id':3,'nome':'Perfume','preco':59.90},
    {'id':4,'nome':'Vestido','preco':75.00},
    {'id':5,'nome':'Tênis','preco':85.00}
)

cart =[]

def showProducts():
    for p in products:
        print(
            'Id: {0} - Nome: {1} - Preço: {2}\n'.format(p['id'], p['nome'], p['preco']))

def showOptions():
    print('\n\n')
    print('1 - Adicionar Item')
    print('2 - Remover Item')
    print('3 - Exibir itens e o valor total')
    print('4 - Limpar Carrinho de compras')
    print('5 - Sair')
    

option = '1'

print('***Marketplace*** \n')

def productName(id):
    for p in products:
        if p['id'] == id:
            return p['nome']

showProducts()
while option != '5':
    showOptions()
    option = input('Digite a opção: ')

    if option == '1':
        showProducts()
        id = int(input('Digite o identificador do produto: '))
        quantidade = int(input('Digite quantidade: '))
        cart.append({'id': id, 'quantidade': quantidade})

    if option == '2':
        id = int(input('Digite o id do produto que deseja remover: '))
        tempcart = []
        cart = [item]
        for item in cart:
            if item['id'] != id:
                tempcart.append(item)
        

    if option == '3':
        print('\n\n')
        somatorio = 0
        for item in cart:
            for p in products:
                if p['id'] == item['id']:
                    somatorio = somatorio + \
                        (p['preco'] * item['quantidade'])
                    break

            print(
                'Nome: {0} - Quantidade: {1}'.format(productName(item['id']), item['quantidade']))
        print('Preço total: {0}'.format(somatorio))

    if option == '4':
        cart = []