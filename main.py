

def add(num_One, num_Two):
    return num_One + num_Two

def subtract(num_One, num_Two):
    return num_One - num_Two

def multiply(num_One, num_Two):
    return num_One * num_Two

def divide(dividend, divisor):
    return dividend / divisor

def sum(nums: list):
    total = 0
    for number in nums:
        total += number
    return total

def main():
    value_one = 121
    value_two = 11

    print("The sum of", value_one, "and", value_two, "is:", add(value_one, value_two))
    print("The subtraction of", value_one, "by", value_two, "is:", subtract(value_one, value_two))
    print("The multiplication of", value_one, "and", value_two, "is:", multiply(value_one, value_two))
    print("The division of", value_one, "by", value_two, "is:", divide(value_one, value_two))

if __name__ == '__main__':
    main()
