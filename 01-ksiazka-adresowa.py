# Książka adresowa:
# Program przechowujący danę kontaktowe znajomych/klientów.
#
# - program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
#   - Wyświetlenie wszystkich wpisów
#   - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
#   - Usunięcie wpisu
#   - Zakończenie pracy programu
# - Program powinien na starcie mieć już wprowadzone kilka wpisów.


print('Tu Twoja ksiażka adresowa. Podaj komendę, aby skorzystać z moich funkcji: \n  1. show_all <- Pokażę Ci wszystkie Twoje kontakty \n 2. create_new <- Stworzę nowy kontakt \n 3. remove')

address_book = [
    [1, 'Paweł', 'Walner', '+48600200300', 'test5@wp.pl'],
    [2, 'Piotr', 'Wu', '+48603200300', 'test4@wp.pl'],
    [3, 'Ewa', 'Zet', '+48604200300', 'test3@wp.pl'],
    [4, 'Łukasz', 'Igrek', '+48605200300', 'test2@wp.pl'],
    [5, 'Paweł', 'Iks', '+48606200300', 'test1@wp.pl'],
]


# wyświetlanie wszystkich wpisów:
for element in address_book:
    print(f'ID: {element[0]} Imię: {element[1]} Nazwisko: {element[2]} Telefon: {element[3]} Email: {element[4]}')
    print('--- --- --- --- ---')

# Tworzenie nowego kontaktu

last_id = address_book[-1][0] # czy może lepiej dać len(address_book) ?
first_name = input('Podaj imię kontaktu: ')
last_name = input('Podaj nazwisko kontaktu: ')
phone =  input('Podaj numer telefonu kontaktu: ')
email = input('Podaj adres email kontaktu: ')
new_contact = [last_id + 1, first_name, last_name, phone, email]
address_book.append(new_contact)
print(f'Kontakt {first_name} {last_name} został pomyślnie dodany do Twojej listy kontaktów')

# usunięcie wpisu
print('Poniżej podaję listę kontaktów wraz z numerem ID')
for element in address_book:
    print(f'{element[1]} {element[2]} - numer ID: {element[0]}')


remove_id = int(input('Podaj numer ID kontaktu, który chcesz usunąć:'))
index_entries_in_address_book = address_book[-1][0] - 1
print(index_entries_in_address_book)

if remove_id - 1 in range(index_entries_in_address_book):
    first_name_to_remove = address_book[remove_id - 1][1]
    last_name_to_remove = address_book[remove_id - 1][2]
    print(f'Kontakt {first_name_to_remove} {last_name_to_remove} został usunięty z Twojej książki adresowej')
    address_book.pop(remove_id - 1)
else:
    print('Podałeś ID, które nie znajduje się na liście - żaden z kontaktów nie został usunięty.')