def win_check(symbol, plansza):
    if plansza[0][0] == [symbol] and plansza[0][1] == [symbol] and plansza[0][2] == [symbol] or plansza[1][0] == [
        symbol] and plansza[1][1] == [symbol] and plansza[1][2] == [symbol] or plansza[2][0] == [symbol] and plansza[2][
        1] == [symbol] and plansza[2][2] == [symbol] or plansza[0][0] == [symbol] and plansza[1][0] == [symbol] and \
            plansza[2][0] == [symbol] or plansza[0][1] == [symbol] and plansza[1][1] == [symbol] and plansza[2][1] == [
        symbol] or plansza[0][2] == [symbol] and plansza[1][2] == [symbol] and plansza[2][2] == [symbol] or plansza[0][
        0] == [symbol] and plansza[1][1] == [symbol] and plansza[2][2] == [symbol] or plansza[2][0] == [symbol] and \
            plansza[1][1] == [symbol] and plansza[0][2] == [symbol]:
        print(f'[{symbol}] in line! Player [{symbol}] wins!')
        return True


# if statements responsible for checking if any of the symbols is in line of 3

def player_move(symbol, plansza):  # one function for both players 'symbol' can be 'X' or 'O'
    print(f'Player: {symbol} move: ')
    choice = input('Select field: 1-9 ')  # 1-9 starting from top left corner of 3x3 board
    i = 0  # row index
    j = 0  # column index
    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8',
                      '9']:  # with this line we are safe from inputs different than expected
        print(
            'Wrong move!')  # if player input is not in given list in line19, player_move function will initiate again from the beginning
        player_move(symbol, plansza)
    if choice == '1':  # choice selection top-left
        i = 0
        j = 0
    if choice == '2':  # top-mid
        i = 0
        j = 1
    if choice == '3':  # top-right
        i = 0
        j = 2
    if choice == '4':  # mid- left
        i = 1
        j = 0
    if choice == '5':  # center
        i = 1
        j = 1
    if choice == '6':  # mid- right
        i = 1
        j = 2
    if choice == '7':  # bottom-left
        i = 2
        j = 0
    if choice == '8':  # bottom-mid
        i = 2
        j = 1
    if choice == '9':  # bottom-right
        i = 2
        j = 2
    if plansza[i][j] != [' ']:  # checks if selected field is already taken.
        print('Place taken, please try again')
        player_move(symbol, plansza)  # if selected field is taken, player_move executes again
    else:
        plansza[i][j] = [symbol]  # if selected field is free [symbol] of a player in turn is inserted
    return plansza
