#1
# а)
print(full_name('Иван', 'Петров'))  
print(full_name('Мария', 'Сидорова', middle_name='Алексеевна'))  
# б)
def transform_list(numbers, transform_function=None):
    if transform_function is None:
        return numbers.copy()  
    else:
        result = []
        for num in numbers:
            result.append(transform_function(num))  
        return result
print(transform_list([1, 2, 3]))  
print(transform_list([1, 2, 3], transform_function=lambda x: x * 2))  # [2, 4, 6]
# в)
def sum_positive_numbers(*args):
    total = 0
    for num in args:
        if num > 0:
            total += num  
    return total
print(sum_positive_numbers(1, -2, 3, -4, 5))  
print(sum_positive_numbers(-1, -2, -3)) 
# г)
def common_keys(**kwargs):
    if not kwargs:  
        return {}    
    first_dict = list(kwargs.values())[0]
    common = {}  
    for key in first_dict:        
        if all(key in d for d in kwargs.values()):
            
            common[key] = first_dict[key]
    return common
print(common_keys(dict1={'a': 1, 'b': 2}, dict2={'b': 2, 'c': 3}))  
print(common_keys(dict1={'x': 5, 'y': 6}, dict2={'y': 6, 'z': 7}, dict3={'y': 6, 'w': 8}))  

#2
# а)
def sort_numbers(numbers, reverse_order=False):
    return sorted(numbers, reverse=reverse_order)
print(sort_numbers([4, 2, 5, 1, 3]))  
print(sort_numbers([4, 2, 5, 1, 3], reverse_order=True)) 
# б)
def uppercase_text(text, separator=' '):
    words = text.split(separator)
    upper_words = [word.upper() for word in words]
    return separator.join(upper_words)
print(uppercase_text('hello world'))  
print(uppercase_text('python,java,c++', separator=',')) 
# в)
def multiply_all(*args):
    if not args:  
        return 1  
    product = 1
    for num in args:
        product *= num
    return product
print(multiply_all(1, 2, 3, 4))  
print(multiply_all(5, 10))  
# г)
def filter_strings(strings, **criteria):
    result = []
    for string in strings:
        meets_criteria = True
        if 'min_length' in criteria:
            if len(string) < criteria['min_length']:
                meets_criteria = False
        if 'starts_with' in criteria:
            if not string.startswith(criteria['starts_with']):
                meets_criteria = False
        if 'ends_with' in criteria:
            if not string.endswith(criteria['ends_with']):
                meets_criteria = False
        if meets_criteria:
            result.append(string)
    return result
print(filter_strings(['яблоко', 'вишня', 'киви'], min_length=6))  
print(filter_strings(['test', 'text', 'tent'], starts_with='te', ends_with='t'))


#3
def split_string(text, delimiter=' '):
    return text.split(delimiter)

def compare_elements(list1, list2, comparison_function=None):
    result = []
    for i in range(min(len(list1), len(list2))):
        x, y = list1[i], list2[i]
        if comparison_function is None:
            if x == y:
                result.append((x, y))
        else:
            if comparison_function(x, y):
                result.append((x, y))
    return result


def count_unique_chars(*strings):
    unique_chars = set()
    for string in strings:
        for char in string:
            unique_chars.add(char)
    return len(unique_chars)

def common_elements(*lists):
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common = common.intersection(set(lst))
    return list(common)

# Запускаем примеры
print("split_string:")
print(split_string('яблоко виноград дыня'))
print(split_string('one,two,three', delimiter=','))

print("\ncompare_elements:")
print(compare_elements([1, 2, 3], [1, 4, 3]))
print(compare_elements([1, 2, 3], [4, 5, 6], 
                     comparison_function=lambda x, y: x + y > 5))


print("\ncount_unique_chars:")
print(count_unique_chars('hello', 'world'))
print(count_unique_chars('abc', 'def', 'ghi'))


