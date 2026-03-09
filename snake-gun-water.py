import random as r 

def result(player_choice , sys_choice):
    if player_choice == sys_choice:
        return "DRAW"
    elif player_choice == "WATER":
        if sys_choice == "GUN":
            return "WIN" 
        else:
            return "LOSE"
    elif player_choice == "GUN":
        if sys_choice == "SNAKE":
            return "WIN" 
        else:
            return "LOSE"
    else:
        if sys_choice == "WATER":
            return "WIN" 
        else:
            return "LOSE"
 

def score(point,outcome):
    if outcome == "WIN":
        return (point + 10)
    elif outcome == "LOSE":
        return (point - 5)
    else:
        return point


lst = ["GUN" , "WATER" , "SNAKE"]
point = 0
round = 1
while True:
    print("1 - GUN")
    print("2 - WATER")
    print("3 - SNAKE")
    select = int(input("Enter ur choice : "))
    if select < 1 or select > 3:
        print("Invalid choice!!")
        continue
    player_choice = lst[select-1]
    sys_choice = r.choice(lst)
    outcome = result(player_choice, sys_choice)
    point = score(point , outcome)
    print("Player:", player_choice)
    print("Computer:", sys_choice)
    print("Result:", outcome)
    print("Total point : ",point)
    play = input("Do u want to play again?(Y/N) : ").lower()
    print("Total rounds played : ",round)
    round += 1
    if play != "y":
        print("Thanks for playing!!")
        break
    print("-"*30)