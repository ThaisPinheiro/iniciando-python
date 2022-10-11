
dias = int(input("Aluguel de Carros \n\nInsira quantos dias o carro foi alugado: "))
km = float(input("Insira quantos kilometros foi percorrido: "))
valor = (dias * 60) + (km * 0.15)

print('O valor total a ser pago é R$ {:.2f}'.format(valor))