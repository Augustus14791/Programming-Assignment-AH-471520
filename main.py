def Welcome():
    print('Welcome trusted servant of the state!\n')
    try:
        choice1 = int(input('Choose your title:\n1) Lord Garry\n2) Lady Janet\n3) Sir Derek IV\n'))
    except ValueError:
        print("Please enter a number.")
        return Welcome()

    match choice1:
        case 1:
            print("Greetings Lord Garry!")
        case 2:
            print("Greetings Lady Janet!")
        case 3:
            print("Greetings Sir Derek IV!")
        case _:
            print("Invalid choice. Try again")
            Welcome()

Welcome()

