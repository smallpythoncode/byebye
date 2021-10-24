from random import randint


def roll_d20():
    """Simulates a 20-sided die roll.

    :return: An integer between 1 and 20 (inclusive)
    :rtype: int
    """
    return randint(1, 20)


if __name__ == '__main__':
    print(roll_d20())
