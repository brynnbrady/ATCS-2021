import random
"""
Brynn Brady
AT CS - Ms. Namasivayam
February 16th 2022
TicTacToe

Current version: User vs. NPC with changeable difficulty levels tic tac toe
"""

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("This is a two player game. Take turns inserting X's and O's into the grid.")
        print("The first person to score three in a row of their symbol wins!")
        return

    def getDifficultyLevel(self):
        while(True):
            diffLevel = input("Select a difficulty level. Type 'easy', 'medium', or 'hard'")
            # return the depth of tree depending on the difficulty they want
            if diffLevel == "easy":
                return 3
            elif diffLevel == "medium":
                return 5
            elif diffLevel == "hard":
                return 7
            else:
                print("Bad input, try again")


    def print_board(self):
        # TODO: Print the board
        print()
        print("Current Board:")
        print("   ", "0", " ", "1", " ", "2")
        for i in range(3):
            for j in range(3):
                if j == 0:
                    print(i, "\t", end ="")
                print(self.board[i][j], "\t", end ="")
            print()
        return

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if (row > 2 or col > 2):
            return False
        elif (row < 0 or col < 0):
            return False
        elif self.board[row][col] == '-':
            return True
        else:
            return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        noInput = True
        while(noInput):
            row = int(input("What row do you choose?"))
            col = int(input("What column do you choose?"))
            if (self.is_valid_move(row, col)):
                noInput = False
                self.place_player(player, row, col)
            else:
                print("Bad input, try again")
        return

    def take_random_turn(self, player):
        goodInput = False
        while(not goodInput):
            randRow = random.randint(0, 2)
            randCol = random.randint(0, 2)
            if self.is_valid_move(randRow, randCol):
                self.place_player(player, randRow, randCol)
                goodInput = True
        return

    def minimax(self, player, depth):
        # base case
        if self.check_win("O"):
            return (10, None, None)
        elif self.check_win("X"):
            return (-10, None, None)
        elif self.check_tie():
            return (0, None, None)
        elif depth == 0:
            return (0, None, None)

        # recursive case
        if player == "O":
            best = -10000
            opt_row = -1
            opt_col = -1
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        # place the symbol, calc score, restore board to normal
                        self.place_player("O", row, col)
                        score = self.minimax("X", depth-1)[0]
                        self.place_player("-", row, col)
                        if score >= best:
                            opt_row = row
                            opt_col = col
                            best = score
            return (best, opt_row, opt_col)
        if player == "X":
            worst = 10000
            opt_row = -1
            opt_col = -1
            for row in range(3):
                for col in range(3):
                    if self.is_valid_move(row, col):
                        # place the symbol, calc score, restore board to normal
                        self.place_player("X", row, col)
                        score = self.minimax("O", depth-1)[0]
                        if score < worst:
                            worst = score
                            opt_row = row
                            opt_col = col
                        self.place_player("-", row, col)
            return (worst, opt_row, opt_col)

    def take_minimax_turn(self, player, depth):
        score, row, col = self.minimax(player, depth)
        self.place_player(player, row, col)
        return

    def take_turn(self, player, depth):
        # TODO: Simply call the take_manual_turn function
        print("Player ", player, ", it's your turn")
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_minimax_turn(player, depth)
        return

    def check_col_win(self, player):
        # TODO: Check col win
        for col in range(3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        for row in range(3):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if (self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player)):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "-":
                    return False
        if self.check_win("X") == False and self.check_win("O") == False:
            return True
        return False

    def play_game(self):
        # TODO: Play game
        self.print_instructions()
        depth = self.getDifficultyLevel()
        self.print_board()
        player = "X"
        keepPlaying = True
        while(keepPlaying):
            self.take_turn(player, depth)
            if self.check_win(player):
                keepPlaying = False
                print("Player, ", player, " wins!")
            elif self.check_tie():
                keepPlaying = False
                print("It's a tie!")
            if player == "X":
                player = "O"
            else:
                player = "X"
            self.print_board()
        print("Game Over")
        return

