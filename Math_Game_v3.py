import random

class Game:

    # defining class variables for later use by methods
    mode = 0
    level = 0
    max_num = 0
    score = 0
    counter = 1

    # Method calls to initalize the difficulty level and sets the max_num variable
    def set_level(self):

        # used like a do-while loop to make sure user input is valid
        while True:

            print("Please select a level 1 - 4: ")
            user_choice = input(" > ")

            # logic to determine if user_choice was valid
            try: 
                level = int(user_choice)
                # checks if the user_choice is able to be converted to an int (aka it's not text of some sort) 
                # also checks if the value is in the correct range and sets the max_num based on that
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
            # catches specific error and then re-starts the while loop
            except ValueError:
                print("\nEntry must be a number. No letters")
                continue

    # this takes the max_num variable from the set_level() method and assigns two random numbers
    # that are within the range 1 - max_num, then saves a list of those two varaibles for later access
    def set_nums(self, max_num):
        
        g.nums = []
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        g.nums.extend((num1, num2))
        print(g.nums)
        return g.nums

    # Method calls sets the mode based on ther user input using the same logic from set_level() method
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

    # Method sets the variables each method call, allowing for different options on following calls
    def play_game(self):
        self.level = g.set_level()
        self.mode = g.set_mode()

        # checks how many problems have been asked and runs the loop until it reaches the limit
        while g.counter <= 10:
            
            # sets the two random numbers each iteration to give different values each time through the loop
            self.nums = g.set_nums(self.level)

            # utilizes the earlier defined mode to ask user for the answer and saves said answer
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

            # logic to check user_answer vs the correct answer (float used due to rounding errors with division)
            if float(user_answer) == float(self.answer):
                print("Correct!\n")
                g.score += 1
                print("Current Score: " + str(g.score) + "/" + str(g.counter))
            else:
                print("Incorrect, you were " + str(round(abs(self.answer - float(user_answer)),5)) + " away from the right answer " + str(round(self.answer, 5)))
                print("Current Score: " + str(g.score) + "/" + str(g.counter))

            g.counter +=1

        # when the loop exits, it shows the total score for the round
        print("*** You got " + str(g.score) + "/" + str(g.counter) + " correct! ***")

        # resets variables to default values and executes the keep_playing() method to re-start or end the program based on the users input
        g.counter = 1
        g.score = 0
        g.keep_playing()
            
    # method holding the logic to restart or end the program based on the user input
    def keep_playing(self):

        while True:
            
            # sets the user response to the question
            go_again = input("\nPlay again? (y/n): ")

            # logic used to restart or end the program
            if go_again.lower() == "y":
                print("\n")
                g.play_game()
            else:
                if go_again.lower() == "n":
                    quit()
                else:
                    print("Invalid response!")
                    g.keep_playing()

    # simple methods holding the answer for each given game mode           
    def add(self, nums):
        self.answer = nums[0] + nums[1]
        return self.answer
    # simple methods holding the answer for each given game mode  
    def sub(self, nums):
        self.answer = nums[0] - nums[1]
        return self.answer
    # simple methods holding the answer for each given game mode  
    def mult(self, nums):
        self.answer = nums[0] * nums[1]
        return self.answer
    # simple methods holding the answer for each given game mode  
    def div(self, nums):
        self.answer = nums[0] / nums[1]
        return self.answer

# creates the g object of type Game
g = Game()

# starts the game the first time
g.play_game()