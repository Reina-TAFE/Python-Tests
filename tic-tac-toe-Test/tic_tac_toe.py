from board import Board
class TicTacToe:
    def __init__(self):
        self.board = Board(3)
        self.players = [1, 2]
        self.rounds = 0

    def get_move(self, player):
        row = input('Enter row number: ')
        col = input('Enter col number: ')
        valid_move = False
        while not valid_move:
            try:
                row = int(row)
                col = int(col)
                valid_move = True
            except TypeError:
                print("invalid row or column number")
        position = (row, col)
        self.board.update_board_matrix((row, col), player)


    def play(self):
        while not self.board.check_win():
            for player in self.players:
                print(f"Player {player}'s turn!")
                self.get_move(player)
                self.rounds += 1
                self.board.show_board()
                if self.board.check_win():
                    print(f"Player {player} wins!")
                    quit()

