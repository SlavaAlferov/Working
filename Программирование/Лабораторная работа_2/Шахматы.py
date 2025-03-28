def is_safe(board, row, col, N):
    """Проверяет безопасность клетки"""
    attack_pattern = [
        (-4,-4), (-4,4), (4,-4), (4,4),
        (-3,-3), (-3,3), (3,-3), (3,3),
        (-2,-2), (-2,2), (2,-2), (2,2),
        (-1,-1), (-1,1), (1,-1), (1,1)]

    for di, dj in attack_pattern:
        r, c = row + di, col + dj
        if 0 <= r < N and 0 <= c < N and board[r][c] == 1:
            return False
    return True


def mark_attacked_cells(board, positions, N):
    """Размечает клетки под боем"""
    # Очищаем предыдущие отметки
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 0

    attack_pattern = [
        (-4,-4), (-4,4), (4,-4), (4,4),
        (-3,-3), (-3,3), (3,-3), (3,3),
        (-2,-2), (-2,2), (2,-2), (2,2),
        (-1,-1), (-1,1), (1,-1), (1,1)]

    for x, y in positions:
        for di, dj in attack_pattern:
            r, c = x + di, y + dj
            if 0 <= r < N and 0 <= c < N and board[r][c] == 0:
                board[r][c] = 2


def place_figures(board, start_row, start_col, positions, placed, total_required, N, solutions):
    """Рекурсивно размещает фигуры, избегая дубликатов перестановок"""
    if placed == total_required:
        # Сохраняем отсортированное решение для уникальности
        sorted_solution = tuple(sorted(positions))
        if sorted_solution not in solutions:
            solutions[sorted_solution] = True
        return

    # Продолжаем размещение с текущей позиции
    for i in range(start_row, N):
        start_j = start_col if i == start_row else 0
        for j in range(start_j, N):
            if board[i][j] == 0 and is_safe(board, i, j, N):
                # Сохраняем текущее состояние
                old_board = [row[:] for row in board]

                # Размещаем фигуру
                board[i][j] = 1
                positions.append((i, j))
                mark_attacked_cells(board, positions, N)

                # Рекурсивный вызов с новой стартовой позицией
                place_figures(board, i, j + 1, positions, placed + 1, total_required, N, solutions)

                # Backtrack
                board[i][j] = 0
                positions.pop()
                board = [row[:] for row in old_board]
                mark_attacked_cells(board, positions, N)


def main():
    # Чтение входных данных
    with open('input.txt', 'r') as file:
        N, L, K = map(int, file.readline().strip().split())
        board = [[0] * N for _ in range(N)]
        initial_positions = []

        for _ in range(K):
            x, y = map(int, file.readline().strip().split())
            board[x][y] = 1
            initial_positions.append((x, y))

    # Первоначальная разметка клеток под боем
    mark_attacked_cells(board, initial_positions, N)

    # Используем словарь для хранения уникальных решений
    unique_solutions = {}
    place_figures(board, 0, 0, initial_positions.copy(), K, K + L, N, unique_solutions)

    # Запись количества решений
    with open('output.txt', 'w') as out_file:
        out_file.write(f'{len(unique_solutions)}\n')

    # Вывод информации
    print("Количество решений:",len(unique_solutions))
    if unique_solutions:
        # Получаем первое решение
        first_solution = next(iter(unique_solutions.keys()))
        print("  Доска:")

        # Создаем демонстрационную доску
        demo_board = [[0] * N for _ in range(N)]
        for x, y in first_solution:
            demo_board[x][y] = 1
        mark_attacked_cells(demo_board, first_solution, N)

        # Выводим доску
        for row in demo_board:
            print(' '.join('#' if cell == 1 else '*' if cell == 2 else '0' for cell in row))


if __name__ == '__main__':
    main()
