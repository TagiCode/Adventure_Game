"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, opponent_move):
        self.my_move = my_move
        self.opponent_move = opponent_move


class RandomPlayer(Player):  # 2.Subclass that plays randomly
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):  # 3.Subclass for a human player
    def move(self):
        pick = input(f"What's your pick? (Rock, Paper, Scissor): ")
        pick = pick.lower()
        while pick not in moves:  # 6.Validate user input
            pick = input("Pick a valid move!")
        return pick


class ReflectPlayer(Player):  # 5. Reflect_Player
    def __init__(self):
        Player.__init__(self)
        self.opponent_move = None

    def move(self):
        if self.opponent_move is None:
            return random.choice(moves)
        else:
            return self.opponent_move


class CyclePlayer(Player):  # 5. CyclePlayerz
    def __init__(self):
        Player.__init__(self)
        self.my_move = random.choice(moves)

    def move(self):
        if self.my_move == "Rock":
            return "Paper"
        elif self.my_move == "Paper":
            return "Scissors"
        else:
            return "Rock"


def beats(one, two):
    return (
        (one == "rock" and two == "scissors") or
        (one == "scissors" and two == "paper") or
        (one == "paper" and two == "rock")
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Your move: {move1} Copmuter's move: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.score1 += 1  # Keep score
            print("*** You Win ***")
        elif beats(move2, move1):
            self.score2 += 1
            print("*** You Lose ***")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        rounds = input("How many rounds do you want to play?  ")
        for round in range(int(rounds)):
            print(f"Round {round +1}:")
            self.play_round()
            print(f"Your Score: {self.score1}\n"
                  f"Computer's Score: {self.score2}")
        if self.score1 > self.score2:  # Winner announcment
            print("***Congratts, You are the Champion!***")
        elif self.score1 < self.score2:
            print("***Sorry, Computer is the Champion!***")
        else:
            print("***No winners at this time!***")
        print("Game over!")


if __name__ == '__main__':
    strategies = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer(),
    }

user_input = input(
    "Select the player strategy (Pick a Number))\n"
    "you want to play against\n"
    "Rock Player (1)\n"
    "Random Player (2)\n"
    "Cycle Player (3)\n"
    "Reflect Player (4)\n"
)

game = Game(HumanPlayer(), strategies[user_input])
game.play_game()