print("\ncommon_elements:")
print(common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(common_elements(['a', 'b'], ['b', 'c'], ['b', 'd']))
print(common_elements([10, 20, 30], [20, 30, 40]))
print(common_elements([1, 2], [3, 4]))



#4
# a
def calculate(a, b, operation='add'):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    else:
        return None
print(calculate(10, 5))                    # 15
print(calculate(10, 5, operation='multiply'))  # 50
# б
def modify_strings(strings, case=None):
    if case == 'upper':
        return [s.upper() for s in strings]
    elif case == 'lower':
        return [s.lower() for s in strings]
    else:
        return strings
print(modify_strings(['Hello', 'World']))                # ['Hello', 'World']
print(modify_strings(['Hello', 'World'], case='upper'))  # ['HELLO', 'WORLD']
print(modify_strings(['Hello', 'World'], case='lower'))
# в
def average(*numbers):
    if not numbers:  
        return 0
    return sum(numbers) / len(numbers)
print(average(1, 2, 3, 4, 5))  # 3.0
print(average(10, 20))              # 15.0
print(average())                    # 0

# г
def merge_dictionaries(main_dict, **additional_dicts):
    result = main_dict.copy()  
    for dict_name, dict_value in additional_dicts.items():
        result.update(dict_value)  
    return result
print(merge_dictionaries({'a': 1, 'b': 2}, dict1={'b': 3, 'c': 4}))
# {'a': 1, 'b': 3, 'c': 4}

print(merge_dictionaries({'x': 5}, dict1={'y': 6}, dict2={'z': 7}))
# {'x': 5, 'y': 6, 'z': 7}



#5
def filter_items(items, condition=None):
    if condition is None:
        return items
    else:
        result = []
        for item in items:
            if condition(item):
                result.append(item)
        return result


def merge_and_filter(list1, list2, filter_function=None):
    merged = list1 + list2
    if filter_function is None:
        return merged
    else:
        result = []
        for item in merged:
            if filter_function(item):
                result.append(item)
        return result

def common_in_all(*lists):
    if not lists:
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common = common.intersection(set(lst))
    return list(common)

def find_primes(*numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in numbers:
        if is_prime(num):
            result.append(num)
    return result

# Примеры вызовов
print("filter_items:")
print(filter_items([1, 2, 3, 4, 5]))
print(filter_items([1, 2, 3, 4, 5], condition=lambda x: x > 3))

print("\nmerge_and_filter:")
print(merge_and_filter([1, 2], [3, 4]))
print(merge_and_filter([1, 2], [3, 4], filter_function=lambda x: x % 2 == 0))

print("\ncommon_in_all:")
print(common_in_all([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(common_in_all(['яблоко', 'вишня'], ['виноград', 'вишня'], ['вишня', 'дыня']))

print("\nfind_primes:")
print(find_primes(2, 3, 4, 5, 6, 7))
print(find_primes(10, 15, 17, 19, 23))





#6
def word_count(text, separator=' '):
    words = text.split(separator)
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

def filter_numbers(numbers, exclude_multiples_of=2):
    result = []
    for num in numbers:
        if num % exclude_multiples_of != 0:
            result.append(num)
    return result

def merge_and_sort_keys(*dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged:
                merged[key] = max(merged[key], value)
            else:
                merged[key] = value
    sorted_keys = sorted(merged.keys(), key=lambda k: merged[k], reverse=True)
    return sorted_keys

def sum_non_negative(*numbers):
    total = 0
    for num in numbers:
        if num >= 0:
            total += num
    return total

# Примеры вызовов
print("word_count:")
print(word_count('один два один'))
print(word_count('red,green,blue,red', separator=','))

print("\nfilter_numbers:")
print(filter_numbers([1, 2, 3, 4, 5]))
print(filter_numbers([10, 15, 20, 25], exclude_multiples_of=5))

print("\nmerge_and_sort_keys:")
print(merge_and_sort_keys({'a': 2, 'b': 3}, {'a': 5, 'c': 1}))
print(merge_and_sort_keys({'x': 10}, {'y': 5}, {'z': 15}))

print("\nsum_non_negative:")
print(sum_non_negative(1, -2, 3, -4, 5))
print(sum_non_negative(-10, -20))



#7
def join_strings(strings, delimiter=','):
    return delimiter.join(strings)

def combine_lists(list1, list2, join_str=''):
    result = []
    for i in range(len(list1)):
        combined = list1[i] + join_str + list2[i]
        result.append(combined)
    return result

def unique_values(*args):
    unique = []
    for item in args:
        if item not in unique:
            unique.append(item)
    return unique

def reverse_concatenate(*strings):
    reversed_list = list(strings)[::-1]
    return ' '.join(reversed_list)

# Примеры вызовов
print("join_strings:")
print(join_strings(['один', 'два', 'три']))
print(join_strings(['sun', 'moon', 'stars'], delimiter=' | '))

print("\ncombine_lists:")
print(combine_lists(['a', 'b'], ['1', '2']))
print(combine_lists(['x', 'y'], ['10', '20'], join_str='-'))


print("\nunique_values:")
print(unique_values(1, 2, 2, 3, 3, 3))
print(unique_values('a', 'b', 'a', 'c', 'b'))

print("\nreverse_concatenate:")
print(reverse_concatenate('one', 'two', 'three'))
print(reverse_concatenate('hello', 'world'))



#8
def pair_and_filter(list1, list2, filter_function=None):
    result = []
    for x in list1:
        for y in list2:
            if filter_function is None:
                result.append((x, y))
            else:
                if filter_function(x, y):
                    result.append((x, y))
    return result

def concat_or_upper(strings, uppercase=False):
    if uppercase:
        upper_strings = [s.upper() for s in strings]
        return ' '.join(upper_strings)
    else:
        return ' '.join(strings)

def filter_uppercase_strings(strings):
    result = []
    for s in strings:
        if s.isupper():
            result.append(s)
    return result

def unique_sorted_elements(*lists):
    unique = set()
    for lst in lists:
        for item in lst:
            unique.add(item)
    return sorted(list(unique))

# Примеры вызовов
print("pair_and_filter:")
print(pair_and_filter([1, 2], [3, 4]))
print(pair_and_filter([1, 2], [3, 4], filter_function=lambda x, y: (x + y) % 2 == 0))

print("\nconcat_or_upper:")
print(concat_or_upper(['hello', 'world']))
print(concat_or_upper(['hello', 'world'], uppercase=True))

print("\nfilter_uppercase_strings:")
print(filter_uppercase_strings(['HELLO', 'World', 'BYE']))
print(filter_uppercase_strings(['Python', 'JAVA', 'c++']))

print("\nunique_sorted_elements:")
print(unique_sorted_elements([3, 1], [2, 3], [1, 4]))
print(unique_sorted_elements(['b', 'a'], ['c', 'a'], ['d', 'b']))




#9
def capitalize_words(text, separator=' '):
    words = text.split(separator)
    capitalized = []
    for word in words:
        if word:
            capitalized.append(word[0].upper() + word[1:].lower())
        else:
            capitalized.append('')
    return separator.join(capitalized)

def filter_elements(list1, list2, filter_function=None):
    combined = list1 + list2
    result = []
    for item in combined:
        if filter_function is None:
            result.append(item)
        else:
            if filter_function(item):
                result.append(item)
    return result

def merge_dictionaries(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

def unique_keys(*dicts):
    all_keys = {}
    for d in dicts:
        for key in d.keys():
            if key in all_keys:
                all_keys[key] += 1
            else:
                all_keys[key] = 1

    result = {}
    for d in dicts:
        for key, value in d.items():
            if all_keys[key] == 1:
                result[key] = value
    return result

# Примеры вызовов
print("capitalize_words:")
print(capitalize_words('hello world'))
print(capitalize_words('python,java,c++', separator=','))

print("\nfilter_elements:")
print(filter_elements([1, 2, 3], [4, 5, 6]))
print(filter_elements([1, 2, 3], [4, 5, 6], filter_function=lambda x: x > 3))

print("\nmerge_dictionaries:")
print(merge_dictionaries({'a': 1}, {'b': 2}, {'a': 3}))
print(merge_dictionaries({'x': 5}, {'y': 6}, {'z': 7}, {'x': 8}))

print("\nunique_keys:")
print(unique_keys({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(unique_keys({'x': 5}, {'y': 6}, {'z': 7}, {'x': 8}))




#10
def filter_numbers(numbers, condition=None):
    if condition is None:
        return numbers
    else:
        result = []
        for num in numbers:
            if condition(num):
                result.append(num)
        return result

def transform_numbers(numbers, transform_function=None):
    if transform_function is None:
        return numbers
    else:
        result = []
        for num in numbers:
            result.append(transform_function(num))
        return result

def cube_numbers(*lists):
    result = []
    for lst in lists:
        for num in lst:
            result.append(num ** 3)
    return result

def product_non_zero(*numbers):
    product = 1
    for num in numbers:
        if num != 0:
            product *= num
    return product

# Примеры вызовов
print("filter_numbers:")
print(filter_numbers([1, 2, 3, 4, 5]))
print(filter_numbers([1, 2, 3, 4, 5], condition=lambda x: x % 2 == 0))

print("\ntransform_numbers:")
print(transform_numbers([1, 2, 3]))
print(transform_numbers([1, 2, 3], transform_function=lambda x: x ** 3))

print("\ncube_numbers:")
print(cube_numbers([1, 2], [3, 4]))
print(cube_numbers([5], [6, 7], [8]))

print("\nproduct_non_zero:")
print(product_non_zero(1, 2, 0, 4))
print(product_non_zero(0, 0, 0))



#11
def format_strings(strings, separator=' '):
    capitalized = []
    for s in strings:
        if s:
            capitalized.append(s[0].upper() + s[1:].lower())
        else:
            capitalized.append('')
    return separator.join(capitalized)

def merge_and_sort(list1, list2, sort_function=None):
    merged = list1 + list2
    if sort_function is None:
        return sorted(merged)
    else:
        return sorted(merged, key=sort_function)

def concat_all_strings(*lists):
    all_strings = []
    for lst in lists:
        for s in lst:
            all_strings.append(s)
    return ','.join(all_strings)

def unique_sorted_strings(*strings):
    unique = []
    for s in strings:
        if s not in unique:
            unique.append(s)
    return sorted(unique)

# Примеры вызовов
print("format_strings:")
print(format_strings(['hello', 'world']))
print(format_strings(['good', 'morning'], separator='-'))

print("\nmerge_and_sort:")
print(merge_and_sort([3, 1], [4, 2]))
print(merge_and_sort([3, 1], [4, 2], sort_function=lambda x: -x))

print("\nconcat_all_strings:")
print(concat_all_strings(['a', 'b'], ['c', 'd']))
print(concat_all_strings(['вишня'], ['банан', 'дыня'], ['киви']))

print("\nunique_sorted_strings:")
print(unique_sorted_strings('виноград', 'яблоко', 'тыква', 'яблоко'))
print(unique_sorted_strings('x', 'z', 'y', 'x', 'y'))




#12
def combine_lists(list1, list2, order='first_second'):
    if order == 'first_second':
        return list1 + list2
    elif order == 'second_first':
        return list2 + list1
    else:
        return list1 + list2

def process_string(text, separator=None):
    if separator is not None:
        words = text.split(separator)
        capitalized = []
        for word in words:
            if word:
                capitalized.append(word[0].upper() + word[1:].lower())
            else:
                capitalized.append('')
        return separator.join(capitalized)
    else:
        return text.lower()

def difference(*lists):
    if not lists:
        return []
    first_list = lists[0]
    other_elements = set()
    for lst in lists[1:]:
        for item in lst:
            other_elements.add(item)
    result = []
    for item in first_list:
        if item not in other_elements:
            result.append(item)
    return result

def common_in_at_least_two(*lists):
    count = {}
    for lst in lists:
        for item in lst:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
    result = []
    for item, freq in count.items():
        if freq >= 2:
            result.append(item)
    return result

# Примеры вызовов
print("combine_lists:")
print(combine_lists([1, 2], [3, 4]))
print(combine_lists([1, 2], [3, 4], order='second_first'))

print("\nprocess_string:")
print(process_string('HELLO WORLD'))
print(process_string('python_java_c++', separator='_'))

print("\ndifference:")
print(difference([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(difference(['a', 'b', 'c'], ['b', 'c'], ['c']))

print("\ncommon_in_at_least_two:")
print(common_in_at_least_two([1, 2], [2, 3], [2, 4]))
print(common_in_at_least_two(['a', 'b'], ['b', 'c'], ['b', 'd']))




#13
def divisible_by(numbers, divisor=2):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result

def transform_numbers(numbers, transform_function=None):
    if transform_function is None:
        result = []
        for num in numbers:
            if num >= 0:
                result.append(num)
        return result
    else:
        result = []
        for num in numbers:
            result.append(transform_function(num))
        return result

def sorted_values_by_keys(*dicts):
    all_items = []
    for d in dicts:
        for key, value in d.items():
            all_items.append((key, value))
    sorted_items = sorted(all_items, key=lambda item: item[0])
    result = []
    for item in sorted_items:
        result.append(item[1])
    return result

def common_keys_in_dicts(*dicts):
    if not dicts:
        return {}
    common_keys = set(dicts[0].keys())
    for d in dicts[1:]:
        common_keys &= set(d.keys())
    result = {}
    for key in common_keys:
        for d in reversed(dicts):
            if key in d:
                result[key] = d[key]
                break
    return result

# Примеры вызовов
print("divisible_by:")
print(divisible_by([1, 2, 3, 4, 5]))
print(divisible_by([10, 15, 20, 25], divisor=5))

print("\ntransform_numbers:")
print(transform_numbers([1, -2, 3, -4]))
print(transform_numbers([1, 2, 3], transform_function=lambda x: x ** 2))

print("\nsorted_values_by_keys:")
print(sorted_values_by_keys({'2': 'b', '1': 'a'}, {'4': 'd', '3': 'c'}))
print(sorted_values_by_keys({'10': 'j'}, {'5': 'e', '15': 'o'}))

print("\ncommon_keys_in_dicts:")
print(common_keys_in_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(common_keys_in_

#14
def merge_lists_with(list1, list2, merge_function=None):
    if merge_function is None:
        return list1 + list2
    result = []
    for i in range(len(list1)):
        if i < len(list2):
            result.append(merge_function(list1[i], list2[i]))
    return result

def extract_digits(strings, digits_only=False):
    if not digits_only:
        return strings
    result = []
    for s in strings:
        digits = ""
        for char in s:
            if char.isdigit():
                digits += char
        result.append(digits)
    return result

def filter_even_numbers(*numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

def sorted_positive_numbers(*numbers):
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return sorted(positive, reverse=True)

# Примеры вызовов
print("merge_lists_with:")
print(merge_lists_with([1, 2], [3, 4]))
print(merge_lists_with([1, 2], [3, 4], merge_function=lambda x, y: x + y))

print("\nextract_digits:")
print(extract_digits(['a1b2', 'c3d4']))
print(extract_digits(['a1b2', 'c3d4'], digits_only=True))

print("\nfilter_even_numbers:")
print(filter_even_numbers(1, 2, 3, 4, 5, 6))
print(filter_even_numbers(7, 9, 11))

print("\nsorted_positive_numbers:")
print(sorted_positive_numbers(-1, 3, -5, 7, 0))
print(sorted_positive_numbers(-10, -20))


#15
def change_case(strings, to_upper=False):
    result_parts = []
    for s in strings:
        if to_upper:
            result_parts.append(s.upper())
        else:
            result_parts.append(s.lower())
    return ' '.join(result_parts)

def filter_combined_lists(list1, list2, filter_function=None):
    combined = list1 + list2
    if filter_function is None:
        return combined
    else:
        result = []
        for item in combined:
            if filter_function(item):
                result.append(item)
        return result

def unique_sorted_numbers(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return sorted(unique)

def strings_starting_with_upper(*strings):
    result = []
    for s in strings:
        if s and s[0].isupper():
            result.append(s)
    return result

# Примеры вызовов
print("change_case:")
print(change_case(['Hello', 'World']))
print(change_case(['Hello', 'World'], to_upper=True))

print("\nfilter_combined_lists:")
print(filter_combined_lists([2, 4], [6, 8]))
print(filter_combined_lists([2, 4], [6, 8], filter_function=lambda x: x > 5))

print("\nunique_sorted_numbers:")
print(unique_sorted_numbers([3, 1, 2, 3, 4, 2]))
print(unique_sorted_numbers([5, 5, 5, 5]))

print("\nstrings_starting_with_upper:")
print(strings_starting_with_upper('Apple', 'banana', 'Cherry'))
print(strings_starting_with_upper('dog', 'Elephant', 'fox'))


