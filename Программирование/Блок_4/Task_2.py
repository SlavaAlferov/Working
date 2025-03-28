def reverse(input_str):
    """
    С клавиатуры поступает строка.
    Необходимо вывести строку, где порядок слов в противоположном направлении.
    Первое слово с заглавной буквы, остальные с маленькой. МЕЖДУ словами только ОДИН пробел.
        Input: “hello world”
        Output: "Hello world"
        Input: "it was cool"
        Output: "Cool was it"
        Input: "good"
        Output: "Good"
    """
    if not input_str.strip():
        return ""

    words = input_str.lower().split()
    words.reverse()
    return ' '.join(words).capitalize()


def main():
    input_str = input()
    print(reverse(input_str))

if __name__ == '__main__':
    main()
