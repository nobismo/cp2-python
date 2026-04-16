import math

A = int(input("Digite o valor do lado A do triangulo:"))
B = int(input("Digite o valor do lado B do triangulo:"))
C = int(input("Digite o valor do lado C do triangulo:"))

if A>= B + C:
    print("NÃO FORMA TRIANGULO")

else:

    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBSTUSANGULO")
    if  A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")


    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A==B and A!=C or C==B and C!=A or A==C and A!=B:
        print("TRIANGULO ISOSCELES")