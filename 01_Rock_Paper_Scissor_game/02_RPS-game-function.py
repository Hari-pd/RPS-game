import random
# game function for the outcome
def game(comp,player):
    if comp == player:
        return tie
    elif player not in l:
        return invalid
    elif comp == "r":
        if player == "p":
            return Win
        else:
            return Loose
    elif comp == "p":
        if player == "s":
            return Win
        else:
            return Loose
    elif comp == "s":
        if player == "r":
            return Win
        else:
            return Loose

#list of play options
l =["r", "p", "s"]

#computer's choice
comp = l[random.randint(0,2)]

# player's choice 
player = input("The play options are;\n Rock --> r\n Paper --> p\n Scissor --> s\nEnter your choice: ")

# result prints
tie = "The game is a Tie!"
Win = "You Win!"
Loose = "You Loose!"
invalid = "You didnot choose from the play options."

# function call and assign a result
Result = game(comp,player)

# prints result with the choices
print("Computer chooses ", comp)
print(Result)
