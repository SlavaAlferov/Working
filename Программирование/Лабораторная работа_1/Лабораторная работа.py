def find_expression(nums, target, current_index=0, current_sum=0, expression=""):
    # Базовый случай: все числа обработаны
    if current_index == len(nums):
        if current_sum == target:
            return expression
        else:
            return None

    # Пробуем добавить текущее число
    positive_case = find_expression(
        nums, 
        target, 
        current_index + 1, 
        current_sum + nums[current_index], 
        expression + "+" + str(nums[current_index]) if expression else str(nums[current_index])
    )

    if positive_case is not None:
        return positive_case

    # Пробуем вычесть текущее число
    negative_case = find_expression(
        nums, 
        target, 
        current_index + 1, 
        current_sum - nums[current_index], 
        expression + "-" + str(nums[current_index])
    )

    return negative_case

def main():
    # Считывание данных из файла
    with open("input.txt", "r") as file:
        data = list(map(int, file.read().strip().split()))
    
    N = data[0]  # количество чисел
    nums = data[1:N+1]  # числа
    S = data[N+1]  # целевое значение

    # Находим выражение
    result = find_expression(nums, S)

    # Запись результата в выходной файл
    with open("output.txt", "w") as file:
        if result:
            file.write(result + "=" + str(S) + "\n")
        else:
            file.write("no solution\n")

if __name__ == "__main__":
    main()