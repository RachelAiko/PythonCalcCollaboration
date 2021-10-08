"""
Colabrative Calculator made by FGCU's Software Engineering Club to demo collaboration using Github
"""


def add(num_One, num_Two):
    return num_One + num_Two


def subtract(num_One, num_Two):
    return num_One - num_Two


def multiply(num_One, num_Two):
    return num_One * num_Two


def divide(dividend, divisor):
    return dividend // divisor


def sum(nums: list):
    total = 0
    for number in nums:
        total += number
    return total


if __name__ == '__main__':
    value_one = 121
    value_two = 11
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print("The sum of", value_one, "and", value_two, "is:", add(value_one, value_two))
    print("The subtraction of", value_one, "by", value_two, "is:", subtract(value_one, value_two))
    print("The multiplication of", value_one, "and", value_two, "is:", multiply(value_one, value_two))
    print("The division of", value_one, "by", value_two, "is:", divide(value_one, value_two))
    print("The division of the list", values, "is:", sum(values))
