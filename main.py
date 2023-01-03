import random

# Define a class for a card
class Card:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f'{self.value}'

# Define a class for a deck of cards with 2x copies of each card
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

  def has_cards(self, value1, value2):
    count = 0
    for card in self.hand:
      if card.value == value1 or card.value == value2:
        count += 1
    return count == 2



# simulates a certain number of different hands and show chance that one card is drawn
def simulate_hands_single(num_hands, draws):
  count = 0
  for i in range(num_hands):
    # Create two players
    player1 = Player('Player 1')
    player2 = Player('Player 2')

    # Shuffle the decks and deal 3 cards to each player
    player1.deck.shuffle()
    player2.deck.shuffle()
    for i in range(draws):
      player1.draw()
      player2.draw()

    # Check if player 1 has a card with value 1
    if player1.has_card(1):
      count += 1

  # Calculate and print the percentage chance of having a card with value 1 in your hand
  percentage = count / num_hands * 100
  print(f'The percentage chance of having a card with value 1 in your hand is {percentage:.2f}%')

# Define a function that simulates a certain number of different starting hands and show chance of two cards are drawn
def simulate_hands_double(num_hands, value1, value2, draws):
  count = 0
  for i in range(num_hands):
    # Create two players
    player1 = Player('Player 1')
    player2 = Player('Player 2')

    # Shuffle the decks and deal 3 cards to each player
    player1.deck.shuffle()
    player2.deck.shuffle()
    for i in range(draws):
      player1.draw()
      player2.draw()

    # Check if player 1 has two specific cards
    if player1.has_cards(value1, value2):
      count += 1

  # Calculate and print the percentage chance of having two specific cards in your hand
  percentage = count / num_hands * 100
  print(f'The percentage chance of having cards with values {value1} and {value2} in your hand is {percentage:.2f}%')

# Simulate x different hands and track the percentage chance of having two specific cards by draw y
simulate_hands_double(10000, 1, 1, 25)

# Simulate x different  hands
# simulate_hands_single(10000, 9)

# # Create two players
# player1 = Player('Player 1')
# player2 = Player('Player 2')
#
# # Have each player draw five cards from their deck
# for i in range(3):
#   player1.draw()
#   player2.draw()
# # Show each player's hand
# player1.show_hand()
# player2.show_hand()
#
# # Check if player 1 has a card with value 10
# print(player1.has_card(10))
#
# # Check if player 2 has a card with value 10
# print(player2.has_card(10))

