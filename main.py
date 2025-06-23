def Welcome():
    print('Welcome trusted servant of the state!\nMy Name is Gerald and I have asked you here to provide us with your wisdom.\nThe People of Barrowlandia are revolting against us in the government.\nWe need you to calm the people, maintain our power, create rest in our kingdom.\nWe are relying on YOU!')
    try:
        choice1 = int(input('Choose your title:\n1) Lord Garry\n2) Lady Janet\n3) Sir Derek IV\n'))
    except ValueError:
        print("Please enter a number.")
        return Welcome()

    match choice1:
        case 1:
            title = "Lord Garry"
        case 2:
            title = "Lady Janet"
        case 3:
            title = "Sir Derek IV"
        case _:
            print("Invalid choice you gremlin. Try again")
            return Welcome()

    print(f"Greetings {title}! I look forward to serving with you.")
    Challenge1(title)  # Pass the title to the next function


def Challenge1(title):
    print(f'\nIt is time for your first challenge, {title}!')
    print('The people of Barrowlandia are facing an economic depression.')
    print('The people are hopeless and depressed!')
    print('We have 3 choices, choose wisely as the people are relying on you.')

    try:
        choice2 = int(input('Choose your strategy:\n1) Place funding into industry to support jobs\n2) Provide cheap beer to raise spirits\n3) Increase state benefits and universal credit to improve the standard of living\n'))
    except ValueError:
        print("Please enter a number.")
        return Challenge1(title)

    match choice2:
        case 1:
            print("Fantastic choice. The people are starting to realise that there are opportunities out there.\nAlthough there is still work to do, spirits are still low.")
        case 2:
            print("Well what a nice idea!!\nUnfortunately, the cheap booze caused a riot at the rugby.\n150 people died\nBUT spirits are still high! (Pun Intended)")
        case 3:
            print("Whatever are we paying you for?\nThe people have given up any kind of employment and are becoming couch potatoes.")
        case _:
            print("Invalid choice you gremlin. Try again")
            return Challenge1(title)

Welcome()



