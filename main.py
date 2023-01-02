import random

# Define a class for a card
class Card:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f'{self.value}'

# Define a class for a deck of cards
class Deck:
  def __init__(self):
    self.cards = []
    for value in range(1, 16):
      self.cards.append(Card(value))
      self.cards.append(Card(value))

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    return self.cards.pop()

# Define a class for a player
class Player:
  def __init__(self, name):
    self.name = name
    self.hand = []
    self.deck = Deck()
    self.deck.shuffle()

  def draw(self):
    self.hand.append(self.deck.deal())

  def show_hand(self):
    print(f'{self.name} has the following cards in their hand:')
    for card in self.hand:
      print(card)

  def has_card(self, value):
    for card in self.hand:
      if card.value == value:
        return True
    return False

# Create two players
player1 = Player('Player 1')
player2 = Player('Player 2')

# Have each player draw five cards from their deck
for i in range(5):
  player1.draw()
  player2.draw()

# Show each player's hand
player1.show_hand()
player2.show_hand()

# Check if player 1 has a card with value 10
print(player1.has_card(10))

# Check if player 2 has a card with value 10
print(player2.has_card(10))

