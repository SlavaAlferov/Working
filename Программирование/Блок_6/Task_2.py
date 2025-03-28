from itertools import combinations

def get_unique_subsets(elements):
    """
    Генерирует все уникальные подмножества из списка элементов (без повторений)
    и возвращает их в отсортированном виде с количеством.
    """
    # Удаляем дубликаты, сохраняя порядок (если важно)
    unique_elements = list(dict.fromkeys(elements))

    # Генерируем все возможные подмножества (кроме пустого)
    subsets = set()  # Используем множество для автоматического удаления дублей

    for r in range(1, len(unique_elements) + 1):
        for combo in combinations(unique_elements, r):
            # Сортируем и преобразуем в строку без лишних символов
            sorted_str = "".join(sorted(map(str, combo)))
            subsets.add(sorted_str)

    # Сортируем подмножества по длине, затем по значению
    sorted_subsets = sorted(subsets, key=lambda x: (len(x), x))

    return sorted_subsets, len(sorted_subsets)

def main():
    input =[1, 2, 3, 4]
    input =['a', 'b', 'c', 'd', 'd']
    input =[1, 1, 1]
    input =['x', 'y', 'x', 'z']

    for lst in input:
        subsets, count = get_unique_subsets(lst)

        # Красиво форматируем вывод подмножеств
        formatted_subsets = []
        for s in subsets:
            if len(s) == 1:
                formatted_subsets.append(s)
            else:
                formatted_subsets.append(', '.join(s))

        print("Подмножества:",formatted_subsets,"; Количество:",count)

if __name__ == '__main__':
    main()
