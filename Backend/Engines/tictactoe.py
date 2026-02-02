class TicTacToe:
    def __init__(self):
        self.board = ["","","","","","","","",""]
        self.next_move = "X"
        self.active = True
    
    def checkwinner(self):
        if self.board[0] != "" and self.board[0] == self.board[1] == self.board[2]:
            self.active = False
        elif self.board[3] != "" and self.board[3] == self.board[4] == self.board[5]:
            self.active = False
        elif self.board[6] != "" and self.board[6] == self.board[7] == self.board[8]:
            self.active = False
        elif self.board[0] != "" and self.board[0] == self.board[3] == self.board[6]:
            self.active = False
        elif self.board[1] != "" and self.board[1] == self.board[4] == self.board[7]:
            self.active = False
        elif self.board[2] != "" and self.board[2] == self.board[5] == self.board[8]:
            self.active = False
        elif self.board[0] != "" and self.board[0] == self.board[4] == self.board[8]:
            self.active = False
        elif self.board[2] != "" and self.board[2] == self.board[4] == self.board[6]:
            self.active = False

    def make_move(self, position):
        if self.board[position-1] != "":
            print("Somebody has alread gone there")
            return
        self.board[position-1] = self.next_move
        if self.next_move == "X":
            self.next_move = "O"
        else:
            self.next_move = "X"
        print(self.board)
        self.checkwinner()

t = TicTacToe()