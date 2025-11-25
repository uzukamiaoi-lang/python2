#1
# a,b,c=map(int,input().split())
# V=a*b*c
# S=2*(a*b+b*c+a*c)
# print(V,S)


# 2
# R=int(input())
# L=2*math.pi*R
# S=math.pi*R**2
# print(L,S)

#3
# a, b = map(int, input().split())
# c = math.sqrt(a ** 2 + b ** 2)
# P = a + b + c
# print(c, P)


#4
# R1,R2=map(int,input().split())
# S1=math.pi*R1**2
# S2=math.pi*R2**2
# S3=S1-S2
# print(S3)

#5
# x1,y1,x2,y2=map(int,input().split())
# st1=x2-x1
# st2=y2-y1
# S=st1*st2
# P=2*(st1+st2)
# print(S,P)

#6
# x1,y1,x2,y2=map(int,input().split())
# f=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(f)

#7
# def rast(a1, a2, b1, b2):
#     liner = math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)
#     return liner
#
#
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# st1 = rast(x1, x2, y1, y2)
# st2 = rast(x2, x3, y2, y3)
# st3 = rast(x1, x3, y1, y3)
# polper = (st1 + st2 + st3) / 2
# Per = st1 + st2 + st3
# S = math.sqrt(polper * (polper - st1) * (polper - st2) * (polper - st3))
# print(Per, S)

#8
# tempF = int(input())
# tempC = (tempF - 32) * 5 / 9
# print(tempC)


#9
# for i in range(50):
#     x, a, y, b = map(int, input().split())
#     choc = 1 * a
#     iris = 1 * b
#     raz = choc / iris
#     print(choc, iris, raz)


#10
# a1, a2, b1, b2, c1, c2 = map(int, input().split())
# d = a1 * b2 - a2 * b1
# x = (c1 * b2 - c2 * b1) / d
# y = (a1 * c2 - a2 * c1) / d
# print(x, y)

#11
# alf = int(input())
# alfrad = alf * math.pi / 180
# print(alfrad)


#12
# v1, v2, pyt, t = map(int, input().split())
# s2 = t * (v1 + v2)
# obS = pyt + s2
# print(obS)

#13
# a, b, c = map(int, input().split())
# ac = abs(c - a)
# bc = abs(c - b)
# sums = ac + bc
# print(ac, bc, sums)


#14
# a, b = map(int, input().split())
# a2 = a ** 2
# b2 = b ** 2
# sums = a2 + b2
# razn = a2 - b2
# proiz = a2 * b2
# dels = a2 / b2
# print(sums, razn, proiz, dels)

#15
# vtech, vkater, t1, t2 = map(int, input().split())
# s1 = vkater * t1
# s2 = (vkater - vtech) * t2
# S = s1 + s2
# print(S)
