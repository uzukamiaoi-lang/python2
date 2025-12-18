#1
def midpoint(x1, y1, x2, y2):
    x_mid = (x1 + x2) / 2
    y_mid = (y1 + y2) / 2
    return (x_mid, y_mid)
def can_form_triangle(a, b, c):    
    return (a + b > c) and (a + c > b) and (b + c > a)
def triangle_area(a, b, c):
    if not can_form_triangle(a, b, c):
        return None  
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area
#Пример использования :
import geometry_module
# Пример 1: вычисление середины отрезка
x1, y1 = 1, 2
x2, y2 = 5, 6
mid = geometry_module.midpoint(x1, y1, x2, y2)
print(f"Середина отрезка: {mid}")
# Пример 2: проверка возможности построения треугольника
a, b, c = 3, 4, 5
if geometry_module.can_form_triangle(a, b, c):
    print("Треугольник можно построить!")
else:
    print("Треугольник построить нельзя!")
# Пример 3: вычисление площади треугольника
area = geometry_module.triangle_area(a, b, c)
if area is not None:
    print(f"Площадь треугольника: {area}")
else:
    print("Невозможно вычислить площадь — треугольник не существует")
#2
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def perimeter(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)  # сторона AB
    b = distance(x2, y2, x3, y3)  # сторона BC
    c = distance(x3, y3, x1, y1)  # сторона CA
    return a + b + c
