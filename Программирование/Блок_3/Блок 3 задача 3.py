def zigzag_convert(s, num_rows):
    # Если количество строк 1 или больше длины строки, то просто вернуть исходную строку
    if num_rows == 1 or num_rows >= len(s):
        return s

    # Создаем список для хранения строк в каждой "строке" зигзага
    rows = [''] * num_rows
    current_row = 0
    direction = 1  # 1 означает движение вниз, -1 означает движение вверх

    # Проходим по каждому символу в строке
    for char in s:
        # Добавляем символ в текущую строку
        rows[current_row] += char
        # Меняем направление при достижении верхней или нижней строки
        if current_row == 0:
            direction = 1
        elif current_row == num_rows - 1:
            direction = -1
        current_row += direction

    # Склеиваем все строки в одну
    return ''.join(rows)

# Примеры использования функции
print(zigzag_convert("перфекционист", 3))  # Вывод: "пеотефкинсрци"
print(zigzag_convert("перфекционист", 4))  # Вывод: "пцтекисреоифн"
print(zigzag_convert("перфекционист", 1))  # Вывод: "перфекционист"