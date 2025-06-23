import os
import random
# --- LeaderboardManager Class ---
class LeaderboardManager:
    """
    Manages the game leaderboard, including loading, updating, adding,
    and saving scores.
    """
    def __init__(self, filename='Barrowlandia_Leaderboard.txt'): # Changed filename for clarity
        """
        Initializes the LeaderboardManager with the specified filename.
        Ensures the leaderboard file exists.
        """
        self.filename = filename
        self.leaderboard_data = []  # Stores data as list of [username, points]
        self._ensure_file_exists()
        self._load_leaderboard()

    def _ensure_file_exists(self):
        """
        Creates the leaderboard file if it doesn't already exist.
        """
        if not os.path.exists(self.filename):
            try:
                with open(self.filename, 'w') as f:
                    f.write("") # Create an empty file
                print(f"Created new leaderboard file: {self.filename}")
            except IOError as e:
                print(f"Error creating file {self.filename}: {e}")

    def _load_leaderboard(self):
        """
        Loads the leaderboard data from the file.
        Each line is expected to be 'username,points'.
        """
        self.leaderboard_data = [] # Clear existing data
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    # Strip whitespace, then split by comma
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        username = parts[0].strip()
                        try:
                            # Convert points to an integer
                            points = int(parts[1].strip())
                            self.leaderboard_data.append([username, points])
                        except ValueError:
                            print(f"Warning: Could not parse points for line: '{line.strip()}'")
                    else:
                        print(f"Warning: Skipping malformed line in leaderboard: '{line.strip()}'")
            # Sort the leaderboard by points in descending order after loading
            self._sort_leaderboard()
        except FileNotFoundError:
            # This specific error is handled by _ensure_file_exists, so it's less likely to occur
            # here unless the file was deleted between _ensure_file_exists and _load_leaderboard.
            print(f"Leaderboard file '{self.filename}' not found. A new one will be created on save.")
        except IOError as e:
            print(f"Error reading leaderboard file {self.filename}: {e}")

    def _save_leaderboard(self):
        """
        Saves the current leaderboard data back to the file.
        Each entry is written as 'username,points' on a new line.
        """
        # Ensure the leaderboard is sorted before saving
        self._sort_leaderboard()
        try:
            with open(self.filename, 'w') as file:
                for entry in self.leaderboard_data:
                    file.write(f"{entry[0]},{entry[1]}\n")
            print("Leaderboard saved successfully.")
        except IOError as e:
            print(f"Error writing to leaderboard file {self.filename}: {e}")

    def _sort_leaderboard(self):
        """
        Sorts the leaderboard data by points in descending order.
        """
        # Sorts by the second element (points), in reverse (descending) order
        self.leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    def update_score(self, username, new_points):
        """
        Updates a player's score. If the username exists and the new_points
        are higher, the score is updated. If the username doesn't exist,
        a new entry is added.
        Automatically saves the leaderboard after update.
        """
        found = False
        for i, entry in enumerate(self.leaderboard_data):
            if entry[0] == username:
                if new_points > entry[1]:
                    self.leaderboard_data[i][1] = new_points
                    print(f"Updated {username}'s score to {new_points}.")
                else:
                    print(f"{username}'s current score ({entry[1]}) is higher or equal. No update needed.")
                found = True
                break # Exit loop once user is found

        if not found:
            self.leaderboard_data.append([username, new_points])
            print(f"Added new player {username} with score {new_points}.")

        self._save_leaderboard() # Save changes immediately

    def get_top_scores(self, num_scores=10):
        """
        Returns a formatted string of the top 'num_scores' entries.
        """
        if not self.leaderboard_data:
            return "\n--- LEADERBOARD ---\nLeaderboard is currently empty.\n-------------------\n"

        top_entries = self.leaderboard_data[:num_scores]
        output = "\n--- LEADERBOARD ---\n"
        output += "Rank | Username    | Score\n"
        output += "--------------------------\n"
        for i, entry in enumerate(top_entries):
            # Ensure username and score are formatted correctly.
            # Using str() in case a malformed entry somehow made it in
            output += f"{i+1:<4} | {str(entry[0]):<11} | {str(entry[1]):<5}\n"
        output += "--------------------------\n"
        return output

# --- Global Leaderboard Manager Instance ---
# This will be initialized once when the script runs.
leaderboard = LeaderboardManager()

# --- Game Functions ---

