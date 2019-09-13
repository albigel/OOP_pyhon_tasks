# Задача 4
# Создать список чисел меньших 2500, оканчивающихся на 1 и являющихся квадратами целых чисе
print(list(map(lambda x: x ** 2, filter(lambda x: 1 if ((x % 10 == 1) or (x % 10 == 9)) else 0, range(1, 50)))))

# Задача 3
# Написать в одну строчку обращение словаря
a = dict(i=1, j=2, k=3)
print({a[i]: i for i in a.keys()})


# Задача 2
def bbbl_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Задача 1
min_ = float("inf")
max_ = -float("inf")
average = 0
sqr_average = 0
len_ = 0
while True:
    inpt = input()
    if inpt == 'End':
        print({'avrg': average, 'min': min_, 'max': max_, 'stdev': (sqr_average - average ** 2) ** 0.5})
        break
    else:
        len_ += 1
        inpt = float(inpt)
        min_ = inpt if inpt < min_ else min_
        max_ = inpt if inpt > max_ else max_
        average = (average * (len_ - 1) + inpt) / len_
        sqr_average = (sqr_average * (len_ - 1) + inpt ** 2) / len_
