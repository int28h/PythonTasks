import numpy as np

'''
Вычисляет результат сумматорной функции для каждого примера из input_matrix. 
input_matrix - матрица примеров размера (n, m), каждая строка - отдельный пример,
n - количество примеров, m - количество переменных.
Возвращает вектор значений сумматорной функции размера (n, 1).
'''
def summatory(self, input_matrix):    
    return np.dot(input_matrix, self.w)

'''
Вычисляет для каждого примера результат активационной функции,
получив на вход вектор значений сумматорной функций
summatory_activation - вектор размера (n, 1), 
где summatory_activation[i] - значение суммматорной функции для i-го примера.
Возвращает вектор размера (n, 1), содержащий в i-й строке 
значение активационной функции для i-го примера.
'''
def activation(self, summatory_activation):
    return self.activation_function(summatory_activation)

def vectorized_forward_pass(self, input_matrix):
    return self.activation(self.summatory(input_matrix))