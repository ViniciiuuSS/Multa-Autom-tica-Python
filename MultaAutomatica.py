from time import sleep
from random import randint
print("-=-" * 30)
rad = "RADAR"
print(rad.center(80))
print("-=-" * 30)
carro = randint(81, 90)
print("Processando valocidade...")
sleep(2)
if (carro > 80 ):
    km = (carro-80) * 7     
    print("Voce ultrapassou o limite de velocidade! MULTADO! = Sua multa é de R${}  \nVelocidade = {}KM/H".format(km,carro))
else:
    print("Limite permitido! = {}KM/H".format(carro))
