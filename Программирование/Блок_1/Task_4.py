# трехзначное число по цифрам через ,

num=int(input())
if num > 0:
    print(str(num)[0], str(num)[1], str(num)[2], sep=(',')) # если число > 0
else:
    print('-' + str(num)[1], str(num)[2], str(num)[3], sep=(',')) # если число < 0
