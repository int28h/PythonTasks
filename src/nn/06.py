'''
Найдите оптимальные коэффициенты для построения линейной регрессии.

На вход вашему решению будет подано название csv-файла, из которого нужно считать данные. 
Загрузить их можно следующим образом:

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

Ваша задача — подсчитать вектор коэффициентов линейной регрессии для предсказания первой переменной (первого столбца данных) 
по всем остальным. Напомним, что модель линейной регрессии — это y = β0 + β1x1 + ... + βnxn.

Напечатайте коэффициенты линейной регрессии, начиная с β0, через пробел. 
Мы будем проверять совпадения с точностью до 4 знаков после запятой.

Методы и приёмы, которые мы ещё не упоминали и которые могут вам помочь в процессе решения (могут являться подсказками!):

np.hstack((array1, array2, ...))  # склеивает по строкам массивы, являющиеся компонентами кортежа, поданного на вход; 
массивы должны совпадать по всем измерениям, кроме второго

np.ones_like(array)  # создаёт массив, состоящий из единиц, идентичный по форме массиву array

"delim".join(array)  # возвращает строку, состоящую из элементов array, разделённых символами "delim"

map(str, array)  # применяет функцию str к каждому элементу array

Sample Input:
https://stepic.org/media/attachments/lesson/16462/boston_houses.csv

Sample Output:
-3.65580428507 -0.216395502369 0.0737305981755 4.41245057691 -25.4684487841 7.14320155075 -1.30108767765
'''
import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

Y = np.array(data[:,0])

data[:,0] = 1

res = np.linalg.inv(data.T.dot(data)).dot(data.T).dot(Y)
print(*res)