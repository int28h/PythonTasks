'''
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
'''
a = float(input())
b = float(input())
print(0.5 * a * b)

'''
Две старушки идут навстречу друг другу с постоянными скоростями V1​ и V2​ км/ч.
Определите, через какое время старушки встретятся, если расстояние между ними равно S км.
'''
s = float(input())
v_first = float(input())
v_second = float(input())
print(s / (v_first + v_second))

'''
Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
'''
input = float(input())
if input == 0:
    print('Обратного числа не существует')
else:
    print(1 / input)

'''
Напишите программу, которая определяет, какой температуре по шкале Цельсия
соответствует указанное значение по шкале Фаренгейта.
'''
input = float(input())
print(5 / 9 * (input - 32))

'''
На вход программе подается число n – количество собачьих лет.
Напишите программу, которая вычисляет возраст собаки в человеческих годах.

Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам.
После этого каждый год собаки равен 4 человеческим годам.
'''
input = float(input())
if input <= 2:
    print(input * 10.5)
else:
    print((2 * 10.5) + ((input - 2) * 4))

'''
Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
'''
input = float(input())
print(int(input * 10  % 10))

'''
Дано положительное действительное число. Выведите его дробную часть.
'''
input = float(input())
print(input % int(input))

'''
Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max(a, b, c, d, e))

'''
Напишите программу, которая упорядочивает три числа от большего к меньшему.
'''
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print((a+b+c) - (max(a, b, c)) - (min(a, b, c)))
print(min(a, b, c))

'''
Назовем число интересным, если в нем разность максимальной и минимальной цифры
равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет.
Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
'''
input = int(input())
a, b, c = input // 100, input // 10 % 10, input % 10
mid = (a + b + c) - max(a, b, c) - min(a, b, c)
if max(a, b, c) - min(a, b, c) == mid:
    print('Число интересное')
else:
    print('Число неинтересное')

'''
Даны пять чисел​. Напишите программу, которая вычисляет сумму их модулей.
'''
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

'''
На плоскости манхэттенское расстояние между двумя точками (p1; p2) и (q1; q2)
определяется так ∣p1−q1∣+∣p2−q2∣.

Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
'''
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))

'''
Напишите программу, которая выводит текст:
"Python is a great language!", said Fred. "I don't ever remember having this much fun before."
'''
print("\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before.\"")

'''
Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
«Hello [введенное имя] [введенная фамилия]! You just delved into Python».
'''
firstname = input()
lastname = input()
print("Hello " + firstname + " " + lastname + "! You just delved into Python", sep = '')

'''
Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
'''
teamname = input()
print("Футбольная команда " + teamname + " имеет длину " + str(len(teamname)) + " символов", sep='')

'''
Даны названия трех городов. Напишите программу, которая определяет самое короткое
и самое длинное название города.
'''
one = input()
two = input()
three = input()
print(min(one, two, three, key=len))
print(max(one, two, three, key=len))

'''
Вводятся 3 строки в случайном порядке.
Напишите программу, которая выясняет можно ли из длин этих строк построить
возрастающую арифметическую прогрессию.
'''
a = len(input())
b = len(input())
c = len(input())

if (2 * b - c - a) * (2 * c -b - a) * (2 * a -b - c) == 0:
    print('YES')
else:
    print('NO')

'''
Напишите программу, которая считывает одну строку, после чего выводит «YES»,
если в введенной строке есть подстрока «синий» и «NO» в противном случае.
'''
input = input()
if 'синий' in input:
    print('YES')
else:
    print('NO')

'''
Напишите программу, которая считывает одну строку, после чего выводит «YES»,
если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
'''
input = input()
if 'суббота' in input or 'воскресенье' in input:
    print('YES')
else:
    print('NO')

'''
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки.
Напишите программу проверяющую корректность email адреса.
'''
input = input()
if '@' in input and '.' in input:
    print('YES')
else:
    print('NO')

'''
На плоскости евклидово расстояние между двумя точками (x1; y1) и (x2; y2)
определяется так ρ=sqrt((x1−x2)^2+(y1−y2)^2)
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
'''
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

'''
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
'''
import math

r = float(input())

print(math.pi * pow(r, 2))
print(2 * math.pi * r)

'''
На вход программе подается два вещественных числа a и b​, каждое на отдельной строке.
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
'''
import math

a = float(input())
b = float(input())

print((a + b) / 2)
print(math.sqrt(a * b))
print((2 * a * b) / (a + b))
print(math.sqrt((pow(a, 2) + pow(b, 2)) / 2))

'''
Напишите программу, вычисляющую значение тригонометрического выражения
sin⁡x+cos⁡x+(tan⁡ x)^2 по заданному числу градусов x.
'''
import math

xGrades = float(input())
xRads = (xGrades * math.pi) / 180

print(math.sin(xRads) + math.cos(xRads) + pow(math.tan(xRads), 2))
