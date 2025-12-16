#1
#а
#sequence = "A B C X Y Z 1 2 3 + - * D E F"
#digits = set(ch for ch in sequence if ch.isdigit())
#ops = set(ch for ch in sequence if ch in "+-*/")
#letters_A_F = set(ch for ch in sequence if 'A' <= ch <= 'F')
#letters_X_Z = set(ch for ch in sequence if 'X' <= ch <= 'Z')
#print("Цифры:", digits)
#print("Знаки:", ops)
#print("A-F:", letters_A_F)
#print("X-Z:", letters_X_Z)
#б
#all_codes = set(range(1, 21))
#given_codes = {2, 5, 8, 12, 15, 18}
#missing = all_codes - given_codes
#print("Отсутствуют:", missing)
#2
#а
#user_input = "abc123+4-5*6"
#digits_set = set("0123456789")
#signs_set = set("+-*")
#digit_count = sum(1 for ch in user_input if ch in digits_set)
#sign_count = sum(1 for ch in user_input if ch in signs_set)
#print("Цифр:", digit_count)
#print("Знаков +,-,*:", sign_count)
#б
#list1 = [1, 2, 3, 4, 5]
#list2 = [4, 5, 6, 7, 8]
#common = set(list1) & set(list2)
#print("Общие элементы:", common)
#3
#а
#user_input = "Hello, world! How are you?"
#punctuation = set(".,!?;:-'\"")
#letters = set(ch for ch in user_input if 'a' <= ch <= 'z')
#punct_count = sum(1 for ch in user_input if ch in punctuation)
#print("Строчные латинские буквы:", letters)
#print("Количество знаков препинания:", punct_count)
#б
#A = {1, 2, 3}
#B = {1, 2, 3, 4, 5}
#is_subset = A.issubset(B)
#print("A подмножество B?", is_subset)
#4
#а
#s1 = "Привет мир"
#s2 = "Мир светел"
#s3 = "Светит солнце"
#letters1 = set(s1.lower().replace(" ", ""))
#letters2 = set(s2.lower().replace(" ", ""))
#letters3 = set(s3.lower().replace(" ", ""))
#common = letters1 & letters2 & letters3
#print("Общие буквы:", common)
#б
#uni1_subjects = {"Математика", "Физика", "Химия"}
#uni2_subjects = {"Математика", "Информатика", "Физика"}
#only_uni1 = uni1_subjects - uni2_subjects
#only_uni2 = uni2_subjects - uni1_subjects
#print("Только в универе 1:", only_uni1)
#print("Только в универе 2:", only_uni2)
#5
#а
#a, b, c = 123, 456, 789
#digits_a = set(str(a))
#digits_b = set(str(b))
#digits_c = set(str(c))
#all_digits = digits_a | digits_b | digits_c
#digit_vals = [int(d) for d in all_digits if d.isdigit()]
#max_digit = max(digit_vals)
#print(max_digit)
#б
#A = {1, 2, 3, 4}
#B = {3, 4, 5, 6}
#only_one = A ^ B  
#print(only_one)
#6
#а
#s = "abc12345def67890"
#unique_digits = set(ch for ch in s if ch.isdigit())
#print("Уникальные цифры:", unique_digits)
#print("Количество:", len(unique_digits))
#б
#purchases = {
#    "user1": {"яблоко", "банан", "молоко"},
#   "user2": {"банан", "хлеб", "сыр"},
#    "user3": {"молоко", "сыр", "яблоко"}
#}
#all_items = set()
#items_count = {}
#for items in purchases.values():
#    all_items.update(items)
#    for item in items:
#        items_count[item] = items_count.get(item, 0) + 1
#only_one_user = {item for item, count in items_count.items() if count == 1}
#print("Товары, купленные только одним пользователем:", only_one_user)
#7
#а
#s1 = "Привет мир"
#s2 = "Мир светел"
#s3 = "Светит солнце"
#letters1 = set(s1.lower().replace(" ", ""))
#letters2 = set(s2.lower().replace(" ", ""))
#letters3 = set(s3.lower().replace(" ", ""))
#unique_to_s1 = letters1 - letters2 - letters3
#unique_to_s2 = letters2 - letters1 - letters3
#unique_to_s3 = letters3 - letters1 - letters2
#all_unique = unique_to_s1 | unique_to_s2 | unique_to_s3
#print("Уникальные буквы в каждом предложении (объединённые):", all_unique)
#б
#A = {1, 2, 3}
#B = {4, 5, 6}
#are_disjoint = A.isdisjoint(B)
#print("Непересекающиеся?", are_disjoint)
#8
#а
#s1 = "abcde"
#s2 = "fghij"
#target = "acegi"
#available = set(s1) | set(s2)
#target_set = set(target)
#can_form = target_set.issubset(available)
#print("Можно составить?", can_form)
#б
#employees = {
#    "emp1": {"Python", "SQL", "Excel"},
#    "emp2": {"Python", "Java", "Excel"},
#    "emp3": {"SQL", "C++", "Excel"}
#}
#all_skills = {}
#for skills in employees.values():
#    for skill in skills:
#        all_skills[skill] = all_skills.get(skill, 0) + 1
#unique_skills = {skill for skill, count in all_skills.items() if count == 1}
#print("Навыки только у одного сотрудника:", unique_skills)
#9
#а
#text = "Привет, как дела? Эх, хорошая погода!"
#vowels = set("аеёиоуыэюя")
#found = set()
#for ch in text.lower():
#    if ch in vowels:
#        found.add(ch)
#sorted_vowels = sorted(found)
#print(sorted_vowels)
#б
#products = {
#    "prod1": {"электроника", "техника"},
#    "prod2": {"электроника", "компьютеры"},
#    "prod3": {"техника", "инструменты"}
#}
#category_count = {}
#for categories in products.values():
#    for cat in categories:
#        category_count[cat] = category_count.get(cat, 0) + 1
#single_product_cats = {cat for cat, count in category_count.items() if count == 1}
#print("Категории с одним продуктом:", single_product_cats)
#10
#а
#num = 1234554321
#digits_set = set(str(num))
#sorted_digits = sorted(digits_set)
#print(sorted_digits)
#б
#A = {1, 2, 3}
#B = {1, 2, 3, 4, 5}
#is_strict = A.issubset(B) and A != B
#print("A — строгое подмножество B?", is_strict)
#11
#а
#text = "Привет, мир! Как дела?"
#vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
#consonants = set("бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
#vowel_count = sum(1 for ch in text if ch in vowels)
#consonant_count = sum(1 for ch in text if ch in consonants)
#print("Гласных:", vowel_count)
#print("Согласных:", consonant_count)
#if vowel_count > consonant_count:
#    print("Гласных больше")
#else:
#    print("Согласных больше")
#б
#orders = {
#    "day1": {"яблоко", "банан", "молоко"},
#    "day2": {"банан", "хлеб", "сыр"},
#    "day3": {"молоко", "сыр", "яблоко"}
#}
#target_day = "day1"
#target_items = orders[target_day]
#items_other_days = set()
#for day, items in orders.items():
#    if day != target_day:
#        items_other_days.update(items)
#only_target_day = target_items - items_other_days
#print("Товары, заказанные только в", target_day, ":", only_target_day)    
#12
#а
#num = 12345
#all_digits = set("0123456789")
#num_digits = set(str(num))
#missing = sorted(all_digits - num_digits)
#print("Отсутствующие цифры:", missing)
#б
#A = {1, 2, 3, 4, 5}
#B = {2, 3, 4}
#is_superset = B.issubset(A)
#print("A — надмножество B?", is_superset)
#13
#а
#A = {1, 2, 3, 4, 5}
#B = {4, 5, 6, 7}
#A = A - B  # или A.difference_update(B)
#print(A)
#б
#purchases = {
#    "user1": {"яблоко", "банан"},
#    "user2": {"банан", "хлеб"},
#    "user3": {"молоко"}
#}
#all_items = set()
#for items in purchases.values():
#    all_items.update(items)
#print("Товары, купленные хотя бы одним:", all_items)
#14
#а
#text = "Привет, мир!"
#all_consonants = set("бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
#text_letters = set(text.lower())
#missing_consonants = sorted(all_consonants.intersection(set("бвгджзйклмнпрстфхцчшщ")) - text_letters)
#print("Согласные, не встречающиеся в тексте:", missing_consonants)
#б
#A = {1, 2, 3}
#B = {3, 2, 1}
#are_equal = A == B
#print("Множества равны?", are_equal)
#15
#а
#A = {1, 2, 3}
#B = {4, 5, 6}
#have_common = not A.isdisjoint(B)
#print("Есть общие элементы?", have_common)
#б
#uni1_subjects = {"Математика", "Физика", "Химия"}
#uni2_subjects = {"Математика", "Информатика", "Физика"}
#common = uni1_subjects & uni2_subjects
#print("Предметы, изучаемые в обоих университетах:", common)
