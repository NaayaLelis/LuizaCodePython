# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em
# variáveis diferentes.
# a. Calcule a área de um quadrado cujo lado seja 2 cm.
from re import I


def quadrado(x):
    return x*x
area= quadrado(2)

print(area)

# b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar
# por ela.
x=120
y = (x/100)*5
precofinal = x - y

print(precofinal)
 
# c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem
# será 200 Km. Quantas horas irá demorar a viagem.
velocidademedia=100
trechodaviagem = 200
tempodeviagem = trechodaviagem//velocidademedia

print("O tempo de viagem será de" , tempodeviagem , "horas.")

# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
# sua média.

jp=2
mp=3
sp=1

total = jp+mp+sp
media = total//3
print("O total de pirulitos é: ", total)
print("A média de pirulitos é: ", media)



# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
# verificação se a idade de Davi é maior que a idade de sua irmã. 
d =13
irm = 7

if d > irm :
 
 print(" Davi é mais velho")