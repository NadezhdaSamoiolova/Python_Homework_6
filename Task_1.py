# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#### Вариант решения 1 (список изначально  задан) ###########

# numbers = [2, 3, 5, 9, 3]
# sum_digits = 0
# # print(len(numbers))
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         sum_digits += numbers[i]
# print(sum_digits)


### Вариант решения с List Comprehesion и lambda-фукцией
list_1 = [2, 3, 5, 9, 3]
data = [list_1[i] for i in range(1, len(list_1), 2)]
print(data)

res = lambda data: [(data[i] + data[i + 1]) for i in range(len(data)) if (i + 1) < len(data)]
print(res(data))
