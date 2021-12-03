import random


def choose_numbers(x):
    # Level 1: up to 10
    if x == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    # Level 2: up to 20
    elif x == 2:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
    # Level 3: up to 50
    elif x == 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    # Level 4: up to 100
    elif x == 4:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    else:
        pass
    return num1, num2


choose_level = input("What difficulty level? 1 - 4: ")


# Add
def math_add(nums):
    answer = nums[0] + nums[1]
    print(answer)

# Sub
def math_sub(nums):
    answer = nums[0] - nums[1]
    print(answer)

# Mult
def math_mult(nums):
    answer = nums[0] * nums[1]
    print(answer)

# Div
def math_div(nums):
    answer = nums[0] / nums[1]
    print(answer)


