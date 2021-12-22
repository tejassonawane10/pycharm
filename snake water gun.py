# snake water gun while loop for 10 chances
import random
lst = ['s','w','g']
chance = 10
no_of_chance = 0
computer_point = 0
player_point = 0
print("s for snake\nw for water\ng for gun\n")
while(chance > no_of_chance):
    player = input("snake,water,gun:")
    computer = random.choice(lst)

    if player == computer:
        print("Tie both 0 point to each \n")
    elif player == "s" and computer == "g":
        computer_point = computer_point + 1
        print(f"your guess {player} and computer guess {computer} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif player == "s" and computer == "w":
        player_point = player_point + 1
        print(f"your guess {player} and computer guess {computer} \n")
        print("player wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif player == "w" and computer == "s":
        computer_point = computer_point + 1
        print(f"your guess {player} and computer guess {computer} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif player == "w" and computer == "g":
        player_point = player_point + 1
        print(f"your guess {player} and computer guess {computer} \n")
        print("player wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif player == "g" and computer == "s":
        player_point = player_point + 1
        print(f"your guess {player} and computer guess {computer} \n")
        print("player wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    elif player == "g" and computer == "w":
        computer_point = computer_point + 1
        print(f"your guess {player} and computer guess {computer} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {player_point} \n")

    else:
        print("you have wrong input\n")
    no_of_chance = no_of_chance +1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("game over")
if player_point == computer_point:
    print("Tie")
elif computer_point > player_point:
    print("computer won sorry you lose")
else:
    print("you win and computer lose")
print(f"your point is {player_point} and computer point is {computer_point}")