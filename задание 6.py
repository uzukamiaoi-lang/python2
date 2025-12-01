#БЛОК 6
#1
# import math
#
# a = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     a.append(element)
# k, l = map(int, input().split())
# if not (1 <= k <= l <= n):
#     print('error')
# masa2 = a[k - 1:l]
# sumel = sum(masa2)
# countel = len(masa2)
# srarif = sumel / countel
# print(srarif)


#2
# import math
#
# a = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     a.append(element)
# k, l = map(int, input().split())
# if not (1 <= k <= l <= n):
#     print('error')
# masa2 = a[k - 1:l]
# sumel = sum(masa2)
# suma = sum(a)
# razn = suma - sumel
# print(razn)

#3
#1
# import math
#
# a = []
# n = int(input())
# for i in range(n):
#     element = int(input())
#     a.append(element)
# k, l = map(int, input().split())
# if not (1 <= k <= l <= n):
#     print('error')
# del a[k - 1:l]
# print(a)
# sumel = sum(a)
# countel = len(a)
# srarif = sumel / countel
# print(srarif)

#4
# a = [0, 1, 2, 3, 4, 5]
# chet = []
# nechet = []
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         chet.append(a[i])
#     else:
#         nechet.append(a[i])
# nechet.reverse()
# maxar = chet + nechet
# print(maxar)

#5
# a = [0, 1, 2, 3, 4, 5]
#
# for i in range(0, len(a), 2):
#     print(a[i], end=' ')
# for i in range(1, len(a), 2):
#     print(a[i], end=' ')

#6
# a = [0, 6, 2, 3, 4, 5]
# maxel = max(a)
# r = a.index(maxel)
# del a[0:r + 1]
# prod = 1
# for i in range(len(a)):
#     prod *= a[i]
# print(prod)

#7
# a = [3, 1, 2, 3, 4, 7]
# maxel = max(a)
# minel = min(a)
# r = a.index(maxel)
# l = a.index(minel)
# if r - l > 0:
#     masa = a[l:r + 1]
# else:
#     masa = a[r:l + 1]
# print(masa)
# suma = sum(masa)
# print(suma)

#8
# a = [3, 1, 2, 3, 4, 7]
# maxel = max(a)
# minel = min(a)
# r = a.index(maxel)
# l = a.index(minel)
# start = min(r, l)
# finish = max(l, r)
# for i in range(start + 1, finish):
#     a[i] = 0
# print(a)

#9
# a = [0, 1, 2, 3, 4, 5]
# n = int(input())
# chet = []
# nechet = []
# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         a[i] = a[i] * n
# print(a)

#10
# a = [0, 1, 2, 3, 4, 5]
# for i in range(0, len(a)):
#     if a[i] % 2 != 0:
#         a[i] = a[i] * 0
# print(a)


#11
# a = [0, 1, 2, 3, 4, 5]
# chet = []
# for i in range(0, len(a)):
#     if i % 2 == 0:
#         chet.append(a[i])
# rez = min(chet)
# print(rez)

#12
# a = [0, 8, 5, 3, 4, 5]
# rez = []
# cnt = 0
# for i in range(0, len(a) - 1):
#     if a[i] > a[i + 1]:
#         rez.append(i)
#         cnt += 1
# print(rez)
# print(cnt)

#13
# a = [0, 8, 5, 3, 4, 5]
# rez = []
# maxsum = 0
# maxel1 = 0
# maxel2 = 0
# for i in range(0, len(a) - 1):
#     if a[i] + a[i + 1] > maxsum:
#         maxsum = a[i] + a[i + 1]
#         maxel1 = a[i]
#         maxel2 = a[i + 1]
# sd = []
# sd.append(maxel1)
# sd.append(maxel2)
# print(sd)

#14
# a = [0, 8, 5, 3, 4, 5]
# minind = a.index(min(a))
# maxind = a.index(max(a))
# a[minind], a[maxind] = a[maxind], a[minind]
# print(a)

#15
# n, a, b = map(int, input().split())
# rez = [a, b]
# for i in range(2, n):
#     nexel = sum(rez)
#     rez.append(nexel)
# print(rez)
