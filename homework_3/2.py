def info(name, surname, data_birthday, city, email, phone):
    return f"Имя: {name} ", \
           f"Фамилия: {surname}, " \
           f"Дата рождения: {data_birthday}, " \
           f"Город: {city}, " \
           f"Почта: {email}, " \
           f"Телефон: {phone}"


print(info(name='Pavel', surname='Dobryakov', data_birthday='30.08.02', city='Volgograd', email='paul_bonhomme@mail.ru',
           phone=79020951963,))
