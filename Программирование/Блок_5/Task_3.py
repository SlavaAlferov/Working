def spiral(matrix):
    """
    Функция получает на вход матрицу, а возвращает элементы матрицы в порядке спирального обхода
    """
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Движение вправо по верхней строке
        result += matrix[top][left:right + 1]
        top += 1

        # Движение вниз по правому столбцу
        result += [matrix[i][right] for i in range(top, bottom + 1)]
        right -= 1

        if top <= bottom:  # Проверка, есть ли еще строки
            # Движение влево по нижней строке (в обратном порядке)
            result += matrix[bottom][left:right + 1][::-1]
            bottom -= 1

        if left <= right:  # Проверка, есть ли еще столбцы
            # Движение вверх по левому столбцу (в обратном порядке)
            result += [matrix[i][left] for i in range(bottom, top - 1, -1)]
            left += 1

    return result

def main():
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    M = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
    print(spiral(M))

if __name__ == '__main__':
    main()
