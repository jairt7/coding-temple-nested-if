# 1. Nested Decisions: The Adventure Game
'''
Original code:

place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")

'''
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You don't have a match!")
    elif action == "proceed in the dark":
        print("Oh, you think the darkness is your ally, but you merely adopted the dark. \
I was born in it, molded by it. I didn't see the light until I was already a man; by then, \
it was nothing to me but blinding! The shadows betray you, because they belong to me.")
    else:
        pass
else:
    pass