# Rock Paper Scissors

import random as r


rps = ["rock", "paper", "scissors"]

print("type 0 for rock")
print("type 1 for paper")
print("type 2 for scissors")

human = int(input("type a choice: "))
computer = round(r.random()*2)

print(f"{rps[human]}<--->{rps[computer]}")

if rps[human] == rps[computer]:
    print("Draw")
elif rps[human] == "rock" and rps[computer] == "scissors":
    print("you win")
elif rps[human] == "scissors" and rps[computer] == "paper":
    print("you win")
elif rps[human] == "paper" and rps[computer] == "rock":
    print("you win")
else:
    print("computer won")
