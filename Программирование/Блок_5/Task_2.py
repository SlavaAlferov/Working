def matrix(matrix):
    """
    Транспонирование матрицы
    """
    for i in range(len(matrix[0])):
        print(' '.join(str(matrix[j][i]) for j in range(len(matrix))))


def main():
    M = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    M =[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
    matrix(M)

if __name__ == '__main__':
    main()
