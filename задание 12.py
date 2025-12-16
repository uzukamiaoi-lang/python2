#1
#a
#strings = ("Привет", "МИР", "Test", "ПРИВЕТ")
#tup = tuple(strings)
#print(tup)
#б
#tup = ('Привет', 'МИР', 'Test', 'ПРИВЕТ')
#d = {}
#for s in tup:
#    upper_count = sum(1 for ch in s if ch.isupper())
#    d[s] = upper_count
#print(d)
#2
#а
#tup = ("строка", 42, [1,2,3], 3.14, {"a":1}, (5,6))
#print(tup)
#б
#list_of_tuples = [("abc", 1, [2]), ("def", 3, []), (4, "ghi", 5.5)]
#str_list = []
#int_list = []
#float_list = []
#list_list = []
#other_list = []

#for t in list_of_tuples:
#    for item in t:
#        if isinstance(item, str):
#            str_list.append(item)
#        elif isinstance(item, int):
#            int_list.append(item)
#        elif isinstance(item, float):
#            float_list.append(item)
#        elif isinstance(item, list):
#            list_list.append(item)
#        else:
#            other_list.append(item)
#print("Строки:", str_list)
#print("Целые:", int_list)
#print("Вещественные:", float_list)
#print("Списки:", list_list)
#print("Остальное:", other_list)
#3
#а
#numbers = (10, 20, 30, 40, 50)
#print(numbers[0])
#б
#numbers = (10, 20, 30, 40, 50, 60, 70)
#reversed_tuple = tuple(reversed(numbers))
#filtered_tuple = tuple(x for x in reversed_tuple if x % 3 != 0)
#print(filtered_tuple)
#4
#а
#tup = ("Иван", 25, "Москва")
#name, age, city = tup
#print("Имя:", name)
#print("Возраст:", age)
#print("Город:", city)
#б
#list_of_tuples = [("a", 3), ("b", 1), ("c", 2)]
#d = dict(list_of_tuples)
#sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
#print(sorted_d)
#5
#а
#tup = (1, 2, 3)
#new_element = 4
#new_tup = tup + (new_element,)
#print(new_tup)
#б
#tup = ("abc", "мир", "123")
#formatted = tuple(s[::-1] for s in tup)
#print(formatted)
#6
#а
#tup = ("яблоко", "банан", "вишня")
#separator = "-"
#result = separator.join(tup)
#print(result)
#б
#list_of_tuples = [("a", 1, 5), ("b", "текст"), (3, 4, 9.5)]
#new_value = 100
#new_list = []
#for t in list_of_tuples:
#    if isinstance(t[-1], (int, float)):
#        t = t[:-1] + (new_value,)
#    new_list.append(t)
#print(new_list)
#7
#а
#tup = (10, 20, 30, 40, 50, 60, 70, 80, 90)
#fourth_from_start = tup[3]
#fourth_from_end = tup[-4]
#print("4-й с начала:", fourth_from_start)
#print("4-й с конца:", fourth_from_end)
#б
#import random
#list_of_tuples = [(1,2), (), (3,), (), (5,6)]
#new_list = []
#for t in list_of_tuples:
#    if t == ():
#        new_list.append((random.randint(1, 10),))
#    else:
#        new_list.append(t)
#print(new_list)
#8
#а
#dict1 = {"name": "Иван", "age": 25}
#dict2 = {"name": "Мария", "age": 30}
#tup = (dict1, dict2)
#print(tup)
#б
#tup = (
#    {"name": "A", "value": 3.5},
#    {"name": "B", "value": 1.2},
#    {"name": "C", "value": 4.0}
#)
#sorted_tup = tuple(sorted(tup, key=lambda x: x["value"], reverse=True))
#print(sorted_tup)
#9
#а
#tup = (1, 2, 3, 2, 4, 5, 3, 6)
#repeated = []
#seen = set()
#for x in tup:
#    if x in seen and x not in repeated:
#        repeated.append(x)
#    seen.add(x)
#print(repeated)
#б
#lst = [1, 2, 3, "hello", (4,5), 6, 7]
#count = 0
#total = 0
#for item in lst:
#    if isinstance(item, tuple):
#        break
#    count += 1
#    if isinstance(item, int):
#        total += item
#print("Количество элементов до кортежа:", count)
#print("Сумма чисел до кортежа:", total)
#10
#а
#tup = (1, 2, 3, 2, 4, 2, 5)
#element = 2
#if element in tup:
#    count = tup.count(element)
#    print("Найдено", count, "раз(а)")
#else:
#    print("Не найдено")
#б
#lst = ["a", "b", "a", "c", "b", "d"]
#tup = tuple(set(lst))
#print(tup)
#11
#а
#lst = [10, 20, 30, 40]
#tup = tuple(lst)
#print(tup)
#б
#tup = (1, 2, 3, 4, 5, 6)
#product = 1
#for x in tup:
#    if x % 2 == 0:
#        product *= x
#print(product)
#12
#а
#tup = (1, 2, 3, 4, 5)
#element_to_remove = 3
#new_tup = tuple(x for x in tup if x != element_to_remove)
#print(new_tup)
#б
#tup_of_tuples = ((1, 6, 7), (5, 10, 15), (2, 3, 4))
#averages = []
#for inner_tup in tup_of_tuples:
#    nums = [x for x in inner_tup if isinstance(x, (int, float)) and x > 5]
#    if nums:
#        avg = sum(nums) / len(nums)
#        averages.append(round(avg, 2))
#    else:
#        averages.append(0)
#print(averages)
#13
#а
#tup = (1, "a", 2, "b", 3, "c", 4)
#start = 1
#end = 6
#sliced = tup[start:end]
#filtered = tuple(x for x in sliced if not isinstance(x, str))
#print(filtered)
#б
#tup = ("10", "20", "30")
#new_tup = tuple(int(x) for x in tup)
#print(new_tup)
#14
#а
#tup = (10, "a", 20, "b", 30, 40)
#element = 30
#index = -1
#count = 0
#for i, x in enumerate(tup):
#    if isinstance(x, (int, float)):
#       count += 1
#        if x == element:
#            index = count  # порядковый номер среди чисел
#            break
#if index != -1:
#    print("Порядковый номер среди чисел:", index)
#else:
#    print("Не найден")
#б
#tup = (12, 7, 9, 15, 4, 18)
#filtered = [str(x) for x in tup if x % 3 == 0]
#if filtered:
#    big_number = int(''.join(filtered))
#else:
#    big_number = 0
#print(big_number)
#15
#а
#tup = ("a", 1, "b", 2, "c", "d")
#count_str = sum(1 for x in tup if isinstance(x, str))
#print("Длина (только строки):", count_str)
#б
#tup_of_tuples = ((1,2), (3,4), (1,5), (6,7))
#element = 1
#count = 0
#for inner_tup in tup_of_tuples:
#    count += inner_tup.count(element)
#print("Количество вхождений:", count)
