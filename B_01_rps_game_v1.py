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

# Main routine goes here

# intialise game variable

mode = "regular"
rounds_played = 0

print("Rock / Paper / Scissors Game")
print()

# instructions

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if user choose infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1


