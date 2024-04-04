import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of item in the list
            elif user_response == item[0]:
                return item


        # print error if the user doesn't enter a vaild response
        print(error)
        print()


# display instruction
def instruction():
    print('''

*** Instructions ***

To begin, choose the number of the rounds ( or press <enter> for infinite mode.)

Then play against the computer. You need to choose R (Rock), P (Paper) or S (Scissors).

The rules are as follows:
●   Paper beats rock
●   Rock beats scissors 
●   scissors beats paper

Press <xxx> to end the game at any time.

Good Luck!
    ''')



def int_check(question):


    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# compares user / computer choice and returns
# result (win/ lose / tie)
def rps_compare(user, comp):

    # if the computer and the user chose the same it is a tie.
    if user == comp:
        result = "tie"

    # there are three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"

    # if it's not a win / tie, then it's a loss
    else:
        result = "lose"
    return result




# Main routine goes here

# initialise game variable
mode = "regular"
rounds_played = 1

rps_list = ["rock", "paper", "scissors", "xxx"]

print("### Rock / Paper / Scissors Game ###")
print()

# ask user if they want to see the instruction and display
# them if required
want_instructions = string_checker("Do you want to read instructions? ")

# checks users enter yes or no
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # round heading
    if mode == "infinite":
        rounds_heading = f"\n🙂🙂🙂 Round {rounds_played} (infinite Mode) 🙂🙂🙂"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    # randomly chose from rps list excluding exit
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    # if the user choice is exit break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if user choose infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


