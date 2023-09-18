import sys
def write_txt(filename, phone_book):
    with open('phonebook.txt', 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')
            
def show_menu():
    print('1 - Распечатать справочник',
        '2 - Найти телефон по фамилии',
        '3 - Изменить номер телефона',
        '4 - Удалить запись',
        '5 - Найти абонента по номеру телефона',
        '6 - Добавить абонента в справочник',
        '7 - Найти по имени',
        '8 - Изменить имя',
        '9 - Изменить Фамилию',
        '10 - Закончить работу', sep = '\n')
    choice = int(input("Введите ваш выбор: "))
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while(choice > 0 and choice < 11):
        if choice == 1:
            print_phonebook(phone_book)
            input('\nНажмите Enter для продолжения\n')
        elif choice == 2:
            last_name = input('Фамилия: ')
            print(find_by_lastname(phone_book, last_name))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 3:
            last_name = input('Фамилия: ')
            new_number = input('Новый номер: ')
            print(change_number(phone_book,last_name,new_number))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 4:
            last_name = input('Фамилия: ')
            print(delete_by_lastname(phone_book, last_name))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 5:
            number = input('Номер: ')
            print(find_by_number(phone_book, number))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 6:
            user_data = input('Введите данные: ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
            input('\nНажмите Enter для продолжения\n')
        elif choice == 7:
            first_name = input('Имя: ')
            print(find_by_firstname(phone_book, first_name))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 8:
            last_name = input('Фамилия: ')
            new_name = input('Новое имя: ')
            print(change_firstname(phone_book, last_name, new_name))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 9:
            last_name = input('Фамилия: ')
            new_lastname = input('Новая фамилия: ')
            print(change_lastname(phone_book, last_name, new_lastname))
            input('\nНажмите Enter для продолжения\n')
        elif choice == 10:
            print("\nВыход из программы!")
            input('Нажмите Enter для ВЫХОДА\n')
            sys.exit()
        choice = show_menu()

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия' ,'Имя' ,'Телефон' ,'Описание']
    with open('phonebook.txt', 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book

def print_phonebook(phone_book):
    for i in phone_book:
        print(i)

def find_by_lastname(phone_book, last_name):
    for i in phone_book:
        if last_name in i['Фамилия']:
            return 'Телефон: ' + i['Телефон']
    return 'Такой фамилии нет в справочнике!\n'
        
def change_number(phone_book,last_name,new_number):
    temp = 0
    for i in phone_book:
        if last_name in i['Фамилия']:
            temp = i['Телефон']
            i['Телефон'] = new_number
            return f"Старый телефон {temp} сменен на новый {i['Телефон']}"
    return 'Такой фамилии нет в справочнике!\n'

def delete_by_lastname(phone_book, last_name):
    for i in phone_book:
        if last_name in i['Фамилия']:
            phone_book.remove(i)
            return "Запись удалена"
    return 'Такой фамилии нет в справочнике!\n'

def find_by_number(phone_book, number):
    for i in phone_book:
        if number in i['Телефон']:
            return i['Фамилия']
    return 'Такого телефона нет в справочнике!\n'
    
def add_user(phone_book, user_data):
    fields = ['Фамилия' ,'Имя' ,'Телефон' ,'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    return phone_book

def find_by_firstname(phone_book, first_name):
      for i in phone_book:
        if first_name in i['Имя']:
            return 'Телефон: ' + i['Телефон']
      return 'Такого имени нет в справочнике!\n'

def change_firstname(phone_book, last_name, new_name):
    temp = 0
    for i in phone_book:
        if last_name in i['Фамилия']:
            temp = i['Имя']
            i['Имя'] = new_name
            return f"Старое имя {temp} сменено на новое {i['Имя']}"
    return 'Такой фамилии нет в справочнике!\n'

def change_lastname(phone_book, last_name, new_lastname):
    temp = 0
    for i in phone_book:
        if last_name in i['Фамилия']:
            temp = i['Фамилия']
            i['Фамилия'] = new_lastname
            return f"Старая фамилия {temp} сменена на новую {i['Фамилия']}"
    return 'Такой фамилии нет в справочнике!\n'




work_with_phonebook()