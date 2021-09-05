"""
This program...
"""
# Installs:
# Imports:
# Constants:


def main():
    # Create sample space:
    dice = [1, 2, 3, 4, 5, 6]
    sample_space = []
    for i in dice:
        for j in dice:
            for k in dice:
                sample_space.append([i, j, k])
    print(sample_space)
    print(len(sample_space))
    print("===========================================================================================================")

    # Count the number of outcomes that comply with condition. Identify them:
    count = 0
    event = []
    for i in sample_space:
        if sum(i) == 5:
            count = count + 1
            event.append(i)
    print(count)
    print(event)


if __name__ == "__main__":
    main()
