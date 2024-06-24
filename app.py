import random


run = True
user_score = 0
pc_score = 0
options = ["s" , "k" , "q"]


def game():
    global pc_score, user_score , options


    pc_choice = random.choice(options)
    print("s => sang , k => kaqaz , q => qeychi")
    user_choice = input("Choose one of the above options\n")

    if user_choice in options:
        print(f"pc choice => {pc_choice} , your choice => {user_choice}")

        if user_choice == pc_choice :
            print("It's a tie, try again.")        

        else:

            if user_choice == "s" and pc_choice == "k":
                pc_score += 1
                print("PC wins this round.")

            elif user_choice == "s" and pc_choice == "q":
                user_score += 1
                print("You win this round.")
            elif user_choice == "k" and pc_choice == "s":
                user_score += 1
                print("You win this round.")
            elif user_choice == "k" and pc_choice == "q" :
                pc_score += 1
                print("PC wins this round.")

            elif user_choice == "q" and pc_choice == "s":
                pc_score += 1
                print("PC wins this round.")

            elif user_choice == "q" and pc_choice == "k":
                user_score += 1
                print("You win this round.")


        print(f"pc score : {pc_score} , user score : {user_score}")


    else:
        print("Invalid input, try again.")


while run:
    game()
    if user_score == 3 or pc_score == 3 :
        if user_score == 3 :
            print("You won!")
        else:
            print("PC won!")
        run = False