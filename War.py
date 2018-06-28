from random import shuffle

class Card():
    values = [None, None, "2", "3", "4" ,"5" ,"6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["spades", "hearts", "diamonds", "clubs"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    def __repr__(self):
        v = self.values[self.value]
        s = self.suits[self.suit]
        return v + " of " + s


class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(1, 4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None


class Game():
    def __init__(self):
        name1 = input("Player 1 Name: ")
        name2 = input("Player 2 Name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    def wins(self, winner):
        w = "{} Wins this Round".format(winner)
    def drew(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} and {} drew {}".format(p1n, p1c, p2n, p2c)
        print(d)
    def winner(self, p1_wins, p2_wins):
        if p1_wins > p2_wins:
            print("Player 1 wins!")
        elif p2_wins > p1_wins:
            print("Player 2 wins!")
        else:
            print("Its a draw")
    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            q = input("Press q to Quit, Press any other key to proceed")
            if q == "q":
                break
            p1n = self.p1.name
            p1c = self.deck.rm_card()
            p2n = self.p2.name
            p2c = self.deck.rm_card()
            self.drew(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.wins(p1n)
                self.p1.wins += 1
            else:
                self.wins(p2n)
                self.p2.wins += 1
            self.winner(self.p1.wins, self.p2.wins)

game = Game()
game.play_game()









