#1
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += 1 / (2 ** i)
# print(sumd)

#2
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += (math.cos(x)) ** n / n
# print(sumd)


#3
# n = int(input())
# sumd = 0
# for i in range(0, n + 1):
#     sumd += (-1) ** i * 3 ** i
# print(sumd)


#4
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += 1 / (math.sin(i))
# print(sumd)


#5
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += ((-1) ** (i + 1)) * i ** 3
# print(sumd)

#6
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += (-1) ** (i + 1) * math.cos(i)
# print(sumd)


#7
import math

# n = int(input())
# x = float(input())
# sumd = 0
# if abs(x) < 1:
#     for i in range(1, n + 1):
#         sumd += ((-1) ** (i - 1) * x ** i) / i
# else:
#     print('Error')
# print(sumd)


#8
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += (-1) ** (i + 1) * math.factorial(i)
# print(sumd)

#9
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += math.sin(x ** i)
# print(sumd)

#10
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += 1 / math.factorial(i)
# print(sumd)


#11
# import math
#
# n = int(input())
# s = 0
# for i in range(n):
#     s += (n + i) ** 2
# print(s)


#12
# import math
#
# n = int(input())
# sumd = 0
# for i in range(1, n + 1):
#     sumd += math.factorial(i)
# print(sumd)

#13
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(n + 1):
#     sumd += (x ** i) / (math.factorial(i))
# print(sumd)

#14
# import math
#
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(0, n + 1):
#     sumd += (-1) ** i * x ** i
# print(sumd)


#15
# import math
# 
# n = int(input())
# x = float(input())
# sumd = 0
# for i in range(n + 1):
#     p = 2 * i + 1
#     sy = (-1) ** i
#     sumd += sy * (x ** p) / p
# print(sumd)
