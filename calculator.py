import numpy as np

def transpornation(matrix):
    a = np.transpose(matrix)
    print("\nРезультат:\n", a, "\n")
    return a

def addition(matrix1):
    lines = int(input("\nКол-во строк: "))
    columns = int(input("Кол-во столбцов: "))
    matrix2 = np.zeros((lines, columns))
    if len(matrix1[0]) == columns and len(matrix1) == lines:
        for i in range(lines):
            for j in range(columns):
                matrix2[i][j] = float(input())
        print('\nВторая матрица:\n', matrix2)
        print('\nРезультат:\n', matrix1 + matrix2, "\n")
        return matrix1 + matrix2
    print("\nОшибка: Сложение матриц возможно тогда, когда матрицы имеют одинаковую размерность. Введите матрицу заново")
    return addition(matrix1)

def obrat(matrix):
    if len(matrix) == len(matrix[0]) and np.linalg.det(matrix) != 0:
        print('\nРезультат:\n', np.linalg.inv(matrix))
        return np.linalg.inv(matrix)
    print('\nОшибка: Обратную матрицу возможно высчитать тогда, когда матрица квадратная и невырожденная.')
    return matrix

def determinant(matrix):
    if len(matrix) == len(matrix[0]):
        print("\nОпределитель равен: \n", round(np.linalg.det(matrix), 2), "\n")
    else:
        print('\nОшибка: Определитель матрицы возможно высчитать тогда, когда матрица квадратная.')

def rank(matrix):
    print("\nРанг равен: \n", int(np.linalg.matrix_rank(matrix)), "\n")

def matrix_multiply(matrix1):
    lines = int(input("\nКол-во строк: "))
    columns = int(input("Кол-во столбцов: "))
    matrix2 = np.zeros((lines, columns))
    if len(matrix1[0]) == lines:
        for i in range(lines):
            for j in range(columns):
                matrix2[i][j] = float(input())
        print('\nВторая матрица:\n', matrix2)
        print('\nРезультат:\n', np.dot(matrix1, matrix2), "\n")
        return np.dot(matrix1, matrix2)
    print("\nОшибка: Умножение матриц возможно тогда, когда кол-во столбцов 1-й матрицы равно кол-ву строк 2-й. Введите матрицу заново")
    return matrix_multiply(matrix1)

print("Здравствуй, дорогой друг, ты находишься в матричном калькуляторе имени Шапошникова. Данный калькулятор характеризуется лёгкостью, доступностью и неожиданными сюрпризами. Используй весь функционал, чтобы найти все пасхалки (их всего 6)!\n")
print("Небольшое введение по вводу данных:")
print("Сначала введите количество строк и столбцов матрицы. Затем построчно вводите элементы матрицы. Под каждый элемент матрицы закладывается одна строка консоли. Все элементы матрицы обязаны быть действительными числами! Запросами операций над матрицами являются числа, указанные в инструктаже. После получения результата Вы продолжаете работать с той матрицей, которая у Вас находится в последнем результате.\n")
print("Пример создания матрицы:\nКол-во строк: 2\nКол-во столбцов: 2\n1\n2\n3\n4\n\nРезультат:\n\n[[1. 2.]\n [3. 4.]]\n\n\n")
print("Введите вашу первую матрицу!\n")
lines = int(input("Кол-во строк: "))
columns = int(input("Кол-во столбцов: "))

matrix = np.zeros((lines, columns))

for i in range(lines):
    for j in range(columns):
        matrix[i][j] = float(input())
print("\nВаша первая матрица:\n")
print(matrix, "\n")

flag = True
n = 1

print("Инструкция:")
print("	1 – сложение матриц;")
print("	2 – умножение матриц;")
print("	3 – нахождение определителя;")
print("	4 – транспонирование;")
print("	5 – нахождение обратной матрицы;")
print("	6 – нахождение ранга;")
print("	0 – выход.\n")

while flag == True:
    request = input("Запрос: ")
    if request == "3":
        if n%2==0:
            print("\nА Вы попробуйте упрОстить выражение, тут ведь нет ничего сложного! (В. Е. Шапошников)")
        determinant(matrix)
    elif request == "6":
        if n%2==0:
            print("\nСмотрите, тут просто надо включить голову, а то у Вас одни Ыгреки (Ыгрики) в голове! (К. В. Логвинова)")
        rank(matrix)
    elif request == "4":
        if n%2==0:
            print("\nСкорее всего, в порыве творческого мракобесия Вы совсем забыли, что волк - это не трава; но волк - ты ТРАВА! (Е. А. Лупанова)")
        matrix = transpornation(matrix)
    elif request == "5":
        if n%2==0:
            print("\nВы ведь понимаете, что Вас никто ничему не научит, поэтому давайте подобные вещи по дефолту сводить к некой абстракции! (А. А. Дыдычкин)")
        matrix = obrat(matrix)
    elif request == "2":
        if n%2==0:
            print("\nАга, попался, маленький любитель вычисления матриц через Интернет, ну посмотрим, что ты покажешь на самостоятельной работе! (В. Е. Шапошников)")
        matrix = matrix_multiply(matrix)
    elif request == "1":
        if n%2==0:
            print("\nЗнаете, в этом выражении нет опечатки, я хотел проверить вас на внимательность! (В.Е.Шапошников)")
        matrix = addition(matrix)
    elif request == "0":
        flag = False
    else:
        print("\nВведите одно из чисел, указанных в инструктаже!\n")
    n += 1
print("\nСпасибо за использование калькулятора! Надеюсь Вам понравилось)")
