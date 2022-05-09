import random

# Start of Version 1

""" 
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
 """

# Start of Version 2
""" class Level:
    def __init__(self, dif_level=1):
        self.dif_level = dif_level
    def set_level(self, dif_level):
        self.dif_level = dif_level
    def get_level(self):
        return print(self.dif_level)
    def choose_numbers(self, x):
        # Level 1: up to 10
        if x == 1:
            max_num = 10
        # Level 2: up to 20
        elif x == 2:
            max_num = 20
        # Level 3: up to 50
        elif x == 3:
            max_num = 50
        # Level 4: up to 100
        elif x == 4:
            max_num = 100
        self.num1 = random.randint(1, max_num)
        self.num2 = random.randint(1, max_num)
    def get_nums(self, x):
        self.num1 = self.choose_numbers(x)
        self.num2 = self.choose_numbers(x)
        return self.num1, self.num2
class Mode():
    def set_mode(self):
        print("Select game mode: \n 1. Addition \n2. Subtraction\n 3. Multiplication\n 4. Division")
        self.mode = input("> ")
    
    # Add
    def add(self, nums):
        answer = nums[0] + nums[1]
        print(str(nums[0]) + " + " + str(nums[1]) + "?")
        return answer
    # Sub
    def subtract(nums):
        answer = nums[0] - nums[1]
        print(answer)
    # Mult
    def multiply(nums):
        answer = nums[0] * nums[1]
        print(answer)
    # Div
    def divide(nums):
        answer = nums[0] / nums[1]
        print(answer)
# this is the start of the do-while loop for the entire program
while True:
    level = Level()
    mode = Mode()
    counter = 0
    score = 0
    # small loop to make sure input is within range
    while True:
        choose_level = int(input("What difficulty level? 1 - 4: "))
        if choose_level >= 1 and choose_level <= 4:
            break
        else:
            print("\nSelected number is outside of the available range")
    while True:
        numbers = level.get_nums(choose_level)
        
        choose_mode = int(input("Select a mode: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division"))
        if choose_mode >= 1 and choose_mode <= 4:
            if choose_mode == 1:
                pass
            
        correct_answer = mode.add(numbers)
        user_answer = int(input(">  "))
        if user_answer == correct_answer:
            score += 1
            print("You got it!\n")
        else:
            print("That was incorrect, the correct answer was " + str(correct_answer) + "\n")
        
        counter += 1
        if counter == 5:
            break
    print("Your score: " + str(score) + " out of 5")
    go_again = input("Play again? (y/n): ")
    if go_again.lower() == "y":
        print("\n")
        continue
    else:
        break """

# Start of Version 3
class Game:

    mode = 0
    level = 0
    max_num = 0
    score = 0
    counter = 1

    def set_level(self):
        
        while True:

            print("Please select a level 1 - 4: ")

            user_choice = input(" > ")

            try: 
                level = int(user_choice)
                if level >= 1 and level <= 4:
                    if level == 1:
                        max_num = 10
                        return max_num
                    elif level == 2:
                        max_num = 20
                        return max_num
                    elif level == 3:
                        max_num = 50
                        return max_num
                    else:
                        max_num = 100
                        return max_num
                else:
                    print("Invalid input - outside of selection range. Try again.")
                    continue

            except ValueError:
                print("\nEntry must be a number. No letters")
                continue

    def set_nums(self, max_num):
        
        nums = []
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        nums.extend((num1, num2))
        print(nums)
        return nums

    def set_mode(self):

        while True:

            print("\nPlease select a game mode: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

            user_choice = input(" > ")

            try: 
                mode = int(user_choice)
                if mode >= 1 and mode <= 4:
                    if mode == 1:
                        self.mode = 1
                        return self.mode
                    elif mode == 2:
                        self.mode = 2
                        return self.mode
                    elif mode == 3:
                        self.mode = 3
                        return self.mode
                    else:
                        self.mode = 4
                        return self.mode
                else:
                    print("\nInvalid input - outside of selection range. Try again.")
                    continue

            except ValueError:
                print("\nEntry must be a number. No letters")
                continue

    def play_game(self):
        self.level = g.set_level()
        self.mode = g.set_mode()

        while g.counter <= 10:

            self.nums = g.set_nums(self.level)

            if self.mode == 1:
                g.add(self.nums)
                user_answer = input(str(self.nums[0]) + " + " + str(self.nums[1]) + " = ")
            elif self.mode == 2:
                g.sub(self.nums)
                user_answer = input(str(self.nums[0]) + " - " + str(self.nums[1]) + " = ")
            elif self.mode == 3:
                g.mult(self.nums)
                user_answer = input(str(self.nums[0]) + " * " + str(self.nums[1]) + " = ")
            else:
                g.div(self.nums)
                user_answer = input(str(self.nums[0]) + " / " + str(self.nums[1]) + " = ")

            if float(user_answer) == float(self.answer):
                print("Correct!\n")
                g.score += 1
                print("Current Score: " + str(g.score) + "/" + str(g.counter))
            else:
                print("Incorrect, you were " + str(round(abs(self.answer - float(user_answer)),5)) + " away from the right answer " + str(round(self.answer, 5)))

            g.counter +=1

        print("*** You got " + str(g.score) + "/" + str(g.counter) + " correct! ***")

        g.counter = 1
        g.score = 0
        g.keep_playing()
            
    
    def keep_playing(self):
        while True:

            go_again = input("\nPlay again? (y/n): ")

            if go_again.lower() == "y":
                print("\n")
                g.play_game()
            else:
                if go_again.lower() == "n":
                    quit()

                else:
                    print("Invalid response!")
                    g.keep_playing()
                    
    def add(self, nums):
        self.answer = nums[0] + nums[1]
        return self.answer

    def sub(self, nums):
        self.answer = nums[0] - nums[1]
        return self.answer

    def mult(self, nums):
        self.answer = nums[0] * nums[1]
        return self.answer

    def div(self, nums):
        self.answer = nums[0] / nums[1]
        return self.answer

g = Game()

g.play_game()