def triangle_area_points(x1, y1, x2, y2, x3, y3):    
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area
#Пример использования (main2.py):
import triangle_points_module
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 0, 3
d1 = triangle_points_module.distance(x1, y1, x2, y2)
d2 = triangle_points_module.distance(x2, y2, x3, y3)
d3 = triangle_points_module.distance(x3, y3, x1, y1)
print(f"Расстояние между точками 1 и 2: {d1}")
print(f"Расстояние между точками 2 и 3: {d2}")
print(f"Расстояние между точками 3 и 1: {d3}")
perim = triangle_points_module.perimeter(x1, y1, x2, y2, x3, y3)
print(f"Периметр треугольника: {perim}")
area = triangle_points_module.triangle_area_points(x1, y1, x2, y2, x3, y3)
print(f"Площадь треугольника: {area}")
#3
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def reduce_fraction(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return (numerator // divisor, denominator // divisor)
def fraction_to_decimal(numerator, denominator):
    return numerator / denominator
#Пример использования:
import fraction_module
numerator = 8
denominator = 12
gcd_result = fraction_module.gcd(numerator, denominator)
print(f"НОД({numerator}, {denominator}) = {gcd_result}")
reduced = fraction_module.reduce_fraction(numerator, denominator)
print(f"Несократимая дробь: {reduced[0]}/{reduced[1](https://ru.onlinemschool.com/math/library/analytic_geometry/points_center/)}")
decimal = fraction_module.fraction_to_decimal(numerator, denominator)
print(f"Десятичная форма дроби: {decimal}")
#4
def build_line_equation(x1, y1, x2, y2):
    if x2 - x1 == 0:  
        return "x = " + str(x1)
    k = (y2 - y1) / (x2 - x1)
    
    b = y1 - k * x1
    return f"y = {k}x + {b}"
def are_lines_parallel(k1, b1, k2, b2):
    return k1 == k2
def is_point_on_line(x, y, k, b):
    return y == k * x + b
#Пример использования:
import line_module
x1, y1 = 1, 2
x2, y2 = 3, 6
equation = line_module.build_line_equation(x1, y1, x2, y2)
print("Уравнение прямой:", equation)
k1, b1 = 2, 3
k2, b2 = 2, -1
if line_module.are_lines_parallel(k1, b1, k2, b2):
    print("Прямые параллельны!")
else:
    print("Прямые не параллельны.")
x, y = 2, 7
k, b = 2, 3
if line_module.is_point_on_line(x, y, k, b):
    print(f"Точка ({x}, {y}) принадлежит прямой.")
else:
    print(f"Точка ({x}, {y}) не принадлежит прямой.")
#5
import math
def circle_area(radius):
    return math.pi * radius ** 2
def circle_circumference(radius):
    return 2 * math.pi * radius
def sector_area(radius, angle):
    return (angle / 360) * math.pi * radius ** 2
def inscribed_square_perimeter(radius):
    side = radius * math.sqrt(2)  
    return 4 * side  
#Пример использования:
import geometry_module

radius = 5
angle = 60  
print("Площадь круга:", geometry_module.circle_area(radius))
print("Длина окружности:", geometry_module.circle_circumference(radius))
print("Площадь сектора:", geometry_module.sector_area(radius, angle))
print("Периметр вписанного квадрата:", geometry_module.inscribed_square_perimeter(radius))
#6
def remove_char(string, char):
    result = ""
    for symbol in string:
        if symbol != char:
            result += symbol
    return result
def replace_char(string, old_char, new_char):
    result = ""
    for symbol in string:
        if symbol == old_char:
            result += new_char
        else:
            result += symbol
    return result
def count_char(string, char):
    count = 0
    for symbol in string:
        if symbol == char:
            count += 1
    return count
#Пример использования:
import string_module
text = "Hello, World!"
char_to_remove = "l"
char_to_replace = "o"
new_char = "0"
char_to_count = "l"

print("Исходная строка:", text)
print("Строка после удаления символа '{}':".format(char_to_remove),
      string_module.remove_char(text, char_to_remove))
print("Строка после замены '{}' на '{}':".format(char_to_replace, new_char),
      string_module.replace_char(text, char_to_replace, new_char))
print("Количество символов '{}' в строке:".format(char_to_count),
      string_module.count_char(text, char_to_count))
#7
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Функция для ввода матрицы (пользователь вводит строки через ввод)
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите элемент [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

# Функция для сложения двух матриц одинакового размера
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Матрицы разного размера, сложение невозможно!"
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Функция для умножения двух матриц
def multiply_matrices(matrix1, matrix2):
    # Проверяем, что количество столбцов первой матрицы равно количеству строк второй
    if len(matrix1[0]) != len(matrix2):
        return "Умножение невозможно: размеры матриц не согласованы!"
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Функция для построения транспонированной матрицы
def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):  # по столбцам исходной матрицы
        row = []
        for i in range(len(matrix)):  # по строкам исходной матрицы
            row.append(matrix[i][j])
        result.append(row)
    return result
#Пример использования:
import matrix_module

# Создаём две матрицы 2x2
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("Матрица 1:")
matrix_module.print_matrix(matrix1)

print("\nМатрица 2:")
matrix_module.print_matrix(matrix2)

# Складываем матрицы
sum_matrix = matrix_module.add_matrices(matrix1, matrix2)
print("\nСумма матриц:")
matrix_module.print_matrix(sum_matrix)

# Умножаем матрицы
mult_matrix = matrix_module.multiply_matrices(matrix1, matrix2)
print("\nПроизведение матриц:")
matrix_module.print_matrix(mult_matrix)

# Транспонируем первую матрицу
transposed = matrix_module.transpose_matrix(matrix1)
print("\nТранспонированная матрица 1:")
matrix_module.print_matrix(transposed)
#8
def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return "Векторы разной длины, сложение невозможно!"
    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] + vector2[i])
    return result

# Функция для умножения вектора на число
def multiply_vector_by_number(vector, number):
    result = []
    for element in vector:
        result.append(element * number)
    return result

# Функция для поиска минимального и максимального значений вектора
def find_min_max(vector):
    min_value = vector[0]
    max_value = vector[0]
    for element in vector:
        if element < min_value:
            min_value = element
        if element > max_value:
            max_value = element
    return min_value, max_value
