'''
При регистрации на сайтах требуется вводить пароль дважды.
Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

Напишите программу, которая сравнивает пароль и его подтверждение.
Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
'''
input1 = input()
input2 = input()
if input1 == input2:
    print('Пароль принят')
else:
    print('Пароль не принят')

'''
Напишите программу, которая определяет, является число четным или нечетным.
'''
input = int(input())
if input % 2 == 1:
    print('Нечетное')
else:
    print('Четное')

'''
Напишите программу, которая проверяет, что для заданного четырехзначного числа
выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
'''
input = int(input())
a = input % 10000 // 1000
b = input % 1000 // 100
c = input % 100 // 10
d = input % 10
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')

'''
Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
'''
age = int(input())
if age < 18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')

'''
Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
последовательными членами арифметической прогрессии.
'''
one = int(input())
two = int(input())
three = int(input())
if (two - one) + two == three:
    print('YES')
else:
    print('NO')

'''
Напишите программу, которая определяет наименьшее из двух чисел.
'''
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

'''
Напишите программу, которая определяет наименьшее из четырёх чисел.
'''
one = int(input())
two = int(input())
three = int(input())
four = int(input())

if one > two:
    a = two
else:
    a = one

if three > four:
    b = four
else:
    b = three

if a > b: print(b)
else: print(a)

'''
Напишите программу, которая по введённому возрасту пользователя сообщает,
к какой возрастной группе он относится:

- до 13 включительно – детство;
- от 14 до 24 – молодость;
- от 25 до 59 – зрелость;
- от 60 – старость.
'''
age = int(input())

if age <= 13:
    print('детство')
elif 13 <= age <= 24:
    print('молодость')
elif 25 <= age <= 59:
    print('зрелость')
else:
    print('старость')

'''
Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
'''
one = int(input())
two = int(input())
three = int(input())

sum = 0

if one > 0: sum = sum + one
if two > 0: sum = sum + two
if three > 0: sum = sum + three

print(sum)

'''
Напишите программу, которая принимает целое число x и определяет,
принадлежит ли данное число указанному промежутку.
'''
x = int(input())
if x > -1 and x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

'''
Напишите программу, которая принимает целое число x и определяет,
принадлежит ли данное число указанным промежуткам.
'''
x = int(input())
if x >= 7 or x <= -3:
    print('Принадлежит')
else:
    print('Не принадлежит')

'''
Напишите программу, которая принимает целое число x и определяет,
принадлежит ли данное число указанным промежуткам.
'''
x = int(input())
if x > -30 and x <=-2 or x > 7 and x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

'''
Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
Напишите программу, определяющую, является ли введённое число красивым.
Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
'''
x = int(input())
if (x // 1000 > 0 and x // 1000 <= 9) and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else:
    print('NO')

'''
Напишите программу, которая принимает три положительных числа и определяет,
существует ли невырожденный треугольник с такими сторонами.
'''
a = int(input())
b = int(input())
c = int(input())
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print('YES')
else:
    print('NO')

'''
Напишите программу, которая определяет, является ли год с данным номером високосным.
Если год является високосным, то выведите «YES», иначе выведите «NO».

Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
'''
year = int(input())

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print('YES')
else:
    print('NO')

'''
Даны две различные клетки шахматной доски. Напишите программу, которая определяет,
может ли ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и
номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести «YES», если из первой клетки ходом ладьи можно попасть во вторую,
или «NO» в противном случае.
'''
col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (col1 == col2 and row1 != row2) or (col1 != col2 and row1 == row2):
    print('YES')
else:
    print('NO')

'''
Даны две различные клетки шахматной доски. Напишите программу,  которая определяет,
может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход
четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля
можно попасть во вторую, или «NO» в противном случае.
'''
col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if (abs(col1 - col2) == 1 or abs(col1 - col2) == 0) and (abs(row1 - row2) == 1 or abs(row1 - row2) == 0):
    print('YES')
else:
    print('NO')

'''
На вход программе подаётся два целых числа n и k, скорость Зума и Флэша.

Формат выходных данных
Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES»,
если их скорости равны нужно вывести "Don't know".
'''
n = int(input())
k = int(input())
if n > k:
    print('NO')
else:
    if n == k:
        print('Don\'t know')
    else:
        print('YES')

'''
Напишите программу, которая принимает три положительных числа и определяет вид треугольника,
длины сторон которого равны введенным числам.
'''
a = int(input())
b = int(input())
c = int(input())

if a == b or a == c or b == c:
    if a == b == c:
        print('Равносторонний')
    else:
        print('Равнобедренный')
else:
    print('Разносторонний')

'''
Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.
'''
a = int(input())
b = int(input())
c = int(input())

if a < b < c or a > b > c:
    print(b)
elif b < c < a or b > c > a:
    print(c)
else:
    print(a)

'''
Дан порядковый номер месяца (1, 2,…, 12). Напишите программу, которая выводит на экран
количество дней в этом месяце. Принять, что год является невисокосным.
'''
x = int(input())
if x == 2:
    print('28')
elif x <= 7:
    print(30 + x % 2)
else:
    print(31 - x % 2)

'''
Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть
отнесён к одной из трех весовых категорий:

    Легкий вес – до 60 кг;
    Первый полусредний вес – до 64 кг;
    Полусредний вес – до 69 кг.

Напишите программу, определяющую, в какой категории будет выступать данный боксер.
'''
x = int(input())
if x < 60:
    print('Легкий вес')
elif x < 64:
    print('Первый полусредний вес')
elif x < 69:
    print('Полусредний вес')

'''
Напишите программу, которая считывает с клавиатуры два целых числа и строку.
Если эта строка является обозначением одной из четырёх математических операций (+, -, *, /),
то выведите результат применения этой операции к введённым ранее числам,
в противном случае выведите «Неверная операция».
Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».
'''
a = int(input())
b = int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')
