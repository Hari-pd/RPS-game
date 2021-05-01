from random import randint

#list of game options
l = ["r", "p", "s"] # r= Rock, p= Paper, s= Scissor

player = input("The options are -->\n Rock --> r\n Paper --> p and \n Scissor --> s\nGive your choice: ")

if player in l:
    comp = l[randint(0,2)]

    if player == comp:
        print("It's a Tie!")
    elif player == "r":
        if comp =="p":
            print("You Loose!")
        else:
            print("You Win!")
    elif player == "p":
        if comp == "s":
            print("You Loose!")
        else:
            print("You Win!")
    elif player == "s":
        if comp == "p":
            print("You Win!")
        else:
            print("You Loose!")
    print("Because Computer chooses "+ comp)
else:
    print("Your choice is not from the options.")