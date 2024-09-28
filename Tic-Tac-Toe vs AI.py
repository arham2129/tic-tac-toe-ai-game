from easyAI import TwoPlayerGame, AI_Player, Negamax  
from easyAI.Player import Human_Player 

class TicTacToe(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.board = [0] * 9  
        self.current_player = 1  
    def possible_moves(self):
        return [i + 1 for i in range(9) if self.board[i] == 0]
    def make_move(self, move):
        self.board[move - 1] = self.current_player
    def unmake_move(self, move):
        self.board[move - 1] = 0
    def lose(self):
        lines = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],  
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],  
            [1, 5, 9],
            [3, 5, 7],
        ]
        for line in lines:
            if all(self.board[pos - 1] == self.opponent_index for pos in line):
                return True
        return False
    def is_over(self):
        return not self.possible_moves() or self.lose()
    def show(self):
        symbols = {0: '.', 1: 'X', 2: 'O'}
        board_display = "\n".join(
            " ".join(symbols[self.board[3 * row + col]] for col in range(3))
            for row in range(3)
        )
        print("\n" + board_display + "\n")
    def scoring(self):
        if self.lose():
            return -100
        if not self.possible_moves():
            return 0
        return 0
    def end_message(self):
        if self.lose():
            if self.current_player == 1:
                print("Game is over. The AI wins!")
            else:
                print("Game is over. Human wins!")
        elif not self.possible_moves():
            print("Game is over. It's a draw!")
if __name__ == "__main__":
    ai_algo = Negamax(6)
    game = TicTacToe([Human_Player(), AI_Player(ai_algo)])
    while not game.is_over():
        game.show()
        move = int(input("Your move (1-9) = "))
        if move in game.possible_moves():
            game.make_move(move)
            if not game.is_over():
                game.current_player = 2  
                game.play()  
                game.current_player = 1  
        else:
            print("invalid move try again")
    game.show()
    game.end_message()  