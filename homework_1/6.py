start_km = float(input('Enter the starting value:'))
finish_km = float(input('Enter the desired value:'))
day = 0

while start_km <= finish_km:
    every_day = start_km / 10
    start_km += every_day
    print(f"Количество дней: {day}")
    day += 1