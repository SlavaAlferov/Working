def roman_to_arabic(roman_num):
    """
    Реализуйте функцию, принимающую один аргумент (римское число) и возвращающее арабское.
    """
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    # Обрабатываем строку справа налево
    for char in reversed(roman_num):
        current_value = roman_dict[char]

        if current_value < prev_value:
            result -= current_value  # Вычитаем (случаи типа IV, IX и т.д.)
        else:
            result += current_value  # Складываем

        prev_value = current_value
    return result

def main():
    roman_input = input("Римское число: ").strip().upper()
    print("Арабское число:",roman_to_arabic(roman_input))

if __name__ == '__main__':
    main()
