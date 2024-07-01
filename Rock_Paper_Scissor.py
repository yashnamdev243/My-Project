import random 
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("enter your move = Rock, Paper  Scissor = ")

comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice   :
    print("Both choose same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = computer win")
    else:
        print("Rock smashes Scissor = you win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, computer win")
    else:
        print("Paper covers Rock, you win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, you win")
    else:
        print("Rock smashes Scissor, computer win")