#1
# k, n = map(int, input().split())
# while n > 0:
#     print(k)
#     n -= 1

#2
# a, b = map(int, input().split())
# cnt = 0
# for i in range(a, b + 1):
#     print(i)
#     cnt += 1
# print(cnt)

#3
# a, b = map(int, input().split())
# cnt = 0
# for i in range(b - 1, a, -1):
#     print(i)
#     cnt += 1
# print(cnt)

#4
# c = 20.4
# for i in range(1, 11):
#     print(i, '-', i * c)


#5
# a, b, h = map(int, input().split())
# for i in range(a, b, h):
#     print(i ** 2)


#6
# a, b, h = map(int, input().split())
# for i in range(a, b, h):
#     if i >= 0:
#         print(i)

#7

# a, b = map(int, input().split())
# sumc = 0
# for i in range(a, b + 1):
#     sumc += i
# print(sumc)


#8
# a, b = map(int, input().split())
# sumc = 1
# for i in range(a, b + 1):
#     sumc *= i
# print(sumc)

#9
# a, b = map(int, input().split())
# sumc = 0
# for i in range(a, b + 1):
#     sumc += i ** 2
# print(sumc)


# #10
# n = float(input())
# for weight in range(12, 22, 2):
#     weight /= 10
#     cost = n * weight
#     print(weight, '-', cost)

#11
# n = int(input())
# sq = 0
# for i in range(n):
#     sq += (2 * i + 1)
# print(sq)

#a, n = map(float, input().split())
#i = 0
#while a**i < n:
#   print(a**i, end=' ')
#   i += 1

#13
# n = int(input())
# maxi = 1
# for i in range(1, n + 1):
#     if i ** 2 <= n:
#         maxi = i ** 2
# print(maxi)

#14
# n = int(input())
# maxk = 1
# for k in range(1, n + 1):
#     if 3 ** k < n:
#         maxk = k
# print(maxk)

#15
# n = int(input())
# a, b = map(float, input().split())
# lined = (b - a) / n
# print(lined)
# for i in range(0, int(b - a)):
#     print(a + lined * i)
