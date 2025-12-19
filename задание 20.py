#1
product = 1
with open("f.txt", "r") as file:
    for line in file:
        number = float(line.strip())
        product *= number
print("Произведение:", product)
#2
positives = []
negatives = []

with open("f.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number > 0:
            positives.append(str(number) + "\n")
        else:
            negatives.append(str(number) + "\n")
with open("g.txt", "w") as file:
    file.writelines(positives + negatives)
#3
with open("f.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

squares = []
for num in numbers:
    root = int(num ** 0.5)
    if root * root == num:  
        squares.append(str(num) + "\n")

with open("g.txt", "w") as file:
    file.writelines(squares)
#4
values = []
with open("f.txt", "r") as file:
    for line in file:
        values.append(float(line.strip()))
max_val = max(values)
min_val = min(values)
sum_extremes = max_val + min_val
print("Сумма наибольшего и наименьшего:", sum_extremes)
#5
years = []
with open("dates.txt", "r") as file:
    for line in file:
        parts = line.strip().split()  
        year = int(parts[2](https://otvet.mail.ru/question/220482021))  
        years.append(year)

earliest_year = min(years)
print("Год с наименьшим номером:", earliest_year)
#6
even_count = 0
with open("f.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even_count += 1
print("Количество чётных чисел:", even_count)
#7

with open("f.txt", "r") as file:
    first_line = file.readline().strip()
first_two = first_line[:2]  
if first_two.isdigit():  
    number = int(first_two)
    if number % 2 == 0:
        print("Число чётное")
    else:
        print("Число нечётное")
else:
    print("Первые два символа не являются цифрами")
#8
with open("f.txt", "r") as file_f:
    lines = file_f.readlines()
even_numbers = []
for line in lines:
    number = int(line.strip())
    if number % 2 == 0:  
        even_numbers.append(str(number) + "\n")

with open("g.txt", "w") as file_g:
    file_g.writelines(even_numbers)
#9
with open("f.txt", "r") as file:
    lines = file.readlines()
max_modulus = float('-inf')  
for i in range(1, len(lines), 2):  
    number = float(lines[i].strip())
    modulus = abs(number)  
    if modulus > max_modulus:
        max_modulus = modulus
print("Наибольшее значение модуля:", max_modulus)
#10
with open("dates.txt", "r") as file:
    lines = file.readlines()
spring_dates = []
for line in lines:
    parts = line.strip().split()  
    month = int(parts[1](https://PythonRu.com/osnovy/fajly-v-python-vvod-vyvod))  
    if month in [3, 4, 5]:  
        spring_dates.append(line)
with open("spring_dates.txt", "w") as file:
    file.writelines(spring_dates)
#11
with open("f.txt", "r") as file_f:
    lines = file_f.readlines()
suitable_numbers = []
for line in lines:
    number = int(line.strip())
    if number % 3 == 0 and number % 7 != 0:  
        suitable_numbers.append(str(number) + "\n")
with open("g.txt", "w") as file_g:
    file_g.writelines(suitable_numbers)
#12
with open("f.txt", "r") as file:
    lines = file.readlines()
min_value = float('inf')  
for i in range(0, len(lines), 2):  
    number = float(lines[i].strip())
    if number < min_value:
        min_value = number
print("Наименьшее значение:", min_value)
#13
with open("f.txt", "r") as file_f:
    lines = file_f.readlines()
even_numbers = []
odd_numbers = []
for line in lines:
    number = int(line.strip())
    if number % 2 == 0:
        even_numbers.append(str(number) + "\n")
    else:
        odd_numbers.append(str(number) + "\n")
with open("g.txt", "w") as file_g:
    file_g.writelines(even_numbers)
with open("h.txt", "w") as file_h:
    file_h.writelines(odd_numbers)
#14
with open("f.txt", "r") as file_f:
    lines = file_f.readlines()
numbers = [int(line.strip()) for line in lines]
result = []
for i in range(len(numbers)):
    if not result:  
        result.append(str(numbers[i]) + "\n")
    else:
        last_sign = result[-1].strip()  
        current_sign = "+" if numbers[i] > 0 else "-"
        if last_sign != current_sign:  
            result.append(str(numbers[i]) + "\n")
with open("g.txt", "w") as file_g:
    file_g.writelines(result)
