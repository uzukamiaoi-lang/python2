#1
#а
#d = {1:2, 3:4, 4:3, 2:1, 0:0}
#sorted_asc = dict(sorted(d.items(), key=lambda x: x[1]))
#sorted_desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
#print("По возрастанию:", sorted_asc)
#print("По убыванию:", sorted_desc)
#б
#d1 = {1:2, 3:4}
#d2 = {3:5, 6:7}
#result = d1.copy()
#for k, v in d2.items():
#    if k in result:
#        result[k] += v
#    else:
#        result[k] = v
#print(result)
#в
#d = {1:2, 3:4}
#keys_to_check = {1, 3}
#all_present = all(k in d for k in keys_to_check)
#print(all_present)
#2
#а
#d = {1:2, 3:4}
#new_key = 5
#new_val = 6
#d[new_key] = new_val
#print(d)
#б
#d = {1:2, 3:4, 5:2}
#unique_values = set(d.values())
#print(unique_values)
#в
#d = {1:[2,3,4], 3:[5,6,7], 5:[8,9,0]}
#total = 0
#for v in d.values():
#    total += len(v)
#print(total)
#3
#а
#d1 = {1:2}
#d2 = {3:4}
#d3 = {5:6}
#result = {}
#result.update(d1)
#result.update(d2)
#result.update(d3)
#print(result)
#б
#d = {1:2, 3:4, 4:3, 2:1, 0:0}
#sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
#print(sorted_d)
#в
#d = {1:[2,3,4], 3:[5,6,7], 5:[8,9,0]}
#for k in d:
#    d[k] = []
#print(d)
#4
#а
#d = {1:2, 3:4}
#keys_to_check = [1, 3]
#all_present = True
#for k in keys_to_check:
#    if k not in d:
#        all_present = False
#        break
#print(all_present)
#б
#from itertools import permutations

#d = {1: 'abc', 2: 'def'}
#key = 1
#value = d.get(key, '')
#if value:
#    perms = [''.join(p) for p in permutations(value)]
#    print(perms)
#else:
#    print("Ключ не найден")
#в
#d = {1: [2,3,4], 3: [5,6,7], 5: [8,9,0]}
#for k in d:
#    lst = d[k]
#    avg = sum(lst) / len(lst)
#    d[k] = round(avg, 1)  # округляем до 1 знака
#print(d)
#5
#а
#d = {1:2, 3:4, 5:6}
#for key, value in d.items():
#    print(key, ":", value)
#б
#d = {1:2, 3:4, 5:6}
#values = list(d.values())
#values.sort(reverse=True)
#top3 = values[:3]
#print(top3)
#в
#d1 = {1:2, 3:4}
#d2 = {1:3, 3:4}
#result = {}
#for k in d1:
#    if k in d2:
#        result[k] = (d1[k], d2[k])
#print(result)
#6
#а
#n = 5
#d = {}
#for i in range(1, n+1):
#    d[i] = i*i
#print(d)
#б
#dicts = [{1:2, 3:4}, {5:6}]
#values = []
#for d in dicts:
#    for v in d.values():
#        values.append(v)
#print(values)
#в
#d = {1: '', 2: 'abc', 3: None, 4: [], 5: 0}
#to_delete = []
#for k, v in d.items():
#    if v == '' or v is None or v == []:
#        to_delete.append(k)
#for k in to_delete:
#    del d[k]
#print(d)
#7
#а
#d = {}
#for i in range(1, 16):
#    d[i] = i*i
#print(d)
#б
#s = "hello world"
#freq = {}
#for ch in s:
#    if ch in freq:
#        freq[ch] += 1
#    else:
#        freq[ch] = 1
#print(freq)
#в
#d = {'a':1, 'b':2, 'c':3, 'd':4}
#filtered = {}
#for k, v in d.items():
#    if v > 2:
#        filtered[k] = v
#print(filtered)
#8
#а
#d1 = {'a':1, 'b':2}
#d2 = {'c':3, 'd':4}
#merged = d1.copy()
#merged.update(d2)
#print(merged)
#б
#d = {'a':1, 'b':2, 'c':3, 'd':4}
#print("Ключ : Значение")
#for k, v in d.items():
#    print(k, " : ", v)
#в
#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#keys = ['key1', 'key2']
#d = {keys[0]: list1, keys[1]: list2}
#print(d)
#9
#а
d = {'a':1, 'b':2, 'c':3, 'd':4}
for key, value in d.items():
    print("key:", key, ", value:", value)
