# Сумма цифр двузначного числа

num=int(input())
if len(str(num))==2:
    print('Сумма цифр:', int(str(num)[0]) + int(str(num)[1])) # если число > 0
else:
    print('Сумма цифр:', int(str(num)[2]) + int(str(num)[1])) # если число > 0