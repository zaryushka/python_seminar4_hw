# Задача 24
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
n = int(input('введите количество кустов на грядке:'))
a = list(map(int, input('введите колчество ягод на каждом кусте через пробел:').split()))
max = a[-2] + a[-1] + a[0]
for i in range(len(a) - 1):
    if a[i-1] + a[i] + a[i+1] > max:
        max = a[i-1] + a[i] + a[i+1]
print(max)