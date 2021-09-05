"""
This program...
"""
# Installs:
# Imports:
from itertools import combinations

# Constants:


def main():
    # Create sample space:
    urn = [1, 2, 3, 4, 5, 6]
    sample_space = list(combinations(urn, 3))
    # Convert list_of_combinations_object into list_of_lists:
    sample_space = [list(i) for i in sample_space]
    print("The sample space is: ", sample_space,)
    print("The number of outcomes is: ", len(sample_space))

    # Checks if the second smaller number from each sample outcome is a 3:
    event = []
    # If the second number in a list is a 3, then appends that list to event:
    for i in sample_space:
        # Sorts each list from lower to higher so in each list the second number is the second smaller:
        i.sort
        # If the second element of the list is a three, append it to event:
        if i[1] == 3:
            event.append(i)
    print("The sample space in event A is: ", event)
    print("The number of outcomes in event A is: ", len(event))


if __name__ == "__main__":
    main()
