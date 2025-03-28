def santa_users(users_list):
    """
    Вы санта. Вы попросили эльфа вернуть вам список пользователей, где каждый пользователь представляет собой еще один список,
    который содержит один или два элемента: строка (имя пользователя) и его почтовый индекс.
    Напишите функцию santa_users(), которая принимает двумерный список, и возвращает словарь с элементом для каждого пользователя,
    где ключ - это имя пользователя, а значение - почтовый индекс пользователя. Если нет индекса, тогда значение должно быть None.
        Пример: [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]. У одного пользователя есть имя, но нет индекса.
    santa_users() вернет этот словарь:
{
    "name1 surname1": 12345,
    "name2 surname2": None,
    "name3 surname3": 12354,
    "name4 surname4": 12435,
}
    """
    users_dict = {}

    for user in users_list:
        # Проверка на пустой элемент в списке пользователей
        if not user:
            continue

        name = user[0]
        # Проверяем наличие почтового индекса (второй элемент может быть 0 или False)
        postal_code = user[1] if len(user) > 1 and user[1] is not None else None
        users_dict[name] = postal_code

    return users_dict

def main():
    users = [
        ["name1 surname1", 12345],
        ["name2 surname2"],
        ["name3 surname3", 12354],
        ["name4 surname4", 12435]
    ]
    for name, code in santa_users(users).items():
        print(f'{name}: {code}')

if __name__ == '__main__':
    main()
