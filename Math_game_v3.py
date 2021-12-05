import random

play_game = input("Would you like to play the math game? Y/N ")
choose_level = input("What difficulty level? 1 - 4: ")
mode = input("Choose mode: ")

def choose_numbers(difficulty_level):
    # Level 1: up to 10
    if difficulty_level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    # Level 2: up to 20
    elif difficulty_level == 2:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
    # Level 3: up to 50
    elif difficulty_level == 3:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    # Level 4: up to 100
    elif difficulty_level == 4:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    else:
        choose_numbers(int(choose_level))
    return num1, num2


nums = choose_numbers(int(choose_level))

    
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



def choose_mode(mode):
    if mode == int(1):
        math_add(nums)
    elif mode == int(2):
        math_sub(nums)
    elif mode == int(3):
        math_mult(nums)
    elif mode == int(4):
        math_div(nums)
    else:
        print("Sorry that didn't work... Exiting program...")

choose_mode(int(mode))