import numpy as np

def determinant(matrix):
    if lines == columns:
        print(np.linalg.det(matrix))
    else:
        print('Определитель матрицы возможно высчитать тогда, когда количество строк матрицы равно количеству её столбцов. (В. Е. Шапошников)')

def rank(matrix):
    print(int(np.linalg.matrix_rank(matrix)))

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
    if request == "выход":
        flag = False
    n += 1