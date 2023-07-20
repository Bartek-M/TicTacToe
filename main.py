# Simple TicTacToe game
import os


class Game:
    def __init__(self):
        self.board = [[i for i in range(1, 10)][3*j:3*(j+1)] for j in range(3)]
        self.winner = "player"
        self.turn = 0

        while True:
            self.draw_board()
            run = self.player_move()

            if run:
                break

        self.print_win()

    def _clear(self):
        os.system("clear")
        print("TIC TAC TOU GAME\n")

    def draw_board(self, win=False):
        self._clear()
        drawn = "Board:\n"

        for y, row in enumerate(self.board):
            for x, item in enumerate(row):
                if win and item not in ["X", "O"]:
                    item = "-"

                drawn += f" {item} |" if x != 2 else f" {item} "

            drawn += f"\n{'-'*11}\n" if y != 2 else "\n"

        print(drawn)

    def print_win(self):
        self.draw_board(True)
        print("Result:", self.winner)

    def check_valid(self, pos):
        if not (0 <= pos <= 8):
            return False

        if self.board[pos//3][pos-(pos//3 * 3)] in ["X", "O"]:
            return False

        return True

    def check_win(self):
        # Rows
        for row in self.board:
            check = [item for item in row]

            if check.count("X") == len(check) or check.count("O") == len(check):
                self.winner = f"player {'X' if check[0] == 'X' else 'O'} won"
                return True

        # Cols
        for x in range(len(self.board[0])):
            check = [self.board[y][x] for y in range(len(self.board))]

            if check.count("X") == len(check) or check.count("O") == len(check):
                self.winner = f"player {'X' if check[0] == 'X' else 'O'} won"
                return True

        # Diagonals
        check_1 = []
        check_2 = []

        for i in range(len(self.board)):
            check_1.append(self.board[i][i])
            check_2.append(self.board[-i-1][i])

        if check_1.count("X") == len(check_1) or check_1.count("O") == len(check_1):
            self.winner = f"player {'X' if check_1[0] == 'X' else 'O'} won"
            return True
        if check_2.count("X") == len(check_2) or check_2.count("O") == len(check_2):
            self.winner = f"player {'X' if check_2[0] == 'X' else 'O'} won"
            return True

        # Draw
        if self.turn == 9:
            self.winner = "DRAW"
            return True

        # NOTHING
        return False

    def player_move(self):
        player = "X" if self.turn % 2 == 0 else "O"
        move = int(input(f"[{player}] Pick available space: ")) - 1

        while not self.check_valid(move):
            move = int(input(f"[{player}] Wrong position! Pick available space: ")) - 1

        self.board[move//3][move-(move//3 * 3)] = player
        self.turn += 1
        return self.check_win()


if __name__ == "__main__":
  Game()