# 3) Determine qual é o resultado dos seguintes cálculos no Python:
# a. Operadores matemáticos
# i. 10 + 3 (13)
# ii. 10 - 3 (7)
# iii. 10 * 3 (30)

# iv. 10 / 3 (3.3333333333333335)
def divisao (x, y):
     return x/y
divide = divisao (10, 3)

print (divide) 

# v. 10 / 3.0 (3.3333333333333335)
def divisao (x, y):
     return x/y
divide = divisao (10, 3.0)

print (divide) 

# vi. 13 / 3 (4.333333333333333 )

def divisao (x, y):
     return x/y
divide = divisao (13 , 3)

print (divide) 


# vii. 13 / 3.0 (4.333333333333333 )
def divisao (x, y):
     return x/y
divide = divisao (13 , 3.0)

print (divide) 


# viii. 13 // 3.0 (4)
def divisao (x, y):
    return x//y
divide = divisao (13 , 3)

print (divide) 

# b. Ordem dos operadores
# i. 5 + 30 * 20 (605)

def operacao (x, y , z):
    return x+y*z
op = operacao (5, 30, 20)

print (op) 

# ii. (5 + 30) * 20 (700)

def operacao (x, y , z):
    return (x+y)*z
op = operacao (5, 30, 20)

print (op) 


# iii. ((5 + 30) * 20) / 10 (70)

def operacao (x, y , z):
    return ((x+y)*z)/10
op = operacao (5, 30, 20)

print (op) 

# iv. 5 + 30 * 20 / 10 (65)
# #explicação : 20/10 é igual a 2; então
# 30x2 = 60 , + 5 = 65.

def operacao (x, y , z, w):
    return x+y*z /w
op = operacao (5, 30, 20 , 10)

print (op) 


# 4) Qual será o valor final de x?(80)
x = 10
x = x + 10
x = 100 - x

print(x)




