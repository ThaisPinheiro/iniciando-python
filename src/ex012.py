
d = input('Digite algo: ')
print('O que você digitou é...')
print('O tipo primitivo desse valor é ', type(d))
print('um número?', d.isnumeric())
print('um alfanumérico?', d.isalnum())
print('em letra maiuscula?', d.isupper())
print('um espaço?', d.isspace())