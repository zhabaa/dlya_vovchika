Калькулятор кратных интегралов (Double & Triple Integrals)
Python
SymPy

Простой и удобный калькулятор для вычисления двойных и тройных интегралов с использованием библиотеки sympy. Поддерживает символьные вычисления и работу с параметрическими пределами.

📦 Установка
Клонируйте репозиторий:

bash
Copy
git clone https://github.com/ваш-username/integrals-calculator.git
cd integrals-calculator
Установите зависимости (если у вас нет sympy):

bash
Copy
pip install sympy
🛠 Использование
📌 Примеры кода
1. Двойной интеграл
python
Copy
from integrals import calculate_double_integral
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2
result = calculate_double_integral(f, (x, 0, 1), (y, 0, 2))
print(result)  # Вывод: 10/3
2. Тройной интеграл
python
Copy
from integrals import calculate_triple_integral
import sympy as sp

x, y, z = sp.symbols('x y z')
f = x + y + z
result = calculate_triple_integral(f, (x, 0, 1), (y, 0, 1), (z, 0, 1))
print(result)  # Вывод: 3/2
🔥 Возможности
Символьные вычисления — работа с аналитическими выражениями.

Поддержка параметрических пределов (например, y от 0 до x).

Несобственные интегралы — можно задавать бесконечные пределы (sp.oo).

Численное интегрирование через .evalf() (если символьное решение невозможно).

📂 Структура проекта
Copy
integrals-calculator/
├── integrals.py       # Основной код с функциями integrate_double и integrate_triple
├── README.md          # Этот файл
└── examples.py        # Примеры использования (опционально)
🤝 Как можно улучшить?
Добавить графическую визуализацию областей интегрирования (matplotlib).

Реализовать поддержку пользовательского ввода через CLI.

Расширить для N-мерных интегралов.

📜 Лицензия
MIT — свободное использование с указанием авторства.

Теперь ваш проект выглядит профессионально! Если хотите что-то добавить (например, скриншоты или более сложные примеры), просто отредактируйте README.md. 😊