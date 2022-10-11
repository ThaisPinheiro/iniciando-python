
n = int(input('Insira um número inteiro: '))
print('-' * 15)

for count in range(10):
    print("%d x %d = %d" % (n, count+1, n*(count+1)) )

print('-' * 15)