#main game file

from characters.player import *

player = Player("default",100)
#player = Character("defult",1)

def main():
    #name = str(input("please enter your name: "))
    newname = input("please enter you name: ")
    player.name = newname
    print (player.weapon)

if __name__ == "__main__":
    main()

