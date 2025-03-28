# число десятков и единиц в двузначном числе
num=int(input())
if num > 0:
    print('Кол-во десятков: ', int(str(num)[0]), '\n', 'Кол-во единиц: ', int(str(num)[1]), sep=(''))
else:
    print('Кол-во десятков: ', int(str(num)[1]), '\n', 'Кол-во единиц: ', int(str(num)[2]), sep=(''))
