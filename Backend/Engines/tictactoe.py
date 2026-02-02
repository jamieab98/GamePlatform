class TicTacToe:
    def __init__(self):
        self.board = ["","","","","","","","",""]
        self.next_move = "X"
        self.active = True
        print(self.board)

    def make_move(self, position):
        self.board[position-1] = self.next_move
        if self.next_move == "X":
            self.next_move = "O"
        else:
            self.next_move = "X"
        print(self.board)

t = TicTacToe()
t.make_move(1)
t.make_move(2)