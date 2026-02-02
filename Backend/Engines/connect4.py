class Connect4:
    def __init__(self):
        self.board = [["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
        self.next_move = "R"

c = Connect4()
for row in c.board:
    print(row)