Y = ["Yes","yes","Y","y"]
N = ["No","no","N","n"]
def find_the_kitty():
    print("You find a sweet little kitten sitting next to an empty bowl.It looks up at you imploringly. \"Meow?\"")
    ftk_choice = input("Will you feed the kitty?")
    if ftk_choice in Y:
        print("You begin searching the kitchen for anything that resembles cat food.")
        #feed_the_kitty()
    elif ftk_choice in N:
        print("You heartless scoundrel. You bothered to find out what was meowing and you'd just leave a sweet, precious, little kitty to die of starvation?!")
        end_game()
    else:
        print("What are you doing? That's not acceptible!")
        end_game()
        
def end_game():
    print ("Your choices have resulted in the demise of all. You lose. Kaboom. Universe gone.")


def start_game():
    print("You've fallen into the game and find yourself standing in a kitchen. You hear a meow.")
        
    choice = input("Will you find the source of the meow?(Yes or No)")
    
    if choice in Y:
        print("\"Yes! Here, kitty, kitty, kitty!\"")
        find_the_kitty()
    elif choice in N:
        print("\"Meow? No thanks. I'm out of here.\"")
        end_game()
    else:
        print("What are you doing? That's not acceptible!")
        start_game()
    

start_game()


