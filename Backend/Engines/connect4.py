class Connect4:
    def __init__(self):
        self.board = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
        self.next_move = "R"
    
    def make_move(self, col):
        i = 0
    
    def display_board(self):
        for row in self.board:
            print(row)


c = Connect4()
c.make_move(0)