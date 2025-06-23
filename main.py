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
    Challenge1(title) 


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

    Challenge2(title)


def Challenge2(title):
    print(f"\nThe time has arrived for your second opportunity to prove yourself, {title}!")

    try:
        choice = int(input(
            "The Barrowlandia public transport system is in chaos.\n"
            "Buses are late, trains are overcrowded, and one tram has mysteriously ended up in a duck pond.\n"
            "Choose your strategy:\n"
            "1) Invest in electric buses and hire more drivers\n"
            "2) Freeze fares temporarily\n"
            "3) Launch a public consultation\n"
        ))
    except ValueError:
        print("Please enter a number.")
        return Challenge2(title)

    match choice:
        case 1:
            print("The new buses are shiny, quiet, and smell faintly of pine. Commuters are cautiously optimistic, though one still insists the duck pond tram was 'a sign'.")
        case 2:
            print("The fare freeze is a hit! People are still late, but at least they’re late for free. One man now rides the bus just for the scenery.")
        case 3:
            print("The consultation was thorough. You now have 4,000 opinions, 3 conspiracy theories, and one poem about potholes. Action pending.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge2(title)

    Challenge4(title)

def Challenge4(title):
    print(f"\nAnother challenge awaits, {title}.")
    print("Youth unemployment is rising. Many are disillusioned and dangerously close to forming a ska band.")
    print("You must act before social media becomes their only career plan.")

    try:
        choice = int(input("Choose your strategy:\n1) Expand apprenticeships\n2) Fund youth entrepreneurship\n3) Launch a national volunteer service\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge4(title)

    match choice:
        case 1:
            print("Young people are gaining skills. One now calls himself 'Barrowlandia’s Premier Plumber'.")
        case 2:
            print("Startups bloom! One teen invents a plant pot that screams when thirsty. Investors are intrigued.")
        case 3:
            print("Volunteering surges! One group knits 300 scarves for local llamas. No one knows why, but spirits are high.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge4(title)

    Challenge5(title)


def Challenge5(title):
    print(f"\nA crisis at the docks, {title}!")
    print("Barrowlandia’s shipbuilding industry is facing delays and budget overruns. Workers are frustrated, and the press is circling like seagulls near chips.")

    try:
        choice = int(input("Choose your strategy:\n1) Increase funding and improve project management\n2) Launch a PR campaign highlighting the industry’s legacy\n3) Invite naval officials for a morale-boosting visit\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge5(title)

    match choice:
        case 1:
            print("The funding helps! Projects get back on track, though one vessel still mysteriously beeps to the tune of 'God Save the King'.")
        case 2:
            print("The PR campaign is slick. One ad features a ship majestically sailing past a wind farm. Locals are proud, if slightly confused.")
        case 3:
            print("The naval visit boosts morale! One officer is now dating the mayor’s cousin. Unexpected diplomacy!")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge5(title)

    Challenge6(title)


def Challenge6(title):
    print(f"\nTransport trouble, {title}!")
    print("A key bridge in Barrowlandia is undergoing repairs, causing traffic chaos. Commuters are late, cyclists are grumpy, and one person tried to cross in a kayak.")

    try:
        choice = int(input("Choose your strategy:\n1) Introduce a temporary ferry service\n2) Offer free coffee to delayed commuters\n3) Accelerate bridge repairs with night shifts\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge6(title)

    match choice:
        case 1:
            print("The ferry is a hit! One passenger insists on calling it 'The HMS Shortcut'.")
        case 2:
            print("Free coffee calms tempers. Productivity drops slightly due to caffeine-fueled storytelling.")
        case 3:
            print("Repairs speed up! The night crew includes a man who swears he once fixed Big Ben. Spirits rise.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge6(title)

    Challenge7(title)


def Challenge7(title):
    print(f"\nA cultural conundrum, {title}!")
    print("Barrowlandia’s annual summer festival is at risk of cancellation due to budget cuts and a rogue brass band that refuses to play anything but ABBA.")

    try:
        choice = int(input("Choose your strategy:\n1) Secure local sponsorships to fund the festival\n2) Rebrand it as a community picnic with music\n3) Let the brass band lead and hope for the best\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge7(title)

    match choice:
        case 1:
            print("Local businesses step up! One bakery sponsors a pie-eating contest. The festival is saved — and delicious.")
        case 2:
            print("The picnic is peaceful. The band plays ABBA. People dance. A dog wins the talent show. Success!")
        case 3:
            print("The band plays 'Dancing Queen' on loop. The crowd is confused, but oddly united. A new tradition is born.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge7(title)

    Challenge9(title)


def Challenge9(title):
    print(f"\nThe lights go out every Thursday evening, {title}.")
    print("Citizens host candlelit poetry slams, but they're starting to wonder why Thursdays are so cursed.")

    try:
        choice = int(input("Choose your strategy:\n1) Invest in renewable energy\n2) Implement traditional rolling blackouts\n3) Train squirrels to generate power\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge9(title)

    match choice:
        case 1:
            print("Solar and wind save the day! Though one windmill has become self-aware.")
        case 2:
            print("People accept the tradition. Thursday becomes 'Glowstick Yoga Night'.")
        case 3:
            print("The squirrels are enthusiastic but prone to unionizing. Mixed results.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge9(title)

    Challenge10(title)


def Challenge10(title):
    print(f"\nBarrowlandia is drowning in cabbage, {title}.")
    print("It’s in every market, sandwich, and bedtime story. The people have had enough.")

    try:
        choice = int(input("Choose your strategy:\n1) Export as eco-lettuce\n2) Launch sauerkraut festival\n3) Build Noble Cabbage statue\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge10(title)

    match choice:
        case 1:
            print("Exports succeed! Europe embraces 'green crunch'.")
        case 2:
            print("The festival is tangy and oddly emotional. Cabbage pride restored.")
        case 3:
            print("The statue is majestic. Children whisper tales of its gaze.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge10(title)

    Challenge11(title)


def Challenge11(title):
    print(f"\nA library mutiny is afoot, {title}.")
    print("Patrons must now answer riddles to check out books. Literacy is down, but riddle-solving is up.")

    try:
        choice = int(input("Choose your strategy:\n1) Reward creative librarians\n2) Replace with e-readers\n3) National riddle league\n"))
    except ValueError:
        print("Please enter a number.")
        return Challenge11(title)

    match choice:
        case 1:
            print("The librarians are heroes. One receives the 'Golden Bookmark'.")
        case 2:
            print("Chaos! Digital fires rage. A protest chant rhymes ominously.")
        case 3:
            print("Barrowlandia becomes the global epicenter of witty confusion.")
        case _:
            print("Invalid choice you gremlin. Try again.")
            return Challenge11(title)
    print(f"\nCongratulations, {title}!")
    print("You’ve navigated economic chaos, rogue librarians, magical uprisings, and musical revolutions.")
    print("The kingdom of Barrowlandia is... relatively stable. Or at least entertaining.")
    print("The people chant your name (and possibly Kevin’s) with reverence.")
    print("\nThank you for your service. Long may Barrowlandia thrive under your mildly chaotic rule!")

Welcome()