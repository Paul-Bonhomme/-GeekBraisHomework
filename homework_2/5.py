
my_list = [7, 5, 3, 3, 2]
num = int(input("Введите натуральное число:"))

for el in my_list:
    if el == num:
        my_list.insert(el + 1, num)
        print(my_list)
        break





