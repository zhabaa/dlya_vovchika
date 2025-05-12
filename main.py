import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def calculate_double_integral(f, x_lim, y_lim):
    """
    Вычисляет двойной интеграл функции f по переменным x и y в заданных пределах.

    Параметры:
        f: sympy выражение - подынтегральная функция.
        x_lim: кортеж (x, x_min, x_max) - пределы интегрирования по x.
        y_lim: кортеж (y, y_min, y_max) - пределы интегрирования по y.

    Возвращает:
        Результат вычисления двойного интеграла.
    """
    x, x_a, x_b = x_lim
    y, y_a, y_b = y_lim

    inner_integral = sp.integrate(f, (y, y_a, y_b))
    double_integral = sp.integrate(inner_integral, (x, x_a, x_b))

    return double_integral


def calculate_triple_integral(f, x_lim, y_lim, z_lim):
    """
    Вычисляет тройной интеграл функции f по переменным x, y и z в заданных пределах.

    Параметры:
        f: sympy выражение - подынтегральная функция.
        x_lim: кортеж (x, x_min, x_max) - пределы интегрирования по x.
        y_lim: кортеж (y, y_min, y_max) - пределы интегрирования по y.
        z_lim: кортеж (z, z_min, z_max) - пределы интегрирования по z.

    Возвращает:
        Результат вычисления тройного интеграла.
    """
    x, x_a, x_b = x_lim
    y, y_a, y_b = y_lim
    z, z_a, z_b = z_lim

    inner_integral = sp.integrate(f, (z, z_a, z_b))
    middle_integral = sp.integrate(inner_integral, (y, y_a, y_b))
    triple_integral = sp.integrate(middle_integral, (x, x_a, x_b))

    return triple_integral


def plot_double_integral(f, x_lim, y_lim):
    """
    Визуализирует подынтегральную функцию для двойного интеграла.

    Параметры:
        f: sympy выражение - функция для визуализации.
        x_lim: кортеж (x, x_min, x_max) - пределы по x.
        y_lim: кортеж (y, y_min, y_max) - пределы по y.
    """
    x, x_a, x_b = x_lim
    y, y_a, y_b = y_lim

    f_np = sp.lambdify((x, y), f, 'numpy')

    x_vals = np.linspace(float(x_a), float(x_b), 10)
    y_vals = np.linspace(float(y_a), float(y_b), 10)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f_np(X, Y)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'График функции {f} для двойного интеграла')
    plt.show()


def plot_triple_integral(f, x_lim, y_lim, z_lim):
    """
    Визуализирует подынтегральную функцию для тройного интеграла (2D срезы).

    Параметры:
        f: sympy выражение - функция для визуализации.
        x_lim: кортеж (x, x_min, x_max) - пределы по x.
        y_lim: кортеж (y, y_min, y_max) - пределы по y.
        z_lim: кортеж (z, z_min, z_max) - пределы по z.
    """
    x, x_a, x_b = x_lim
    y, y_a, y_b = y_lim
    z, z_a, z_b = z_lim

    f_np = sp.lambdify((x, y, z), f, 'numpy')

    z_val = (float(z_a) + float(z_b)) / 2

    x_vals = np.linspace(float(x_a), float(x_b), 10)
    y_vals = np.linspace(float(y_a), float(y_b), 10)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f_np(X, Y, z_val)

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar(label='Значение функции')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Срез функции {f} при z = {z_val:.2f} (тройной интеграл)')
    plt.show()


if __name__ == "__main__":
    x, y, z = sp.symbols('x y z')

    print("Пример 1: Двойной интеграл")
    f1 = 1 + x ** 2 - y ** 3
    x_limits = (x, 0, 1)
    y_limits = (y, 0, 1)

    double_result = calculate_double_integral(f1, x_limits, y_limits)
    print(f"Двойной интеграл от {f1}:")
    print(double_result)
    plot_double_integral(f1, x_limits, y_limits)

    print("\nПример 2: Тройной интеграл")
    f2 = x ** 2 + y ** 2 + z ** 2
    x_limits = (x, 0, 1)
    y_limits = (y, 0, 1)
    z_limits = (z, 0, 1)

    triple_result = calculate_triple_integral(f2, x_limits, y_limits, z_limits)
    print(f"Тройной интеграл от {f2}:")
    print(triple_result)
    plot_triple_integral(f2, x_limits, y_limits, z_limits)
