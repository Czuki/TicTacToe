import board  # import board.py file to have acces to a code inside
import game_logic  # import game_logic.py file


def round(symbol, plansza):  # function for playing each round symbol is an 'X' OR 'O' string
    board.show_board(plansza)  # shows board
    game_logic.player_move(symbol, plansza)  # goes to the game_logic.py file and opens player_move function
    return game_logic.win_check(symbol, plansza) #returns True/False If True = player has won and game ends through break statements in lines 16 or 18


def run_game():
    plansza = board.draw_board()
    round('X', plansza)         #total of 9 moves possible we start with 'X'
    for i in range(4):          #last 8 moves nested in for loop
        if round('O', plansza):
            break
        if round('X', plansza):
            break
    board.show_board(plansza)   #draws board after game is over


if __name__ == "__main__":  #ensures run_game is run only if module is being run directly
    run_game()