#б
list_of_dicts = [{'a':1}, {'a':2}, {'a':3}, {'b':1}]
key = 'a'
total = 0
for d in list_of_dicts:
    if key in d:
        total += d[key]
print(total)
#в
students = {'Иван': {'рост':170, 'вес':70}, 'Михаил': {'рост':180, 'вес':75}}
filtered = {}
for name, data in students.items():
    filtered[name] = {'рост': data['рост']}
print(filtered)
#10
#а
#d = {'a':1, 'b':2, 'c':3, 'd':4}
#total = sum(d.values())
#print(total)
#б
#lst = ['a', 'b', 'c']
#d = {}
#for item in lst:
#    d[item] = {}
#print(d)
#в
#d = {'a':1, 'b':1, 'c':1}
#values = list(d.values())
#first = values[0]
#all_same = all(v == first for v in values)
#print(all_same)
#11
#а
#d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#product = 1
#for v in d.values():
#    product *= v
#print(product)
#б
#d = {'a': ['c', 'b', 'a'], 'b': ['c', 'b', 'a']}
#for key in d:
#    d[key].sort()
#print(d)
#в
#pairs = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
#result = {}
#for key, val in pairs:
#    if key not in result:
#        result[key] = []
#    result[key].append(val)
#print(result)
#12
#а
#d = {'a': 1, 'b': 2, 'c': 3}
#key_to_remove = 'b'
#if key_to_remove in d:
#    del d[key_to_remove]
#print(d)
#б
#d = {'a b': 1, ' c ': 2, 'd': 3}
#new_d = {}
#for k, v in d.items():
#    new_key = k.replace(' ', '')
#    new_d[new_key] = v
#print(new_d)
#в
#d = {'a': [1, 2], 'b': [3, 4]}
#keys = list(d.keys())
#values = list(d.values())
#length = len(values[0])
#result = []
#for i in range(length):
#    new_dict = {}
#    for j in range(len(keys)):
#        new_dict[keys[j]] = values[j][i]
#    result.append(new_dict)
#print(result)
#13
#а
#keys = ['a', 'b', 'c']
#values = [1, 2, 3]
#d = {}
#for i in range(len(keys)):
#    d[keys[i]] = values[i]
#print(d)
#б
#items = [
#    {'name': 'item1', 'price': 10},
#    {'name': 'item2', 'price': 50},
#    {'name': 'item3', 'price': 30},
#   {'name': 'item4', 'price': 40}
#]
#sorted_items = sorted(items, key=lambda x: x['price'], reverse=True)
#top3 = sorted_items[:3]
#print(top3)
#в
#list_of_dicts = [{'a':1}, {'b':2}, {'c':3}]
#to_remove = {'b':2}
#result = []
#for d in list_of_dicts:
#    if d != to_remove:
#        result.append(d)
#print(result)
#14
#а
#d = {'b': 1, 'a': 2, 'c': 3}
#sorted_d = dict(sorted(d.items()))
#print(sorted_d)
#б
#d = {'a': 1, 'b': 2, 'c': 3}
#for key, value in d.items():
#  print("key:", key, ", value:", value, ", item:", (key, value))
#в
#d = {'a': '1', 'b': '2', 'c': '3.0'}
#new_d = {}
#for k, v in d.items():
#    if '.' in v:
#        new_d[k] = float(v)
#    else:
#        new_d[k] = int(v)
#print(new_d)
#15
#а
#d = {'a': 1, 'b': 2, 'c': 3}
#max_val = max(d.values())
#min_val = min(d.values())
#print("max:", max_val, ", min:", min_val)
#б
#d = {'a': 1, 'b': 2, 'c': 3}
#for key, value in d.items():
#    print("key:", key, ", value:", value)
#в
#    d = {
#    'x': list(range(11, 21)),
#    'y': list(range(21, 31)),
#    'z': list(range(31, 41))
#}
#for key, lst in d.items():
#    print("пятый элемент из", key + ":", lst[4])
