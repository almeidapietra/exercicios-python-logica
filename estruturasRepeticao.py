# while:
n = int(input('digite o numero '))

while n > 0:
    if (n % 2 == 0):
        print('par')
    else:
        print('impar')
    n = int(input('digite o numero '))

# for:
for i in range(1, 4, 1):
    print('i: ', i)
    n = int(input('digite o numero '))
    if (n % 2 == 0):
        print('par')
    else:
        print('impar')
