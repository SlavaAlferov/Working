def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        N, L, K = map(int, lines[0].strip().split())
        placed_figures = [tuple(map(int, line.strip().split())) for line in lines[1:K+1]]
    return N, L, K, placed_figures

def is_safe(board, x, y, N):
    # Проверка по горизонтали и вертикали
    for i in range(N):
        if board[x][i] == '#' or board[i][y] == '#':
            return False
    
    # Проверка диагоналей на расстоянии 2
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '#':
            return False
    
    return True

def place_figures(board, L, N, solutions, current_figures):
    if L == 0:
        solutions.append(list(current_figures))
        return

    for x in range(N):
        for y in range(N):
            if board[x][y] == '0' and is_safe(board, x, y, N):
                board[x][y] = '#'
                current_figures.append((x, y))
                place_figures(board, L - 1, N, solutions, current_figures)
                current_figures.pop()
                board[x][y] = '0'

def print_board(board):
    for row in board:
        print(' '.join(row))

def format_solution(solutions):
    return '\n'.join(' '.join(f'({x},{y})' for x, y in solution) for solution in solutions)

def write_output(filename, solutions):
    with open(filename, 'w') as f:
        if solutions:
            f.write(format_solution(solutions))
        else:
            f.write('no solutions')

def main():
    N, L, K, placed_figures = read_input('input.txt')

    board = [['0' for _ in range(N)] for _ in range(N)]
    
    # Размещаем уже стоящие фигуры
    for x, y in placed_figures:
        board[x][y] = '#'
    
    solutions = []
    place_figures(board, L, N, solutions, placed_figures)

    # Печатаем доску в консоль
    print_board(board)
    
    # Записываем решения в выходной файл
    write_output('output.txt', solutions)

if __name__ == '__main__':
    main()