# # 15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
# # o valor da conta de energia entre os moradores da casa. No programa eles informam o
# # valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
# # quanto cada um deverá contribuir com a conta de energia.

valor_conta_energia = float(input("Informe o valor da conta de energia :" ))
qtd_moradores = int(input ("Informe a quantidade de moradores : "))
media_por_morador = (valor_conta_energia // qtd_moradores)

print ("Cada morador deve pagar " , media_por_morador , "reais")

