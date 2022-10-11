
print('Calcule quantos litros de tinta serão necessários para pintar sua parede.\n')
print('-' * 25)

largura = float(input('\nInsira a largura: '))
altura = float(input('Insira a altura: '))
area = largura * altura
tinta = area / 2

print('-' * 25)
print('Essa parede possui {:.2f} m²'.format(area))
print('Para pintar essa parede você precisa de {:.2f}l de tinta.'.format(tinta))