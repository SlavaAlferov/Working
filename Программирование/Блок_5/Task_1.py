def rob_banks(banks):
    n = len(banks)
    if n == 0:
        return {
            'money': 0,
            'bank_names': "нет банков",
            'bank_indices': "нет банков"
        }

    # Инициализация массива для хранения максимальных сумм
    dp = [0] * n
    dp[0] = banks[0][1]  # Базовый случай: только один банк

    if n > 1:
        dp[1] = max(banks[0][1], banks[1][1])  # Выбираем лучший из двух первых банков

    # Заполняем массив dp по принципу динамического программирования
    for i in range(2, n):
        # Максимум из:
        # 1) Не грабим текущий банк (берем предыдущий максимум)
        # 2) Грабим текущий банк + максимум двух банков назад
        dp[i] = max(dp[i-1], dp[i-2] + banks[i][1])

    # Восстанавливаем список ограбленных банков
    robbed_banks = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            robbed_banks.append(banks[i])
            i -= 2  # Пропускаем предыдущий банк (соседний нельзя грабить)
        else:
            i -= 1  # Переходим к предыдущему банку

    robbed_banks.reverse()  # Восстанавливаем исходный порядок

    return {
        'money': dp[-1],
        'bank_names': [bank[0] for bank in robbed_banks],
        'bank_indices': [banks.index(bank) for bank in robbed_banks]
    }

def main():
    banks = [("sber", 3), ("ZXC", 10), ("VTB", 5), ("Alfa", 7)]

    result = rob_banks(banks)

    print(f"Максимально денег украдено: {result['money']}")
    print(f"Ограблено банков: {result['bank_names'] if result['bank_names'] else 'нет банков'}")
    print(f"Номера ограбленных банков: {result['bank_indices'] if result['bank_indices'] else 'нет банков'}")

if __name__ == '__main__':
    main()
