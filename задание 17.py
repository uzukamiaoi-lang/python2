#1
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

def fact2(n):
    if n == 1 or n == 2:
        return n
    else:
        return n * fact2(n - 2)

# Примеры вызовов
print("Факториал:")
print(f"5! = {fact(5)}")  
print(f"1! = {fact(1)}")   
print(f"0! = {fact(0)}")   

print("\nДвойной факториал:")
print(f"5!! = {fact2(5)}") 
print(f"6!! = {fact2(6)}") 
print(f"1!! = {fact2(1)}") 
print(f"2!! = {fact2(2)}") 
# ghbvths dspjdjd
print(PowerN(2, 3))   
print(PowerN(5, 0))   
print(PowerN(2, -3))  
print(PowerN(3, 4))   
#2
def PowerN(x, n):    
    if n == 0:
        return 1    
    elif n > 0:
        return x * PowerN(x, n - 1)    
    else:
        return 1 / PowerN(x, -n)
# Пример использования:
print(PowerN(2, 3))  # 8
print(PowerN(2, -2))  # 0.25
print(PowerN(5, 0))   # 1
#3
def SqrtK(x, k, n):    
    if n == 0:
        return 1    
    else:
        y_prev = SqrtK(x, k, n - 1)  
        y_n = y_prev - (y_prev - x / (y_prev ** (k - 1))) / k
        return y_n
# Пример использования:
print(SqrtK(27, 3, 5))
#4
call_count = 0
def FibRec(N):
    global call_count
    call_count += 1     
    if N == 1 or N == 2:
        return 1    
    else:
        return FibRec(N - 2) + FibRec(N - 1)
for i in range(1, 6):
    call_count = 0  
    fib_number = FibRec(i)
    print(f"F({i}) = {fib_number}, вызовов функции: {call_count}")
#5
call_count = 0
def C(m, n):
    global call_count
    call_count += 1      
    if m == 0 or m == n:
        return 1    
    else:
        return C(m, n - 1) + C(m - 1, n - 1)
# Пример использования:
N = 5  
M_values = [1, 2, 3, 4, 5]  
for M in M_values:
    call_count = 0  
    result = C(M, N)
    print(f"C({M}, {N}) = {result}, вызовов функции: {call_count}")
#6
def NOD(A, B):
    if A == 0:
        return B
    else:
        return NOD(B % A, A)
# Пример использования:
A = 48
B = 18
C = 30
D = 42
print(f"NOD({A}, {B}) = {NOD(A, B)}")  
print(f"NOD({A}, {C}) = {NOD(A, C)}")  
print(f"NOD({A}, {D}) = {NOD(A, D)}")
#7
def MinRec(A, index=0):    
    if index == len(A) - 1:
        return A[index]
    else:        
        min_of_rest = MinRec(A, index + 1)        
        return A[index] if A[index] < min_of_rest else min_of_rest
# Пример использования:
arr1 = [3, 1, 4, 1, 5]
arr2 = [10, 2, 8, 6]
arr3 = [7, 7, 7, 7]
print(f"Минимальный элемент в {arr1}: {MinRec(arr1)}")
print(f"Минимальный элемент в {arr2}: {MinRec(arr2)}")
print(f"Минимальный элемент в {arr3}: {MinRec(arr3)}")
#8
def Digits(S, index=0):    
    if index == len(S):
        return 0
    else:        
        current_char_is_digit = 1 if S[index].isdigit() else 0        
        rest_digits = Digits(S, index + 1)        
        return current_char_is_digit + rest_digits
# Пример использования:
str1 = "abc123def45"
str2 = "no digits here"
str3 = "1a2b3c4d5e"
print(f"Количество цифр в '{str1}': {Digits(str1)}")
print(f"Количество цифр в '{str2}': {Digits(str2)}")
print(f"Количество цифр в '{str3}': {Digits(str3)}")
#9
def Simm(S):    
    if len(S) <= 1:
        return True    
    if S[0] != S[-1]:
        return False    
    return Simm(S[1:-1])
# Пример использования:
print(Simm("aba"))     
print(Simm("abc"))     
print(Simm("racecar")) 
print(Simm("hello"))
#10
def AddBinary(a, b):    
    if b == 0:
        return a    
    sum_without_carry = a ^ b  
    carry = (a & b) << 1       
    return AddBinary(sum_without_carry, carry)
# Пример использования:
print(AddBinary(5, 3))
#11
def Root(f, a, b, epsilon=0.001):    
    if f(a) * f(b) >= 0:
        return None      
    mid = (a + b) / 2    
    if abs(f(mid)) < epsilon:
        return mid    
    if f(mid) < 0:
        return Root(f, mid, b, epsilon)  
    else:
        return Root(f, a, mid, epsilon)  
# Пример функции f(x)
def f(x):
    return x**2 - 4
root = Root(f, 1, 3)
print("Корень уравнения:", root)
#12
def ReverseNumber(n, reversed_num=0):    
    if n == 0:
        return reversed_num   
    digit = n % 10        
    reversed_num = reversed_num * 10 + digit  
    remaining = n // 10   
    return ReverseNumber(remaining, reversed_num)
# Пример использования:
print(ReverseNumber(123))   
print(ReverseNumber(4567))
#13
def Simm(S, i, j):   
    if i >= j:
        return True   
    if S[i] != S[j]:
        return False    
    return Simm(S, i + 1, j - 1)
# Пример использования:
S = "abccba"
print(Simm(S, 0, 5))  
print(Simm(S, 1, 4))  
print(Simm(S, 0, 3))
#14
def sum_digits(N):    
    if N < 10:
        return N
    else:
        return (N % 10) + sum_digits(N // 10)
# Пример использования:
N = 12345
result = sum_digits(N)
print("Сумма цифр числа", N, "равна", result)
#15
def is_palindrome(word, start=0):    
    if start >= len(word) // 2:
        return "yes"    
    if word[start] != word[len(word) - 1 - start]:
        return "no"    
    return is_palindrome(word, start + 1)
# Пример использования:
word1 = "level"
word2 = "python"

print(is_palindrome(word1))  
print(is_palindrome(word2))