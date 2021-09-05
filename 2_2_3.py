"""
This program...
"""
# Installs:
# Imports:
from itertools import combinations

# Constants:

def main():
    # Create sample space:
    urn = [1, 2, 3 ,4 ,5, 6]
    sample_space = list(combinations(urn, 3))
    print(sample_space)
    print(len(sample_space))
    sample_space = [list(i) for i in sample_space]
    print(sample_space)
    print(len(sample_space))

    # Checks if the second smaller number from each sample outcome is a 3.
    count = 0
    event = []
    for i in sample_space:
        if find_second_smaller(i) == 3:
            event.append(i)
    print(event)


def find_second_smaller(list):
    """
    :param list: takes every possible sample outcome from the sample space.
    :return: the second smaller number.
    """
    list.sort
    # print(list[1])
    return list[1]


if __name__ == "__main__":
    main()