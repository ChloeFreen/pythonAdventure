import time
import random

items = []


def pause_time(message):
    print(message)
    time.sleep(2)


def villian_picker():
    global villian
    villian = random.choice(["Beast", "Monster", "Witch", "Murderer"])


def introduction():

    pause_time("Time to start your adventure")
    pause_time(". . . .")
    pause_time("A " + villian + " has kidnapped "
               "the beloved princess of this land. ")
    pause_time("Many men have tried and failed to rescue her and now "
               "there is no one left to help ")
    pause_time("It's now up to you")


def forest():
    pause_time("You head left into the dark forest.")
    pause_time("After a few moments, you are "
               "greeted by a talking Donkey")
    if "Key" in items:
        pause_time("The Donkey greets you, but it has already "
                   "given you the Golden Key, so there is nothing "
                   "more to do here now.")
    else:
        pause_time("The Donkey greets you and gives you a Gold Key. "
                   "He says it will be needed to slay the beast")
        items.append("Key")
    pause_time("You head back to the path.")
    returnToPath()


def cave():
    pause_time("You head right into the glowing cave")
    pause_time("The glowing gets brighter until"
               " you find yourself in front of a chest "
               "and there is a large lock on the lid.")
    if "Key" in items:
        pause_time("You insert the Golden Key into the lock and twist")
        pause_time("The chest unlocks and you open the lid")
        pause_time("Inside there is a golden sword, "
                   "shining brighter than anything you've ever seen")
        items.append("Sword")
    else:
        pause_time("You try to open the chest")
        pause_time("But no matter how much you pull and struggle"
                   "you do not have a key "
                   "and you can not open the chest")

    pause_time("You head back to the path.")
    returnToPath()


def beast_layer():
    pause_time("You head towards the " + villian + " layer")
    pause_time("Soon you find yourself face to face with the " + villian +
               "and he does not look happy")
    pause_time("Behind him you see the princess")

    if "Sword" in items:
        pause_time("You charge at the " + villian +
                   " swinging your mighty sword")
        pause_time("The " + villian + " is no match for your power "
                   "and you have defeated him! ")
        win()
    else:
        pause_time("You charge at the " + villian + " trying to fight "
                   "even though you are empty handed")
        pause_time("The " + villian + " laughs as"
                   " you are no match for his power "
                   "and with one swift movement of his arm"
                   " you are sent back the way you came")
        pause_time("You find yourself back at the beginning path")
        returnToPath()


def retry():

    pause_time("")
    response = valid_input("Would you like to try again to save her? \n",
                           "yes",
                           "no")
    if 'yes' in response:
        play_game()
    elif "no" in response:
        return


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("Sorry, I don't understand.")
    return response


def valid_direction(prompt, o1, o2, o3, o4):
    while True:
        path = input(prompt).lower()
        if o1 in path:
            break
        elif o2 in path:
            break
        elif o3 in path:
            break
        elif o4 in path:
            break
        else:
            print("Sorry, I don't understand.")
    return path


def returnToPath():
    pause_time(". . . .")
    pause_time("Which direction shall you take?")
    print("Left to the Murky Forest\n"
          "Forward to the " + villian + " Layer\n"
          "Right to the Glowing Cave\n"
          "Retreat back\n")

    path = valid_direction("Choose a direction\n",
                           "left", "forward", "right", "back")

    if 'left' in path:
        print("You duck into the trees")
        forest()
    if 'forward' in path:
        print("You look up and the castle and take a step forward ")
        beast_layer()
    if 'right' in path:
        print("You look towards the glowing cave")
        cave()
    if 'retreat' in path:
        print("You turn around and run")
        pause_time("Coward, you abandoned the princess")
        retry()


def win():
    pause_time("You won the heart of princess!")
    pause_time("Wanna see if you can do it again?")
    retry()


def play_game():
    villian_picker()
    introduction()
    returnToPath()


play_game()
