import random

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = {player1: 0, player2: 0}
        self.winner = None

    def announce_winner(self, player):
        if self.winner is None:
            self.winner = player
            print(f"The winner is {player}!")
        else:
            raise Exception("Game already has a winner.")

    def update_score(self, player, points):
        if player in self.score:
            self.score[player] += points
        else:
            raise Exception("Player not found in the game.")

class CoinToss(Game):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)

    def play_round(self):
        toss = random.choice(["Heads", "Tails"])
        print(f"Coin toss result: {toss}")

        if toss == "Heads":
            self.update_score(self.player1, 1)
        else:
            self.update_score(self.player2, 1)

        print(f"Score: {self.player1} = {self.score[self.player1]}, {self.player2} = {self.score[self.player2]}")

        if self.score[self.player1] >= 3:
            self.announce_winner(self.player1)
        elif self.score[self.player2] >= 3:
            self.announce_winner(self.player2)

class Battleship1D(Game):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.ship_positions = {
            player1: random.randint(0, 9),
            player2: random.randint(0, 9)
        }

    def play_round(self):
        guess1 = int(input(f"{self.player1}, enter your guess (0-9): "))
        if guess1 == self.ship_positions[self.player2]:
            self.announce_winner(self.player1)
            return

        guess2 = int(input(f"{self.player2}, enter your guess (0-9): "))
        if guess2 == self.ship_positions[self.player1]:
            self.announce_winner(self.player2)
            return

        print("No hits this round. Keep trying!")

print("=== Coin Toss Game ===")
coin_game = CoinToss("Alice", "Bob")
while coin_game.winner is None:
    coin_game.play_round()

print("\n=== Battleship 1D Game ===")
battleship_game = Battleship1D("Alice", "Bob")
while battleship_game.winner is None:
    battleship_game.play_round()