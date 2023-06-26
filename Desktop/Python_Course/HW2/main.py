# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while


# Input:       5

# Output:    120

# print("Введите число N:")
# N = int(input())
# f = 1
# if(N < 0):
#     print("Число отрицательное")    
# while N > 0:
#     f *= N
#     N -= 1
#     print(f)
    
    
#     Альтернативное решение
#     def factorial(n):
#    i = 1
#    fact = 1
#    while i <= n:
#        fact *= i
#        i += 1
#    return fact


# ещё одно

# n = int(input())
#
# count = 1
# fact = 1
# while count <= n:
#     fact = fact*count
#     count += 1
#
# print(fact)

# num = 0
# result = factorial(num)
# print(result)
    
    
    
#     Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
#     Если А не является числом Фибоначчи, выведите число -1.

# Input:     5

# Output:  6


# print("Введите число N:")
# A = int(input())
# n = 0
# c = 1
# count = 0

# if (A < 0):
#     print("Число отрицвательное")
# else:   
#     if A == 0:
#         print(1)
#     else:
#         while n < A:
#            while (c < n):
#             n, c = c, n + c
#             count += 1
#             print(n, count)
#         if(A == n):
#             print("ТОчка на позиции =", count)
#         else:
#             print(" ")
#             print("-1")


# Альтернативное решение 

# a = int(input())

# n0=0
# n1=1
# n2 = n1+n0
# count = 2

# while n2 < a:
#     n2 = n1 + n0
#     n0, n1 = n1, n2
#     count+=1
#     if n2 == a:
#         print(count)
#         break
# else:
#     print(-1)

# Задача№13: Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2


# a = 0
# min_t = 0
# max_t = 0

# print("Введите число N:")
# N = int(input())
# if (1 <= N <= 100):
#     print("Число верное")
#     while a < N:
#         print("Введите температуру x:")
#         x = (input())
#         if (x < 0):
#             min_t +=1
#         else:
#             min_t = 0
#         if (min_t > max_t):
#             max_t = min_t
#         a += 1
    
#         print(x)
#         a  += 1
#     print("Количество дней подряд:", max_t)
# else:
#     print("Число дней не в заданном промежутке")


# Или так

# from random import randint
# n = int(input())
# cur_plus = 0
# max_plus = 0
# for i in range(n):
#     temp = randint(-40, 40)
#     print(temp, end=" ")
#     if temp>0:
#         cur_plus += 1
#     else:
#         if cur_plus>max_plus:
#             max_plus = cur_plus
#         cur_plus = 0

# if cur_plus>max_plus:
#     max_plus = cur_plus

# print(f"\n{max_plus}")

# Альетрнативное решение

# from random import randint
# n = int(input())
# cur_plus = 0
# max_plus = 0
# for i in range(n):
#     temp = randint(-40, 40)
#     print(temp)
#     if temp>0:
#         cur_plus += 1
#     else:
#         if cur_plus>max_plus:
#             max_plus = cur_plus
#         cur_plus = 0

# if cur_plus>max_plus:
#     max_plus = cur_plus

# print(max_plus)
    
    
    # 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
    # Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
    # Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
    # Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. 
    # Здесь каждое число – это масса соответствующего арбуза
    
    # Input:	5 -> 5 1 6 5 9
    # Output:	1 9

# from random import randint

# n = int(input("ВВедите число N:"))

# mass_water = randint(0,20)
# min_n = mass_water
# max_n = mass_water

# for i in range(n-1):
#     mass_water = randint(1,20)
#     print(mass_water)
#     if mass_water>max_n:
#         max_n = mass_water
#     elif mass_water<min_n:
#         min_n = mass_water
# print(min_n,max_n)

# НОД и НОК


# a = 4
# b = 6
# nod = 0
# nok = 0

# flag = False
# for i in range(2, min(a, b)):
#     if a % i == 0 and b % i == 0:
#         nod = i
#         if flag:
#             continue
#         else:
#             nok = i
#             flag = True

# print(f"НОК = {nok}")
# print(f"НОД = {nod}")