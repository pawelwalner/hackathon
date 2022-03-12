print('Tu Twoja ksiażka adresowa. Podaj komendę, aby skorzystać z moich funkcji: \n '
      '1. show <- Pokażę Ci wszystkie Twoje kontakty \n '
      '2. add <- Stworzę nowy kontakt \n '
      '3. remove <- Usunę wybrany kontakt \n '
      '4. exit <- Pożegnamy się tu i teraz. \n')

user_action = 0
address_book = [
    [1, 'Paweł', 'Walner', '+48600200300', 'test5@wp.pl'],
    [2, 'Piotr', 'Wu', '+48603200300', 'test4@wp.pl'],
    [3, 'Ewa', 'Zet', '+48604200300', 'test3@wp.pl'],
    [4, 'Łukasz', 'Igrek', '+48605200300', 'test2@wp.pl'],
    [5, 'Paweł', 'Iks', '+48606200300', 'test1@wp.pl'],
]

while user_action != 'exit':
    user_action = input('Twoja komenda to ---> ')

# Wyświetlanie wszystkich wpisów:
    if user_action == 'show':
        for element in address_book:
            print(f'ID: {element[0]} Imię: {element[1]} Nazwisko: {element[2]} Telefon: {element[3]} Email: {element[4]}')
            print('--- --- --- --- ---')

# Tworzenie nowego kontaktu
    elif user_action == 'add':
        last_id = address_book[-1][0]
        first_name = input('Podaj imię kontaktu: ')
        last_name = input('Podaj nazwisko kontaktu: ')
        phone = input('Podaj numer telefonu kontaktu: ')
        email = input('Podaj adres email kontaktu: ')
        new_contact = [last_id + 1, first_name, last_name, phone, email]
        address_book.append(new_contact)
        print(f'Kontakt {first_name} {last_name} został pomyślnie dodany do Twojej listy kontaktów')

# Usunięcie kontaktu
    elif user_action == 'remove':
        print('Poniżej podaję listę kontaktów wraz z numerem ID')
        for element in address_book:
            print(f'{element[1]} {element[2]} - numer ID ---> {element[0]}')


        remove_id = int(input('Podaj numer ID kontaktu, który chcesz usunąć:'))
        entries_counter = address_book[-1][0]


        if remove_id - 1 in range(entries_counter):
            first_name_to_remove = address_book[remove_id - 1][1]
            last_name_to_remove = address_book[remove_id - 1][2]
            print(f'Kontakt {first_name_to_remove} {last_name_to_remove} został usunięty z Twojej książki adresowej')
            address_book.pop(remove_id - 1)
        else:
            print('Podałeś ID, które nie znajduje się na liście - żaden z kontaktów nie został usunięty.')

    continue