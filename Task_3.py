### Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

numbers = input("Введите список числел, разделенных пробелом: ").split()
numbers_int = list(map(int, numbers))
print(numbers_int)
print('Ваше наибольшее число из списка: ', max(numbers_int))
print('Ваше наименьшее число из списка: ', min(numbers_int))
