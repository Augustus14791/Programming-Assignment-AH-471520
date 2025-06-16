def Welcome():
    print('Welcome trusted servant of the state!\nMy Name is Gerald and I have asked you here to provide us with your wisdom.\nThe People of Barrowlandia are revolting against us in the government.\nWe need you to calm the people, maintain our power, create rest in our kingdom.\n We are relying on YOU!')
    try:
        choice1 = int(input('Choose your title:\n1) Lord Garry\n2) Lady Janet\n3) Sir Derek IV\n'))
    except ValueError:
        print("Please enter a number.")
        return Welcome()

    match choice1:
        case 1:
            print("Greetings Lord Garry! I look forward to serving with you")
        case 2:
            print("Greetings Lady Janet! I look forward to serving with you")
        case 3:
            print("Greetings Sir Derek IV! I look forward to serving with you")
        case _:
            print("Invalid choice you gremlin. Try again")
            Welcome()

def Challenge1():
    print('It is time for your first challenge!\nThe people of Barrowlandia are facing an economic deppression:\nThe people are hopeless and depressed!\We have 3 choices, choose wisely as the people are relying on you')2