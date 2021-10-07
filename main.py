

def add(num_One, num_Two):
    #TODO: Write a function to add two numbers together and return the value
    return num_One + num_Two
    pass

def subtract(num_One, num_Two):
    #TODO: Write a function to subtract num_Two from num_One
    pass

def multiply(num_One, num_Two):
    return num_One * num_Two
    pass

def divide(dividend, divisor):
    #TODO: Write a function to divides two numbers together and return the value
    pass

def sum(nums: list):
    total = 0
    for number in nums:
        total += number
    return total



if __name__ == '__main__':

    value_one = 121
    value_two = 11

    print("The sum of", value_one, "and", value_two, "is:", add(value_one, value_two))
    print("The subtraction of", value_one, "by", value_two, "is:", subtract(value_one, value_two))
    print("The multiplication of", value_one, "and", value_two, "is:", multiply(value_one, value_two))
    print("The division of", value_one, "by", value_two, "is:", divide(value_one, value_two))
