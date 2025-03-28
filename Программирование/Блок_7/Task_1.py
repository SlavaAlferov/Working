import numpy as np
import matplotlib.pyplot as plt

# Исходная функция
def f(x):
    return np.cos(x) * np.sin(x**2 + 8)

# Первая производная
def f_prime(x):
    return -np.sin(x)*np.sin(x**2 + 8) + np.cos(x)*np.cos(x**2 + 8)*2*x

# Вторая производная
def f_double_prime(x):
    term1 = -np.cos(x)*np.sin(x**2 + 8)
    term2 = -np.sin(x)*np.cos(x**2 + 8)*2*x
    term3 = -np.sin(x)*np.cos(x**2 + 8)*2*x
    term4 = np.cos(x)*(-np.sin(x**2 + 8)*4*x**2) + np.cos(x)*np.cos(x**2 + 8)*2
    return term1 + term2 + term3 + term4

# Параметры графика
x_vals = np.linspace(0, 5, 1000)
y_vals = f(x_vals)

# 1. Находим экстремумы
max_idx = np.argmax(y_vals)
min_idx = np.argmin(y_vals)
max_x, max_y = x_vals[max_idx], y_vals[max_idx]
min_x, min_y = x_vals[min_idx], y_vals[min_idx]

# 2. Уравнения касательной и нормали (в точке x0=2)
x0 = 2
y0 = f(x0)
f_prime_x0 = f_prime(x0)

# Касательная: y = f'(x0)(x - x0) + f(x0)
def tangent(x):
    return f_prime_x0 * (x - x0) + y0

# Нормаль: y = -1/f'(x0)(x - x0) + f(x0)
def normal(x):
    return (-1/f_prime_x0) * (x - x0) + y0

# 3. Касательное расслоение (10 касательных)
def tangent_at_point(x_point):
    y_point = f(x_point)
    slope = f_prime(x_point)
    return lambda x: slope * (x - x_point) + y_point

# 4. Длина кривой (численное интегрирование)
def curve_length(a, b, n=1000):
    x_points = np.linspace(a, b, n)
    total = 0
    for i in range(n-1):
        dx = x_points[i+1] - x_points[i]
        dy = f(x_points[i+1]) - f(x_points[i])
        total += np.sqrt(dx**2 + dy**2)
    return total

length = curve_length(0, 5)

# Создаем фигуру с 4 подграфиками
plt.figure(figsize=(15, 10))

# График 1: Основная функция с экстремумами, касательной и нормалью
plt.subplot(2, 2, 1)
plt.plot(x_vals, y_vals, label='f(x) = cos(x)sin(x²+8)')
plt.plot(max_x, max_y, 'ro', label=f'Max: ({max_x:.2f}, {max_y:.2f})')
plt.plot(min_x, min_y, 'bo', label=f'Min: ({min_x:.2f}, {min_y:.2f})')
plt.plot(x_vals, tangent(x_vals), 'g--', label='Касательная')
norm = normal(x_vals)
if norm is not None:
    plt.plot(x_vals, norm, 'm--', label='Нормаль')
plt.title('Основная функция')
plt.legend()
plt.grid()

# График 2: Первая производная
plt.subplot(2, 2, 2)
plt.plot(x_vals, f_prime(x_vals), 'r-', label="f'(x)")
plt.title('Первая производная')
plt.grid()

# График 3: Вторая производная
plt.subplot(2, 2, 3)
plt.plot(x_vals, f_double_prime(x_vals), 'b-', label="f''(x)")
plt.title('Вторая производная')
plt.grid()

# График 4: Касательное расслоение
plt.subplot(2, 2, 4)
plt.plot(x_vals, y_vals, 'k-', label='f(x)')
for x_point in np.linspace(0, 5, 10):
    tangent_func = tangent_at_point(x_point)
    plt.plot(x_vals, tangent_func(x_vals), '--', alpha=0.3)
plt.title('Касательное расслоение')
plt.grid()

plt.tight_layout()
plt.show()

# Вывод результатов
print(f"Максимум функции: {max_y:.4f} при x = {max_x:.4f}")
print(f"Минимум функции: {min_y:.4f} при x = {min_x:.4f}")
print(f"Уравнение касательной в x0={x0}: y = {f_prime_x0:.4f}(x - {x0}) + {y0:.4f}")
print(f"Уравнение нормали в x0={x0}: y = {-1/f_prime_x0:.4f}(x - {x0}) + {y0:.4f}")
print(f"Длина кривой на [0,5]: {length:.4f}")
