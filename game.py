import board
import game_logic

def round(symbol, plansza):
	board.show_board(plansza)
	game_logic.player_move(symbol, plansza)
	win = False
	if game_logic.win_check(symbol, plansza) == True:
		win = True
	return win

def run_game():

	plansza = board.draw_board()
	round('X', plansza)
	for i in range(4):
		if round('O', plansza) == True:
			print(f'\'O\' in line Player 2 Wins!')
			break
		if round('X', plansza) == True:
			print(f'\'X\' in line Player 1 Wins!')
			break
	board.show_board(plansza)

if __name__ == "__main__":
	run_game()
