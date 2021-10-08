def add(num_One, num_Two):

    #TODO: Write a function to add two numbers together and return the value
    return num_One + num_Two
    pass


def subtract(num_One, num_Two):
    # TODO: Write a function to subtract num_Two from num_One
    pass


def multiply(num_One, num_Two):
    # TODO: Write a function to multiply two numbers together and return the value
    return num_One * num_Two



def divide(dividend, divisor):
    return dividend // divisor
    pass


def sum(nums: list):
    # TODO: Write a function that sums up the values in a list and return the resulting value
    pass

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
