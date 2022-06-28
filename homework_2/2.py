lst = list(input("Введите значения:"))

for el in range(1, len(lst), 2):
    lst[el], lst[el - 1] = lst[el - 1], lst[el]

print(lst)

