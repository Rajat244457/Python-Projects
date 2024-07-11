import random
game=["snake","water","gun"]
a=random.choice(game)
n=0
computer_point=0
your_point=0
while n<10:
    n=n+1
    b=input("snake,water,gun:")
    if a==b:
        print("Tie both 0 point to each")
    elif a=="water" and  b=="snake":
        your_point=your_point+1
        print(f" computer guess is {a} and your guess is {b}\n")
        print("you won 1 point\n")
        print(f"computer point is {computer_point} and your point is {your_point}\n")
    elif a=="gun" and b=="water":
        your_point=your_point+1
        print(f" computer guess is {a} and your guess is {b}\n")
        print("you won 1 point\n")
        print(f"computer point is {computer_point} and your point is {your_point}\n")
    elif a=="snake" and b=="gun":
        your_point=your_point+1
        print(f" computer guess is {a} and your guess is {b}\n")
        print("you won 1 point\n")
        print(f"computer point is {computer_point} and your point is {your_point}\n")
    elif a=="snake"and b=="water":
        computer_point=computer_point+1
        print(f" computer guess is {a}and your guess is {b}\n")
        print("computer won 1 point\n")
        print(f"computer point is {computer_point} and your point is {your_point}\n")
    elif a=="gun"and b=="snake":
        computer_point = computer_point + 1
        print(f" computer guess is {a} and your guess is {b}\n")
        print("computer won 1 point\n")
        print(f"computer point is {computer_point} and your point is {your_point}\n")
    elif a=="water"and b=="gun":
        computer_point = computer_point + 1
        print(f" computer guess is {a} and your guess is {b}\n")
        print("computer won 1 point\n")
        print(f"computer point is {computer_point} and your point is {your_point}\n")
    else:
        print("plss enter correct input")
    print(f"{10-n} is left out of {n}\n")
print("GAME OVER")
if computer_point==your_point:
    print("TIE")
elif computer_point>your_point:
    print("COMPUTER WIN AND YOU LOOSE")
else:
    print("YOU WIN AND COMPUTER LOOSE")
print(f"your point is {your_point} and computer point is {computer_point}")



