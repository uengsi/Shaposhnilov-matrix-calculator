import numpy as np

def transpornation(matrix):
    a = np.transpose(matrix)
    print(a)
    return a

def addition(matrix1):
    lines = int(input("Кол-во строк: "))
    columns = int(input("Кол-во столбцов: "))
    matrix2 = np.zeros((lines, columns))
    if len(matrix1[0]) == columns and len(matrix1) == lines:
        for i in range(lines):
            for j in range(columns):
                matrix2[i][j] = float(input())
        print('Вторая матрица:\n', matrix2)
        print('Результат:\n', matrix1 + matrix2)
        return matrix1 + matrix2
    print("Ошибка: Сложение матриц возможно тогда, когда матрицы имеют одинаковую размерность. Введите матрицу заново")
    addition(matrix1)

def obrat(matrix):
    if len(matrix) == len(matrix[0]) and np.linalg.det(matrix) != 0:
        print('Результат:\n', np.linalg.inv(matrix))
        return np.linalg.inv(matrix)
    print('Ошибка: Обратную матрицу возможно высчитать тогда, когда матрица квадратная и невырожденная.')
    return matrix

def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        print(round(np.linalg.det(matrix), 2))
    else:
        print('Ошибка: Определитель матрицы возможно высчитать тогда, когда матрица квадратная.')

def rank(matrix):
    print(int(np.linalg.matrix_rank(matrix)))

def matrix_multiply(matrix1):
    lines = int(input("Кол-во строк: "))
    columns = int(input("Кол-во столбцов: "))
    matrix2 = np.zeros((lines, columns))
    if len(matrix1[0]) == lines:
        for i in range(lines):
            for j in range(columns):
                matrix2[i][j] = float(input())
        print('Вторая матрица:\n', matrix2)
        print('Результат:\n', np.dot(matrix1, matrix2))
        return np.dot(matrix1, matrix2)
    print("Ошибка: Умножение матриц возможно тогда, когда кол-во столбцов 1-й матрицы равно кол-ву строк 2-й. Введите матрицу заново")
    matrix_multiply(matrix1)

lines = int(input("Кол-во строк: "))
columns = int(input("Кол-во столбцов: "))

matrix = np.zeros((lines, columns))

for i in range(lines):
    for j in range(columns):
        matrix[i][j] = float(input())
print(matrix)

flag = True
n = 1

print("Инструкция:")
print("	1 – сложение матриц;")
print("	2 – умножение матриц;")
print("	3 – нахождение определителя;")
print("	4 – транспонирование;")
print("	5 – нахождение обратной матрицы;")
print("	6 – нахождение ранга;")
print("	0 – выход.")

while flag == True:
    request = input("Запрос: ")
    if request == "3":
        if n%2==0:
            print("А Вы попробуйте упрОстить выражение, тут ведь нет ничего сложного! (В. Е. Шапошников)")
        determinant(matrix)
    if request == "6":
        if n%2==0:
            print("Смотрите, тут просто надо включить голову, а то у Вас одни Ыгреки (Ыгрики) в голове! (К. В. Логвинова)")
        rank(matrix)
    if request == "4":
        if n%2==0:
            print("Скорее всего, в порыве творческого мракобесия Вы совсем забыли, что волк - это не трава; но волк - ты ТРАВА! (Е. А. Лупанова)")
        matrix = transpornation(matrix)
    if request == "5":
        if n%2==0:
            print("Вы ведь понимаете, что Вас никто ничему не научит, поэтому давайте подобные вещи по дефолту сводить к некой абстракции! (А. А. Дыдычкин)")
        matrix = obrat(matrix)
    if request == "2":
        if n%2==0:
            print("Ага, попался, маленький любитель вычисления матриц через Интернет, ну посмотрим, что ты покажешь на самостоятельной работе! (В. Е. Шапошников)")
        matrix = matrix_multiply(matrix)
    if request == "1":
        if n%2==0:
            print("Знаете, в этом выражении нет опечатки, я хотел проверить вас на внимательность! (В.Е.Шапошников)")
        matrix = addition(matrix)
    if request == "0":
        flag = False
    n += 1
