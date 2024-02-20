import matplotlib.pyplot as plt
import numpy as np

import methods


# y' = f(x,y); y(0) = 0.1, на отрезке [0, 1]
def f(x, y):
    return 50 * y * (x - 0.6) * (x - 0.85)

# 1-ая производная f по x:   
def d1f(x, y):
    return 50 * (f(x, y) * (x - 0.6) * (x - 0.85) \
                 + y * (2 * x - 1.45))

# 2-ая производная f по x:
def d2f(x, y):
    return 50 * (d1f(x, y) * (x - 0.6) * (x - 0.85) \
                 + 2 * f(x, y) * (2 * x - 1.45) + 2 * y)

# 3-я производная f по x:
def d3f(x, y):
    return 50 * (d2f(x,y) * (x - 0.6) * (x - 0.85) \
                 + 3 * d1f(x, y) * (2 * x - 1.45) + 6 * f(x, y))

# Аналитически найденное решение ДУ (сравним его на графике с приближенными решениями)
def y(x):
    return 0.1 * np.e ** ( (50 / 3) * (x ** 3) \
                     - (145 / 4) * (x ** 2) \
                      + (51 / 2) *  x)




if __name__ == '__main__':
    N = int(input())
    euler = methods.EulerMethod(f, num_points=N, y0=0.1)
    cauchy = methods.CauchyMethod(f, num_points=N, y0=0.1)
    taylor = methods.TaylorMethod(f, d1f, d2f, d3f, num_points=N, y0=0.1)

    X, Y_E = euler.calculate()
    _, Y_C = cauchy.calculate()
    _, Y_T = taylor.calculate()
    rr = np.arange(0, 1, 0.0001)
    if N >= 91: 
        Marker = ''
    else: Marker = '.'
    plt.plot(X, Y_E, color='#F01F1F', linestyle='--', marker=Marker, label='Метод Эйлера')
    plt.plot(X, Y_C, color='#2EBA45', linestyle='--', marker=Marker, label='Метод Коши')
    plt.plot(X, Y_T, color='#01FFCD', linestyle='--', marker=Marker, label='Метод Тейлора 4 порядка')
    plt.plot(rr, y(rr), label='Точное решение')
    plt.title("Сравнение численных методов решения начальной задачи Коши")
            
    # Даем имена осям
    plt.xlabel("ось x")
    plt.ylabel("ось y")
    
    # Используем этот метод для удаления лишнего белого/пустого пространства
    plt.tight_layout()
            
    # Стиль графика:
    plt.style.use('fast')
            
    # Добавляем сетку на график, чтоб было удобнее его анализировать
    plt.grid()
            
    # Добавляем легенду
    plt.legend()
            
    # Показываем график
    plt.show()