import numpy as np

def transpornation(matrix):
    a = np.transpose(matrix)
    print(a)

def addition(matrix1):
    lines = int(input("Кол-во строк: "))
    columns = int(input("Кол-во столбцов: "))
    matrix2 = np.zeros((lines, columns))
    for i in range(lines):
        for j in range(columns):
            matrix2[i][j] = float(input())
    print('Вторая матрица:\n', matrix2)
    print(matrix1 + matrix2)

def obrat(matrix):
    if lines == columns and np.linalg.det(matrix) != 0:
        print(np.linalg.inv(matrix))
    else:
        print('Обратную матрицу возможно высчитать тогда, когда количество строк матрицы равно количеству её столбцов и матрица невырожденная. (В. Е. Шапошников)')

def determinant(matrix):
    if lines == columns:
        print(np.linalg.det(matrix))
    else:
        print('Определитель матрицы возможно высчитать тогда, когда количество строк матрицы равно количеству её столбцов. (В. Е. Шапошников)')

def rank(matrix):
    print(int(np.linalg.matrix_rank(matrix)))

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        print(np.dot(matrix1, matrix2))
    else:
        print("Комментарий: умножение матриц возможно тогда, когда количество столбцов первой матрицы равно количеству строк второй матрицы.")


lines = int(input("Кол-во строк: "))
columns = int(input("Кол-во столбцов: "))

matrix = np.zeros((lines, columns))

for i in range(lines):
    for j in range(columns):
        matrix[i][j] = float(input())
print(matrix)

flag = True
n = 1

while flag == True:
    request = input("Запрос: ")
    if request == "определитель":
        if n%2==0:
            print("А Вы попробуйте упрОстить выражение, тут ведь нет ничего сложного! (В. Е. Шапошников)")
        determinant(matrix)
    if request == "ранг":
        if n%2==0:
            print("Смотрите, тут просто надо включить голову, а то у Вас одни Ыгреки (Ыгрики) в голове! (К. В. Логвинова)")
        rank(matrix)
     if request == "транспонировать":
        if n%2==0:
            print("Скорее всего, в порыве творческого мракобесия Вы совсем забыли, что волк - это не трава; но волк - ты ТРАВА! (Е. А. Лупанова)")
        transpornation(matrix)
    if request == "обратная матрица":
        if n%2==0:
            print("Вы ведь понимаете, что Вас никто ничему не научит, поэтому давайте подобные вещи по дефолту сводить к некой абстракции! (А. А. Дыдычкин)")
        obrat(matrix)
    if request == "умножение":
        if n%2==0:
            print("Ага, попался, маленький любитель вычисления матриц через Интернет, ну посмотрим, что ты покажешь на самостоятельной работе! (В. Е. Шапошников)")
        matrix_multiply(matrix1, matrix2)
    if request == "выход":
        flag = False
    n += 1