#Пример использования (main_vector.py):
import vector_module
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
number = 3
print("Вектор 1:", vector1)
print("Вектор 2:", vector2)
sum_vector = vector_module.add_vectors(vector1, vector2)
print("Сумма векторов:", sum_vector)
mult_vector = vector_module.multiply_vector_by_number(vector1, number)
print("Вектор, умноженный на", number, ":", mult_vector)
min_val, max_val = vector_module.find_min_max(vector1)
print("Минимум в векторе 1:", min_val)
print("Максимум в векторе 1:", max_val)   
#9
def remove_digits_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    # Удаляем все цифры
    new_content = ''.join([char for char in content if not char.isdigit()])
    with open(filename, 'w') as file:
        file.write(new_content)
def count_characters(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return len(content)
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)
#Пример использования:
import file_module
filename = 'example.txt'
with open(filename, 'w') as file:
    file.write("Привет123!\nЭто456тест789.\nКонец0.")
print("Исходный файл:", filename)
file_module.remove_digits_from_file(filename)
print("Цифры удалены.")
char_count = file_module.count_characters(filename)
print("Количество символов в файле:", char_count)
line_count = file_module.count_lines(filename)
print("Количество строк в файле:", line_count)
#10
#11
def power_fraction(P, Q, N):
    P_result = P ** N  # числитель в степени N
    Q_result = Q ** N  # знаменатель в степени N
    return P_result, Q_result  # возвращаем новую дробь (числитель, знаменатель)

# Функция для проверки равенства двух дробей P1/Q1 и P2/Q2
def equal_fractions(P1, Q1, P2, Q2):
    return P1 * Q2 == P2 * Q1  # дроби равны, если P1*Q2 = P2*Q1

# Функция для проверки, что первая дробь больше второй
def greater_fraction(P1, Q1, P2, Q2):
    return P1 * Q2 > P2 * Q1  # первая дробь больше, если P1*Q2 > P2*Q1

# Функция для проверки, что первая дробь меньше второй
def less_fraction(P1, Q1, P2, Q2):
    return P1 * Q2 < P2 * Q1
#Пример использования (main_fraction.py):
import fraction_module

# Пример дроби 2/3, возводим в степень 2
P, Q = 2, 3
N = 2
result_P, result_Q = fraction_module.power_fraction(P, Q, N)
print(f"({P}/{Q})^{N} = {result_P}/{result_Q}")  # Выведет: (2/3)^2 = 4/9

# Сравниваем дроби 3/4 и 2/3
P1, Q1 = 3, 4
P2, Q2 = 2, 3

if fraction_module.equal_fractions(P1, Q1, P2, Q2):
    print("Дроби равны")
elif fraction_module.greater_fraction(P1, Q1, P2, Q2):
    print(f"{P1}/{Q1} больше {P2}/{Q2}")  # Выведет: 3/4 больше 2/3
else:
    print(f"{P1}/{Q1} меньше {P2}/{Q2}")
