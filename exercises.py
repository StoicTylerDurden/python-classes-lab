class Game:
    def __init__(self, turn='X', tie=False, winner=None, board=None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
        }


    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)


    def get_move(self):
        while True:
            move = input(f"It's player {self.turn}'s turn, Enter a valid move (example: A1): ").lower().strip()

            if (move in self.board) and (self.board[move] is None):
                self.board[move] = self.turn
                if self.turn == "X":
                    self.turn = "O"
                elif self.turn == "O":
                    self.turn = "X"
                break
            else:
                print("Invalid move. Try again.")


    def play_game(self):
        print("Welcome to Tic-Tac-Toe Game Shall We play? ")
        while True:
            self.print_board()

            if (self.winner):
                print(f"The Winner is {self.winner}")
                return
            elif (self.tie):
                print("It's a tie!")
                return
        
            self.get_move()
            self.check_for_winner()
    

    def check_for_winner(self):
        letters = "abc"
        for i in range(3):
            # Check for horizontal win
            if self.board[f"{letters[i]}1"] == self.board[f"{letters[i]}2"] == self.board[f"{letters[i]}3"] != None:
                self.winner = self.board[f"{letters[i]}1"]
                return True
    
            # Check for vertical win
            if self.board[f"a{i+1}"] == self.board[f"b{i+1}"] == self.board[f"c{i+1}"] != None:
                self.winner = self.board[f"a{i+1}"]
                return True
    
        # Check for diagonal win
        if self.board["a1"] == self.board["b2"] == self.board["c3"] != None:
            self.winner = self.board["a1"]
            return True
    
        if self.board["a3"] == self.board["b2"] == self.board["c1"] != None:
            self.winner = self.board["a3"]
            return True

        # Check if there's a tie
        for key, value in self.board.items():
            if value is None:
                return False
        self.tie = True
    
        return False


        

game_instance = Game()
game_instance.play_game()


        
