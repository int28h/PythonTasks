'''
Реализуйте метод vectorized_forward_pass класса Perceptron. 
Метод рассчитывает ответ перцептрона при предъявлении набора примеров
input_matrix - матрица примеров размера (n, m), каждая строка - отдельный пример,
n - количество примеров, m - количество переменных
Возвращает вертикальный вектор размера (n, 1) с ответами перцептрона
(элементы вектора - boolean или целые числа (0 или 1))
'''
import numpy as np

def vectorized_forward_pass(self, input_matrix):
    return input_matrix.dot(self.w) > -self.b