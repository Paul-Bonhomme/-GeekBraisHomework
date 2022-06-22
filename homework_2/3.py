number = int(input('Enter the number (1-12):'))

lst = ['Зима', 'Весна', 'Лето', 'Осень']
month = {1: lst[0], 2: lst[0], 3: lst[1], 4: lst[1], 5: lst[1], 6: lst[2], 7: lst[2], 8: lst[2], 9: lst[3],
         10: lst[3], 11: lst[3], 12: lst[0]}

print(f"Время года:",month[number])