#1
#s = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = s.split()
#print(len(words))
#2
#s = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = s.split()
#count = 0
#for w in words:
#    if w[0] == w[-1]:
#        count += 1
#print(count)
#3
#s = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = s.split()
#count = 0
#for w in words:
#    if 'А' in w:
#        count += 1
#print(count)
#4
#s = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = s.split()
#min_len = len(words[0])
#for w in words:
#    if len(w) < min_len:
#        min_len = len(w)
#print(min_len)
#5
#s = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = s.split()
#result = ' '.join(reversed(words))
#print(result)
#6
#s = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = s.split()
#words.sort()
#result = ' '.join(words)
#print(result)
#7
#C = 'А'
#S = "АННА РОЗА МАМА ПАПА"
#S0 = "XX"
#result = S.replace(C, S0 + C)
#print(result)
#8
#S = "  ПРИВЕТ    МИР    КАК   ДЕЛА  "
#words = S.split()
#result = ' '.join(words)
#print(result)
#9
#S = "Hello мир! Привет World!"
#count = 0
#for ch in S:
#    if ('a' <= ch <= 'z') or ('а' <= ch <= 'я'):
#        count += 1
#print(count)
#10
#S = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = S.split()
#max_len = 0
#for w in words:
#    if len(w) > max_len:
#        max_len = len(w)
#print(max_len)
#11
#S = "Программа"
#even = S[1::2]  
#odd = S[0::2]  
#result = even + odd[::-1]
#print(result)
#12
#S = "ABC"
#N = 3
#stars = "*" * N
#result = stars.join(S)
#print(result)
#13
#S = "ПРИВЕТ МИР КАК ДЕЛА"
#C = '.'
#words = S.split()
#result = C.join(words)
#print(result)
#14
#full_path = r"d:\ivanov\primer\prog.py"
#file_name_with_ext = full_path.split("\\")[-1]
#name_without_ext = file_name_with_ext.split(".")[0]
#print(name_without_ext)
#15
#S = "ПРИВЕТ МИР АННА РОЗА ДОХОД ТЕСТ КАК ДЕЛА"
#words = S.split()
#longest_word = ""
#max_len = 0
#for w in words:
#    if len(w) >= max_len:
#        max_len = len(w)
#        longest_word = w
#print(longest_word)
