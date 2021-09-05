"""
This program...
"""
# Installs:
# Imports:
from itertools import permutations

# Constants:


def main():

    # Create standard suit:
    suit = []
    for i in range(1, 14):
        suit.append(i)
    print("A standard suit is: ", suit)
    print("The number of cards in a suit is: ", len(suit))

    # Create Standard deck:
    deck = []
    for i in range(4):
        for j in suit:
            deck.append(j)
    print("A standard deck is: ", deck)
    print("The number of cards in a deck is: ", len(deck))

    # Generate sample space:
    sample_space = permutations(deck, 2)
    sample_space = list(sample_space)
    print("The sample space is: ", sample_space)
    print("The number of outcomes in the sample space is: ", len(sample_space))

    # Generate event (the sum of two drawn cards is 8):
    event = []
    for i in sample_space:
        if sum(i) == 8:
            event.append(i)
    print("The event space is: ", event)
    print("The number of outcomes in the event space is: ", len(event))


if __name__ == "__main__":
    main()
