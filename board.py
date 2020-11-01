def show_board(plansza):  # draws a board which is held in a list of lists
    for i in range(3):
        for j in range(3):
            print(plansza[i][j],
                  end='')  # empty 'end' argument in print statement to avoid printing new line when drawing rows
        print('\n')  # new line after full row is drawn


def draw_board():  # creates a board as a list of lists
    # each field is a single empty space by default
    return [[[' '], [' '], [' ']], [[' '], [' '], [' ']], [[' '], [' '], [' ']]]
