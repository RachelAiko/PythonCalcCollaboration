import math
import random


def add(num_One, num_Two):
    # TODO: Write a function to add two numbers together and return the value
    return num_One + num_Two


def subtract(num_One, num_Two):
    return num_One - num_Two


def multiply(num_One, num_Two):
    # TODO: Write a function to multiply two numbers together and return the value
    return num_One * num_Two


def divide(dividend, divisor):
    return dividend // divisor


def average(nums: list):
    total = sum(nums)
    return total / len(nums)


def median(nums: list):
    # TODO: Median is not being sorted first
    if len(nums) % 2 == 1:
        return nums[(len(nums) - 1) // 2]
    else:
        return ((nums[len(nums) // 2]) + (nums[len(nums) // 2 - 1])) / 2

def sec_Sort(nums: list):
    # TODO: write a sorting algorithm to sort through a list
    pass


if __name__ == '__main__':
    value_one = 121
    value_two = 11
    values = [random.randint(0, 10) for x in range(0, random.randint(2, 20))]

    print("The sum of", value_one, "and", value_two, "is:", add(value_one, value_two))
    print("The subtraction of", value_one, "by", value_two, "is:", subtract(value_one, value_two))
    print("The multiplication of", value_one, "and", value_two, "is:", multiply(value_one, value_two))
    print("The division of", value_one, "by", value_two, "is:", divide(value_one, value_two))
    print("The sum of the list", values, "is:", sum(values))
    print("The average of the list", values, "is:", average(values))
    print("The median of the list", values, "is:", median(values)) # This is not done right, median needs to be sorted!
