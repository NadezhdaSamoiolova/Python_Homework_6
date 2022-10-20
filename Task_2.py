### Task 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#### Вариант решения 1 (список изначально  задан) ###########

# numbers = [2, 3, 4, 5, 6]
# list = []
# for i in range(len(numbers)):
#     if i < len(numbers) / 2:
#         list.append(numbers[i] * numbers[-i-1])
# print(list)

#### Вариант с lambda-фукцией и enumerate

numbers = [2, 3, 4, 5, 6]
res = lambda numbers: [value * numbers[index * -1 -1] for index, value in enumerate(numbers) if index < len(numbers) / 2]

print(res(numbers))
