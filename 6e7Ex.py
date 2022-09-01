# 6) Qual será o valor de z? Qual seria outra forma de escrever este trecho de código?

#  z = 3
#  z += 2 (5)
#  z *= 6 (18)
#  z /= 5 (0,6)
 
#  7) Considere as seguintes variáveis:
# ovo = 3.4
# caju = 12.4
# Qual será o valor de resposta em cada linha:

# resposta = ovo if 1 > 2 else caju 


if (1 > 2):
    print("ovo")

else :
    print("caju")

# resposta = ovo if ovo > caju else caju
ovo = 3.4
caju= 12.4

if (ovo > caju):
    print("ovo")

else :
    print("caju")
    
# resposta = ovo if ovo < caju else caju

ovo = 3.4
caju= 12.4

if (ovo < caju):
    print("ovo")

else :
    print("caju")

# resposta = 100 if ovo + caju > 15 else 200
ovo = 3.4
caju= 12.4

if (ovo + caju >15 ):
    print("100")

else :
    print("200")

# resposta = 100 if ovo == 3 else 0

ovo = 3.4
caju= 12.4

if (ovo == 3 ):
    print("100")

else :
    print("0")

