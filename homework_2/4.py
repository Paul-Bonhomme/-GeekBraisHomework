
stroka = input('Введите строку,разделенную пробелами:').strip().split()

for el in enumerate(stroka):
    print(f"{el[0]})", el[1])