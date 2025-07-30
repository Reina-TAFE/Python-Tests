class Board:
    def __init__(self, size):
        E0 = 0 # default value for un-played position
        P1 = 1 # value for player 1
        P2 = 2 # value for player 2
        self.size = size
        self.board_matrix = [[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]

    def generate_board(self, board_size):
        board = [([0]*board_size)]*board_size
        # format_board = [(["-"]*board_size)]*board_size
        return board

    def check_win(self):
        win_conditions = [([1]*self.size), ([2]*self.size)]
        for row in range(self.size):
            #check row
            if self.board_matrix[row] in win_conditions:
                return True
            #check column
            elif list(map(lambda x: self.board_matrix[x][row], list(range(self.size)))) in win_conditions:
                return True
            #check diagonal
            elif list(map(lambda x: self.board_matrix[x][x], list(range(self.size)))) in win_conditions:
                return True
            #if this point is reached, win condition is not met
            else:
                return False

    def update_board_matrix(self, position, value):
        check_available = lambda x: self.board_matrix[x[0]][x[1]] not in [1, 2]
        if check_available(position):
            self.board_matrix[position[0]][position[1]] = value
        else:
            print("Position already taken")
        return

    def show_board(self):
        # format_board = [(["-"]*self.size)]*self.size
        format_board = [['-', '-', '-'],
                        ['-', '-', '-'],
                        ['-', '-', '-']]
        for row in range(self.size):
            for col in range(len(self.board_matrix[row])):
                if (self.board_matrix[row])[col] == 1:
                    (format_board[row])[col] = "X"
                elif (self.board_matrix[row])[col] == 2:
                    (format_board[row])[col] = "O"
                else:
                    (format_board[row])[col] = "-"
            print(format_board[row])


def make_guess(board):
    row = int(input("row: "))
    column = int(input("column: "))
    player = int(input("player: "))
    position = (row, column)
    board.update_board_matrix(position, player)
    board.show_board()
    return
