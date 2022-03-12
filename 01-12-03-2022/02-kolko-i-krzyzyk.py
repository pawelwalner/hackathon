


user_x = 'x'
user_o = 'o'

board = [
    [' ', '1', ' ', '2', ' ', '3'],
    ['A', '_', '|', '_', '|', '_'],
    ['B', '_', '|', '_', '|', '_'],
    ['C', '_', '|', '_', '|', '_']
]

for row in board:
    print(row[0], row[1], row[2], row[3], row[4], row[5])


A1 = board[1][1]
A2 = board[1][3]
A3 = board[1][5]
B1 = board[2][1]
B2 = board[2][3]
B3 = board[2][5]
C1 = board[3][1]
C2 = board[3][3]
C3 = board[3][5]

available_fields = [A1, A2, A3, B1, B2, B3, C1, C2, C3]

# import random
#
# first_user = user_o, user_x
# first_user = random.choice(first_user)

print('Zaczyna gracz o')
move = input('Podaj pole, na którym chcesz postawić swój znak.')

while move != 'exit':
    if move == 'A1':
        board.insert(1, 'o')
        available_fields.remove(A1)

for row in board:
    print(row[0], row[1], row[2], row[3], row[4], row[5])


# należy określić kiedy jest winner, 8 kombinacji wygranej

winner_scheme_1 = A1 == A2 == A3
winner_scheme_2 = B1 == B2 == B3
winner_scheme_3 = C1 == C2 == C3
winner_scheme_4 = A1 == B1 == C1
winner_scheme_5 = A2 == B2 == C2
winner_scheme_6 = A3 == B3 == C3
winner_scheme_7 = A1 == B2 == C3
winner_scheme_8 = A3 == B2 == C1

# należy określic czy dane pole jest zajęte, jeżeli zostało właśnie zajęte to nalezy je usunąć z możliwości dodania





# poruszamy się w
# row 1
# row 3
# row 5



