def find(input_str):
    """
    С клавиатуры поступает строка. Необходимо вывести самую длинную подстроку без повторных символов.
        Input: “qweasdfdqw"
        Output: "qweasd"
        Input: "aaaaaaa"
        Output: "a"
        Input: "prrker"
        Output: "rke"
    """
    used_chars = ''  # Хранит уникальные символы текущей подстроки
    current_substr = ''  # Текущая подстрока без повторений
    max_substr = ''  # Самая длинная найденная подстрока

    for char in input_str:
        if char not in used_chars:
            used_chars += char
            current_substr += char
        else:
            if len(current_substr) > len(max_substr):
                max_substr = current_substr

            # Находим индекс повторяющегося символа
            index = used_chars.index(char)
            # Обновляем used_chars и current_substr
            used_chars = used_chars[index + 1:] + char
            current_substr = current_substr[index + 1:] + char

    # Проверяем последнюю подстроку
    if len(current_substr) > len(max_substr):
        max_substr = current_substr

    return max_substr if max_substr else input_str[0] if input_str else ''

def main():
    # Получаем ввод от пользователя
    input_str = input("").strip()

    print(find(input_str))

if __name__ == '__main__':
    main()
