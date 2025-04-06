import sympy as sp


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


if __name__ == "__main__":
    # какие переменные
    x, y, z = sp.symbols('x y z')

    # Двойной интеграл
    f1 = x + y
    x_limits = (x, 0, 1)
    y_limits = (y, 0, 1)

    double_result = calculate_double_integral(f1, x_limits, y_limits)
    print(f"Двойной интеграл от {f1}:")
    print(double_result)
    print()

    # Тройной интеграл
    f2 = x + y + z

    x_limits = (x, 0, 1)
    y_limits = (y, 0, 1)
    z_limits = (z, 0, 1)

    triple_result = calculate_triple_integral(f2, x_limits, y_limits, z_limits)
    print(f"Тройной интеграл от {f2}:")
    print(triple_result)