class Connect4:
    def __init__(self):
        self.board = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
        self.next_move = "R"
    
    def make_move(self, col):
        i = 6
        #Check the bottom of the column first. If that spot is occupied, move up. If it is not, place the coin there. If it reaches the top of the board, display the move was invalid and try again.
    
    def display_board(self):
        for row in self.board:
            print(row)


c = Connect4()
c.make_move(0)