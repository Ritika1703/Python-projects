import random
item_list=["Rock","Paper","Scissors"]
user_choice=input("Enter your move from Rock,paper,scissor =")
comp_choice=random.choice(item_list)

print(f"User-choice= {user_choice}, Computer choice= {comp_choice}")

if user_choice==comp_choice:
    print("Both chose same, Match tie!")

elif user_choice=="Rock":
    if comp_choice=="Scissor":
        print("Rock hits Scissor ,You win")
    else: 
        print("Paper cover Rock ,Computer win")

elif user_choice=="Paper":
    if comp_choice=="Rock":
        print("Paper cover Rock ,You win")
    else:
        print("Scissor cut Paper ,Computer win")

elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor cut Paper ,You win")
    else:
        print("Paper cover Rock ,Computer win")