#12
def subtract_vectors(v1, v2):
    return [v1[0] - v2[0], v1[1](https://dspace.www1.vlsu.ru/bitstream/123456789/11269/1/02673.pdf) - v2[1](https://dspace.www1.vlsu.ru/bitstream/123456789/11269/1/02673.pdf)]  # вычитаем координаты по отдельности

# Функция для скалярного произведения векторов
def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1](https://dspace.www1.vlsu.ru/bitstream/123456789/11269/1/02673.pdf) * v2[1](https://dspace.www1.vlsu.ru/bitstream/123456789/11269/1/02673.pdf)  # v1x*v2x + v1y*v2y

# Функция для вычисления длины вектора
def vector_length(v):
    return (v[0]**2 + v[1](https://dspace.www1.vlsu.ru/bitstream/123456789/11269/1/02673.pdf)**2) ** 0.5  # √(x² + y²)

import vector_module

# Пример векторов: v1 = [3, 4], v2 = [1, 2]
v1 = [3, 4]
v2 = [1, 2]

# Вычитаем векторы
v_diff = vector_module.subtract_vectors(v1, v2)
print(f"v1 - v2 = {v_diff}")  # Выведет: v1 - v2 = [2, 2]

# Скалярное произведение
dot = vector_module.dot_product(v1, v2)
print(f"Скалярное произведение v1 и v2 = {dot}")  # Выведет: 11

# Длина вектора v1
length = vector_module.vector_length(v1)
print(f"Длина вектора v1 = {length}")
#13
#14
def find_min_element(matrix):
    min_element = matrix[0][0]  # предполагаем, что первый элемент — минимальный
    for row in matrix:
        for element in row:
            if element < min_element:
                min_element = element
    return min_element

# Функция для поиска максимального элемента матрицы
def find_max_element(matrix):
    max_element = matrix[0][0]  # предполагаем, что первый элемент — максимальный
    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element

# Функция для вычисления суммы всех элементов матрицы
def sum_all_elements(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum

# Функция для вычисления суммы элементов заданной строки матрицы
def sum_row_elements(matrix, row_index):
    if row_index >= len(matrix) or row_index < 0:
        return "Ошибка: индекс строки выходит за пределы матрицы."
    row_sum = 0
    for element in matrix[row_index]:
        row_sum += element
    return row_sum
#Пример использования (main_matrix.py):
import matrix_module

# Создаём матрицу 3x3
matrix = [
    [1, 5, 3],
    [4, 2, 8],
    [7, 9, 6]
]

print("Матрица:")
for row in matrix:
    print(row)

# Ищем минимальный элемент
min_elem = matrix_module.find_min_element(matrix)
print(f"Минимальный элемент: {min_elem}")

# Ищем максимальный элемент
max_elem = matrix_module.find_max_element(matrix)
print(f"Максимальный элемент: {max_elem}")

# Вычисляем сумму всех элементов
total_sum = matrix_module.sum_all_elements(matrix)
print(f"Сумма всех элементов: {total_sum}")

# Вычисляем сумму элементов второй строки (индекс 1)
row_sum = matrix_module.sum_row_elements(matrix, 1)
print(f"Сумма элементов второй строки: {row_sum}")
#15
def add_fractions(P1, Q1, P2, Q2):
    # Находим общий знаменатель (Q1 * Q2)
    common_denominator = Q1 * Q2
    # Приводим дроби к общему знаменателю и складываем
    numerator = P1 * Q2 + P2 * Q1
    return numerator, common_denominator

# Функция для вычитания дробей P1/Q1 - P2/Q2
def subtract_fractions(P1, Q1, P2, Q2):
    # Находим общий знаменатель (Q1 * Q2)
    common_denominator = Q1 * Q2
    # Приводим дроби к общему знаменателю и вычитаем
    numerator = P1 * Q2 - P2 * Q1
    return numerator, common_denominator

# Функция для умножения дробей P1/Q1 * P2/Q2
def multiply_fractions(P1, Q1, P2, Q2):
    # Перемножаем числители и знаменатели
    numerator = P1 * P2
    denominator = Q1 * Q2
    return numerator, denominator
#Пример использования (main_fraction.py):
import fraction_module
P1, Q1 = 1, 2  
P2, Q2 = 3, 4  
sum_P, sum_Q = fraction_module.add_fractions(P1, Q1, P2, Q2)
print(f"{P1}/{Q1} + {P2}/{Q2} = {sum_P}/{sum_Q}")
diff_P, diff_Q = fraction_module.subtract_fractions(P1, Q1, P2, Q2)
print(f"{P1}/{Q1} - {P2}/{Q2} = {diff_P}/{diff_Q}")
prod_P, prod_Q = fraction_module.multiply_fractions(P1, Q1, P2, Q2)
print(f"{P1}/{Q1} * {P2}/{Q2} = {prod_P}/{prod_Q}")