def Welcome():
    print('Welcome trusted servant of the state!\nMy Name is Gerald and I have asked you here to provide us with your wisdom.\nThe People of Barrowlandia are revolting against us in the government.\nWe need you to calm the people, maintain our power, create rest in our kingdom.\nWe are relying on YOU!')

    player_username = ""
    while not player_username:
        player_username = input("Please choose a username: ").strip()
        if not player_username:
            print("Username cannot be empty. Please try again.")

    title = ""
    while True:
        try:
            choice1 = int(input('Choose your title:\n1) Lord Garry\n2) Lady Janet\n3) Sir Derek IV\n'))
        except ValueError:
            print("Please enter a number.")
            continue # Loop continues until valid input

        match choice1:
            case 1:
                title = "Lord Garry"
                break
            case 2:
                title = "Lady Janet"
                break
            case 3:
                title = "Sir Derek IV"
                break
            case _:
                print("Invalid choice you gremlin. Try again")
        
    print(f"Greetings {title}! I look forward to serving with you.")
    
    # Start the challenges with the initial score
    Challenge1(player_username, title, 0) # Initial score is 0


def Challenge1(username, title, current_score):
    print(f'\nIt is time for your first challenge, {title}!')
    print('The people of Barrowlandia are facing an economic depression.')
    print('The people are hopeless and depressed!')
    print('We have 3 choices, choose wisely as the people are relying on you.')

    score_change = 0
    while True:
        try:
            choice2 = int(input('Choose your strategy:\n1) Place funding into industry to support jobs\n2) Provide cheap beer to raise spirits\n3) Increase state benefits and universal credit to improve the standard of living\n'))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice2:
            case 1:
                print("Fantastic choice. The people are starting to realise that there are opportunities out there.\nAlthough there is still work to do, spirits are still low.")
                score_change = 10
                break
            case 2:
                print("Well what a nice idea!!\nUnfortunately, the cheap booze caused a riot at the rugby.\n150 people died\nBUT spirits are still high! (Pun Intended)")
                score_change = 0 
                break
            case 3:
                print("Whatever are we paying you for?\nThe people have given up any kind of employment and are becoming couch potatoes.")
                score_change = -5 
                break
            case _:
                print("Invalid choice you gremlin. Try again")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge2(username, title, current_score)


def Challenge2(username, title, current_score):
    print(f"\nThe time has arrived for your second opportunity to prove yourself, {title}!")

    score_change = 0
    while True:
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
            continue

        match choice:
            case 1:
                print("The new buses are shiny, quiet, and smell faintly of pine. Commuters are cautiously optimistic, though one still insists the duck pond tram was 'a sign'.")
                score_change = 25
                break
            case 2:
                print("The fare freeze is a hit! People are still late, but at least they’re late for free. One man now rides the bus just for the scenery.")
                score_change = 5
                break
            case 3:
                print("The consultation was thorough. You now have 4,000 opinions, 3 conspiracy theories, and one poem about potholes. Action pending.")
                score_change = 0
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge4(username, title, current_score)


