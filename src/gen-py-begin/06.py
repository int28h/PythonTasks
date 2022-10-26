'''
Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.
'''
str = 'Python is awesome!'
for _ in range(10):
    print(str)

'''
Дано предложение и количество раз которое его надо повторить.
Напишите программу, которая повторяет данное предложение нужное количество раз.
'''
str = input()
repeat = int(input())

for _ in range(repeat):
    print(str)

'''
Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:

AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G
'''
for i in range(6):
    print('A' * 3)
for i in range(5):
    print('B' * 4)
print('E')
for i in range(9):
    print('T' * 5)
print('G')

'''
На вход программе подается натуральное число nn.
Напишите программу, которая печатает звездный прямоугольник размерами n×19.
'''
n = int(input())
for i in range(n):
    print('*' * 19)
