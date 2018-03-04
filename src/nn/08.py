'''
В данном степе вам нужно реализовать метод train_on_single_example класса Perceptron, 
который принимает вектор активации входов example формы (m, 1) 
и правильный ответ для него (число 0 или 1 или boolean),
обновляет значения весов перцептрона в соответствии с этим примером
и возвращает размер ошибки, которая случилась на этом примере до изменения весов (0 или 1)
(на её основании мы потом построим интересный график)
'''
import numpy as np

def train_on_single_example(self, example, y):
    predict = self.vectorized_forward_pass(example.T)[0][0]
    self.w += (y - predict) * example
    self.b += y - predict
    return y - predict