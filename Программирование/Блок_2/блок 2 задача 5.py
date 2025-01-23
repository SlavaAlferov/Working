# Проверяет что все цифры заданного натурального трехзначного числа различны

num, d = int(input()), []
if num>0 and len(str(num))==3:
    for i in range(len(str(num))):
        if str(num)[i] not in d:
            d.append(str(num)[i])
        else:
            print(f'В числе {num} есть повторяющиеся цифры')
            exit()
    print(f'В числе {num} нет повторяющихся цифр')
else:print(f'Число {num} не натуральное или не трёхзначное')