def Challenge4(username, title, current_score): 
    print(f"\nAnother challenge awaits, {title}.")
    print("Youth unemployment is rising. Many are disillusioned and dangerously close to forming a ska band.")
    print("You must act before social media becomes their only career plan.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Expand apprenticeships\n2) Fund youth entrepreneurship\n3) Launch a national volunteer service\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("Young people are gaining skills. One now calls himself 'Barrowlandia’s Premier Plumber'.")
                score_change = 25
                break
            case 2:
                print("Startups bloom! One teen invents a plant pot that screams when thirsty. Investors are intrigued.")
                score_change = 15
                break
            case 3:
                print("Volunteering surges! One group knits 300 scarves for local llamas. No one knows why, but spirits are high.")
                score_change = 5
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge5(username, title, current_score)


def Challenge5(username, title, current_score):
    print(f"\nA crisis at the docks, {title}!")
    print("Barrowlandia’s shipbuilding industry is facing delays and budget overruns. Workers are frustrated, and the press is circling like seagulls near chips.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Increase funding and improve project management\n2) Launch a PR campaign highlighting the industry’s legacy\n3) Invite naval officials for a morale-boosting visit\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The funding helps! Projects get back on track, though one vessel still mysteriously beeps to the tune of 'God Save the King'.")
                score_change = 22
                break
            case 2:
                print("The PR campaign is slick. One ad features a ship majestically sailing past a wind farm. Locals are proud, if slightly confused.")
                score_change = 15
                break
            case 3:
                print("The naval visit boosts morale! One officer is now dating the mayor’s cousin. Unexpected diplomacy!")
                score_change = 50
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge6(username, title, current_score)


def Challenge6(username, title, current_score):
    print(f"\nTransport trouble, {title}!")
    print("A key bridge in Barrowlandia is undergoing repairs, causing traffic chaos. Commuters are late, cyclists are grumpy, and one person tried to cross in a kayak.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Introduce a temporary ferry service\n2) Offer free coffee to delayed commuters\n3) Accelerate bridge repairs with night shifts\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The ferry is a hit! One passenger insists on calling it 'The HMS Shortcut'.")
                score_change = 20
                break
            case 2:
                print("Free coffee calms tempers. Productivity drops slightly due to caffeine-fueled storytelling.")
                score_change = 5
                break
            case 3:
                print("Repairs speed up! The night crew includes a man who swears he once fixed Big Ben. Spirits rise.")
                score_change = 25
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge7(username, title, current_score)


def Challenge7(username, title, current_score):
    print(f"\nA cultural conundrum, {title}!")
    print("Barrowlandia’s annual summer festival is at risk of cancellation due to budget cuts and a rogue brass band that refuses to play anything but ABBA.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Secure local sponsorships to fund the festival\n2) Rebrand it as a community picnic with music\n3) Let the brass band lead and hope for the best\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("Local businesses step up! One bakery sponsors a pie-eating contest. The festival is saved — and delicious.")
                score_change = 25
                break
            case 2:
                print("The picnic is peaceful. The band plays ABBA. People dance. A dog wins the talent show. Success!")
                score_change = 20
                break
            case 3:
                print("The band plays 'Dancing Queen' on loop. The crowd is confused, but oddly united. A new tradition is born.\nThose who don't like ABBA kick off and play nickelback. Tears are cried")
                score_change = -5 
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge9(username, title, current_score) # Changed from Challenge8


def Challenge9(username, title, current_score):
    print(f"\nThe lights go out every Thursday evening, {title}.")
    print("Citizens host candlelit poetry slams, but they're starting to wonder why Thursdays are so cursed.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Invest in renewable energy\n2) Implement traditional rolling blackouts\n3) Train squirrels to generate power\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("Solar and wind save the day! Though one wind-turbine has become self-aware.")
                score_change = 30
                break
            case 2:
                print("People accept the tradition. Thursday becomes 'Glowstick Yoga Night'.")
                score_change = 10
                break
            case 3:
                print("The squirrels are enthusiastic but prone to unionizing. Mixed results.\nOnly generate enough power to charge the mayors girlfriends Cupra")
                score_change = 5
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge10(username, title, current_score)


def Challenge10(username, title, current_score):
    print(f"\nBarrowlandia is drowning in cabbage, {title}.")
    print("It’s in every market, sandwich, and bedtime story. The people have had enough.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Export as eco-lettuce\n2) Launch sauerkraut festival\n3) Build Noble Cabbage statue\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("Exports succeed! Europe embraces 'green crunch'.")
                score_change = 25
                break
            case 2:
                print("The festival is tangy and oddly emotional. Cabbage pride restored.")
                score_change = 20
                break
            case 3:
                print("The statue is majestic. Children whisper tales of its gaze.\nThose with a level of education brand it as a shocking waste of money\nOur image is tarnished to all those over the age of 7")
                score_change = -8
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge11(username, title, current_score)


def Challenge11(username, title, current_score):
    print(f"\nA library mutiny is afoot, {title}.")
    print("Patrons must now answer riddles to check out books. Literacy is down, but riddle-solving is up.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Reward creative librarians\n2) Replace with e-readers\n3) National riddle league\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The librarians are heroes. One receives the 'Golden Bookmark'.")
                score_change = 25
                break
            case 2:
                print("Chaos! Digital fires rage. A protest chant rhymes ominously.")
                score_change = -5 
                break
            case 3:
                print("Barrowlandia becomes the global epicenter of witty confusion.")
                score_change = 15
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge12(username, title, current_score)


def Challenge12(username, title, current_score):
    print(f"\nAccusations arise from Millomvia, {title}!")
    print("They claim you’ve stolen their sacred sheep. Bahh-d news.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Deny and fruit basket\n2) Tea and peace talks\n3) Let the sheep choose\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The fruit was appreciated. No one trusts you, but they’re less angry.")
                score_change = 0
                break
            case 2:
                print("Diplomacy! Crumbs mend rifts. A new alliance brews.")
                score_change = 25
                break
            case 3:
                print("The sheep pick Barrowlandia. National anthem now includes a 'baa'.")
                score_change = 20
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge13(username, title, current_score)


def Challenge13(username, title, current_score):
    print(f"\nThe statue of King Barry I is crumbling, {title}.")
    print("It's rusted and oddly weeping. Pigeons have claimed it as sacred ground.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Commission modern replacement\n2) Spray gold and call it retro\n3) Add googly eyes\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The new statue glistens. It spins and plays a lute at noon.")
                score_change = 25
                break
            case 2:
                print("Retro indeed! Locals wear matching jumpers. The ‘80s are back.\nBUGGER...")
                score_change = -30
                break
            case 3:
                print("The googly eyes bring joy to all. Tourists flock in droves.")
                score_change = 20
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge14(username, title, current_score)


def Challenge14(username, title, current_score):
    print(f"\nYou've uncovered a tunnel beneath the town hall, {title}!")
    print("Inside: ancient scrolls and surprisingly fizzy mead barrels.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Launch dig site\n2) Turn it into 'The Boozy Catacombs'\n3) Seal it forever\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("History is rewritten! Tours begin Monday.")
                score_change = 25
                break
            case 2:
                print("Tourists swarm. Someone opens a medieval-themed gastropub.")
                score_change = 20
                break
            case 3:
                print("It’s buried once again. Locals nod solemnly.")
                score_change = 5
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge15(username, title, current_score)


def Challenge15(username, title, current_score):
    print(f"\nMagic is trending in Barrowlandia, {title}.")
    print("Illusions abound. The mayor now disappears at council meetings.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Found Ministry of Illusion\n2) Promote STEM-magic\n3) Ban sorcery outright\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The Ministry dazzles. One magician reboots the postal service.")
                score_change = 25
                break
            case 2:
                print("Science meets sorcery. Barrowlandia wins 'Most Enchanted Tech' award.")
                score_change = 30
                break
            case 3:
                print("Underground wizard cabals rise. You didn’t hear it from me.")
                score_change = -10 
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge16(username, title, current_score)


def Challenge16(username, title, current_score):
    print(f"\nYour AI Oracle is glitching, {title}.")
    print("It predicts 'Mild sock unrest' and that 'Spoons are conspiring'.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Reboot and blame sarcasm\n2) Promote it as prophet\n3) Replace with hamster named Kevin\n"))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                print("The reboot works. The Oracle now dispenses weather and sandwich tips.")
                score_change = 20
                break
            case 2:
                print("Cult forms. They wear aluminum hats but remain very polite.")
                score_change = 5
                break
            case 3:
                print("Kevin is popular. He spins in his wheel before major decisions.")
                score_change = 15
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")
    Challenge17(username, title, current_score)


def Challenge17(username, title, current_score):
    print(f"\nAn anthem crisis rocks the realm, {title}.")
    print("Citizens want to replace it with an accordion remix. The nobles are sweating.")

    score_change = 0
    while True:
        try:
            choice = int(input("Choose your strategy:\n1) Hold a national music vote\n2) Embrace the remix\n3) Declare spontaneous bank holiday\n"))
        except ValueError:
            print("Please enter a number.")
            continue
        match choice:
            case 1:
                print("A national contest ensues. The remix wins by landslide.")
                score_change = 25
                break
            case 2:
                print("Accordion fever sweeps the land. Schools now teach polka.\nCould it get much worse... If only it was plague!")
                score_change = -20
                break
            case 3:
                print("People forget the issue. Everyone loves a day off.")
                score_change = 15
                break
            case _:
                print("Invalid choice you gremlin. Try again.")
    
    current_score += score_change
    print(f"Current Score: {current_score}")

    print(f"\nCongratulations, {title}!")
    print(f"You’ve navigated economic chaos, rogue librarians, magical uprisings, and musical revolutions.")
    print(f"Your final score is: {current_score}")
    print("The kingdom of Barrowlandia is... relatively stable. Or at least entertaining.")
    print("The people chant your name (and possibly Kevin’s) with reverence.")
    print("\nThank you for your service. Long may Barrowlandia thrive under your mildly chaotic rule!")

    # Update the leaderboard with the player's final score
    leaderboard.update_score(username, current_score)

    # Offer to show the leaderboard
    while True:
        view_leaderboard = input("\nWould you like to view the leaderboard? (yes/no): ").lower().strip()
        if view_leaderboard == 'yes':
            print(leaderboard.get_top_scores())
            break
        elif view_leaderboard == 'no':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


# --- Game Start ---
if __name__ == "__main__":
    Welcome()