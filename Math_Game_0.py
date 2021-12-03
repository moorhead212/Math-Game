import random


# Choose Difficulty Levels
class Level:

    def __init__(self, dif_level=1):
        self.dif_level = dif_level

    def set_level(self, dif_level):
        self.dif_level = dif_level

    def get_level(self):
        return self.dif_level


def choose_numbers(x):
    # Level 1: up to 10
    if x == 1:
        a = 1
        b = 10
        num1 = random.randint(a, b)
        num2 = random.randint(a, b)
    # Level 2: up to 20
    elif x == 2:
        a = 1
        b = 20
        num1 = random.randint(a, b)
        num2 = random.randint(a, b)
    # Level 3: up to 50
    elif x == 3:
        a = 1
        b = 50
        num1 = random.randint(a, b)
        num2 = random.randint(a, b)
    # Level 4: up to 100
    elif x == 4:
        a = 1
        b = 100
        num1 = random.randint(a, b)
        num2 = random.randint(a, b)
    else:
        choose_numbers()
    return num1, num2


choose_level = input("What difficulty level? 1 - 4: ")


# Set Correct Answers = 0


# Add
def math_add(nums):
    answer = nums[0] + nums[1]
    print(answer)

# Sub
def math_sub(nums):
    answer = nums[0] - nums[1]
    print(answer)

# Add and Sub
# def math_add_sub(nums):
 # **** Fix this spot! ****   answer = nums[0] Add or Subtract nums[1]
    # print(answer)

# Mult
def math_mult(nums):
    answer = nums[0] * nums[1]
    print(answer)

# Div
def math_div(nums):
    answer = nums[0] / nums[1]
    print(answer)

# Mult and Div
# def math_mult_div(nums):
#     answer = nums[0] Multiply or Divide  nums[1]
#     print(answer)

level = Level()

level.set_level(int(choose_level))

level_num = level.get_level()

print(choose_numbers(level_num))

math_add(choose_numbers(level_num))

math_sub(choose_numbers(level_num))

math_mult(choose_numbers(level_num))

math_div(choose_numbers(level_num))




# Generate (10) questions and answers based on choice of level and mode.
# Get true_answer

# Get the user_answer

# Check true_answer vs user_answer
# if the answer is right correct_answers += 1
# if answer is wrong, no points, show absolute distance from answer
# Correct Answers = 0 out of 10 and you were you were absolute value away from the correct answer
