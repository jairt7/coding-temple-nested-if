# 2. Quick Decisions: The Event Planner
attendees = int(input("Enter number of attendees: "))
venue = "Recommended to use large hall, projector, and audio system" if attendees > 100 else "Recommended to use conference room, TV, and small speaker"
print(venue)
# I'm not really sure what this assignment wanted from me but I tried my best
print()
is_good_person = input("Would you like vegetarian food? y or n ")
if is_good_person == "y":
    print("I recommend Veggie Delight Caterers.")
elif is_good_person == "n":
    print("Ah, meat eaters, I see. Try Gourmet Meals Caterers.")
else:
    print("That wasn't one of the options.")
# I am joking about meat eaters being bad people. I'm a meat eater too.