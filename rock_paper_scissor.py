import random

# Rock paper scissor game

choose = ["rock", "paper", "scissor"]
user_choice = input("Choose anyone(rock,paper or scissor)\n")
comp_choice = random.choice(choose)

if user_choice == comp_choice:
    print(f"Both of you chose {user_choice}. Its a tie")
elif user_choice == "rock":
    if comp_choice == "scissor":
        print(f"The computer chose {comp_choice}, Rock smashes Scissor. You win")
    else:
        print(f"The computer chose {comp_choice}, Paper covers rock. You lose")
elif user_choice == "paper":
    if comp_choice == "scissor":
        print(f"The computer chose{comp_choice}. Scissor cuts paper. You lose")
    else:
        print(f"The computer chose {comp_choice}, Paper covers rock. You win")
elif user_choice == "scissor":
    if comp_choice == "paper":
        print(f"The computer chose {comp_choice}, Scissor cuts paper. You win")
    else:
        print(f"The computer chose {comp_choice}, Rock smashes scissor. You lose")
