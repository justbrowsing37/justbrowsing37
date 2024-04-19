import time, os, sys, random, json

os.system('cls')

####################    CLASSES    ###################

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class GameState:
    def __init__(self, current_room=None, player_inventory=None):
        self.current_room = current_room if current_room else "Chapel"  # Start in the Chapel by default
        self.player_inventory = player_inventory if player_inventory else []

    def to_dict(self):
        return {
            "current_room": self.current_room,
            "player_inventory": self.player_inventory
        }

    @classmethod
    def from_dict(cls, state_dict):
        return cls(state_dict["current_room"], state_dict["player_inventory"])


class StopWatch:
    def __init__(self):
        self.startTime = None
        self.elapsedTime = 0
        self.isRunning = False

    def start(self):
        if not self.isRunning:
            self.startTime = time.time()
            self.isRunning = True

    def stop(self):
        if self.isRunning:
            self.elapsedTime = time.time() - self.startTime
            self.isRunning = False

    def reset(self):
        self.elapsedTime = 0
        self.isRunning = False

    def getElapsedTime(self):
        totalTime = self.elapsedTime
        if self.isRunning:
            totalTime += time.time() - self.startTime
        print(f"Time survived: {totalTime:.2f} seconds")









####################   UI STUFF    ###################

signatures = [
    "- Professional Moron",
    "- Car Enthusiast",
    "- The one and only Indian and Team",
    "- Your neighborhood idiot",
    "- Diphosphourus Trijasonide",
    "- Hyaa'sa ibn Jy'ud al-Qalai",
    "- Chu Che-Huo",
    "- Aluminum Nitrate",
    "- Afar ibn Baani al-Riyal and Team",
    "- Sulfur Hydrochloride",
    "- Nate Horne",
    "- Boris Skolensky",
    "- Gilberto Raymond and Team",
    "- Max Verstappen"
]
random_sign = random.choice(signatures)



def GameIntro():
    show_bar()
    os.system('cls')
    print_instructions()




def progress_bar(iteration, total, bar_length=60):
    percent = "{0:.3f}".format(100 * (iteration / float(total)))
    filled_length = int(bar_length * iteration // total)
    bar = (Color.GREEN + '█' + Color.END) * filled_length + (Color.RED + '█' + Color.END) * (
            bar_length - filled_length)
    sys.stdout.write('\r║%s║ %s%% ' % (bar, percent))
    sys.stdout.flush()

    if iteration < total / 2:
        time.sleep(0.1)
    elif iteration < total * 0.9:
        time.sleep(0.2)
    else:
        time.sleep(0.5)




def clear_bar():
    print('\n')
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")




def show_bar():
    Message()
    time.sleep(2)

    print("\nInitializing....")
    time.sleep(0.5)
    total_iterations = 50
    for i in range(total_iterations + 1):
        progress_bar(i, total_iterations)
    time.sleep(1.5)
    clear_bar()
    print("\nExtracting text...")
    time.sleep(0.5)
    total_iterations = 75
    for i in range(total_iterations + 1):
        progress_bar(i, total_iterations)
    time.sleep(0.5)
    clear_bar()
    print("\nPreparing output...")
    time.sleep(0.5)
    total_iterations = 137
    for i in range(total_iterations + 1):
        progress_bar(i, total_iterations)
    time.sleep(0.5)

    print("\n\nReady to play")
    print("\nPress Enter")
    input("")
    os.system('cls')
    print((Color.BOLD + Color.UNDERLINE + "Please wait..." + Color.END))
    time.sleep(5)
    os.system('cls')





def Message():
    print("\nThe following game is " + (
            Color.BOLD + '  𝘊 𝘈 𝘚 𝘌    𝘚 𝘌 𝘕 𝘚 𝘐 𝘛 𝘐 𝘝 𝘌' + Color.END) + "\n        (im working on it... dont judge me)")
    print(f"\n\nThis project took me months to make... I hope you enjoy!\n     {random_sign}")
    print("\n\n" + "↓↓" + (
            Color.BOLD + Color.UNDERLINE + 'PLEASE WAIT FOR INSTRUCTIONS BELOW... DO NOT TYPE' + Color.END) + "↓↓")




def print_instructions():
    print((Color.BOLD + "Welcome to VOODOO CASTLE!" + Color.END).center(108))
    print("\n                  Welcome player to my wonderful creation! Just know that this is\n                  a test module and things in here are all subject to change. But\n                  don't worry too much. Since I am a very crazy person and I am \n                  always looking for new ways to improve my game! So if you have \n                  any ideas for the game, Be sure to let me know! Anyways, some \n                  commands are |'move', 'take', and 'use'| Have fun! - Bhanu S. :)")
    print("               ---------------------------------------------------------------------")
    print("\n")




def separation():
    linebreaks = (
            Color.BOLD + '______________________________________________________________________________________________' + Color.END)
    linebreaks_ = (
            Color.UNDERLINE + '\n║                                                                                            ║' + Color.END)
    print(linebreaks, linebreaks_)








####################   GAME PLAY    ###################



def display_room_info(current_room, game_map):
    room_info = game_map[current_room]
    print("\nCurrent Room: " + current_room)
    print("Description:" + room_info["Description"])
    print("Exits:", ", ".join(room_info["Exits"]))
    print("Items in the room:", ", ".join(room_info["Items"]))
    print("Objects in the room:", ", ".join(room_info["Objects"]))




def Take(game_state, game_map):
    current_room_info = game_map[game_state.current_room]

    item_name = input("Which item would you like to pick up? ").strip().lower()

    if item_name in current_room_info["Items"]:
        # Remove the item from the room and add it to the player's inventory
        current_room_info["Items"].remove(item_name)
        game_state.player_inventory.append(item_name)
        print(f"You took the {item_name}.")
    else:
        print("There is no such item in the room.")
    return game_state





def move(game_state, game_map, directions):
    current_room_state = game_state.current_room
    current_room_info = game_map[current_room_state]

    # Get player's input for movement command
    move_command_input = input("Which direction would you like to move?: ").strip().lower()

    # Check if the move command is valid
    if move_command_input in directions:
        direction = directions[move_command_input]
        if direction in current_room_info["Exits"]:
            new_room = current_room_info["Exits"][direction]
            print(f"You moved to the {new_room}.")
            game_state.current_room = new_room  # Update the current room
        else:
            print("You can't move in that direction.")
    else:
        print("Invalid move command.")

    return game_state





def use(game_state, usable_items):
    item_name = input("What would you like to use?: ")

    if item_name in game_state.player_inventory and item_name in  usable_items:
        print(f"You used the {item_name}")
        #Put the different print actions here
        game_state.player_inventory.remove(item_name)
    elif item_name not in game_state.player_inventory:
        print("That item is not in your inventory.")
    elif item_name not in usable_items:
        print("You can't use that item.")
    else:
        print("That item doesn't exist.")




def eat(game_state, edible_items):
    item_name = input("What would you lke to eat?")

    if item_name in game_state.player_inventory and item_name in edible_items:
        print(f"You ate {item_name}, Yum yum yum!")
        #Add any effects that the player might experience.
        game_state.player_inventory.remove(item_name)
    elif item_name not in game_state.player_inventory:
        print("That item is not in your inventory")
    elif item_name not in edible_items:
        print("You cant eat this item. Stupid.")
    else:
        print("That item doesn't exist.")




def inv_check(game_state):
    if not game_state.player_inventory:
        print("Your inventory is empty...")
    else:
        print("Your inventory: ")
        for item in game_state.player_inventory:
            print(f"- {item}")





game_map = {
    "Chapel": {
        "Description": " I am standing in a majestic chapel."
                       "\n             There is a coffin in front of me.",
        "Exits": {"north": "Gallery", "east": "Tunnel", "west": "Ballroom (Fireplace)", "south": "Stairs"},
        "Items": [],
        "Objects": ["coffin"]
    },
    "Gallery": {
        "Description": " There is a big window at the top of the stairs."
                       "\n             The view from here is amazing...",
        "Exits": {"south": "Chapel"},
        "Items": [],
        "Objects": ["window"]
    },
    "Ballroom (Fireplace)": {
        "Description": " I am standing in the grand ballroom..."
                       "\n             Sure will you had a girl to dance with don't you?",
        "Exits": {"east": "Chapel"},
        "Items": [],
        "Objects": []
    },
    "Tunnel": {
        "Description": " I am in a tunnel with limestone walls."
                       "\n             There is a large stone door with a Sapphire in the middle.",
        "Exits": {"west": "Chapel"},
        "Items": ["bloody knife"],
        "Objects": []
    },
    "Stairs": {
        "Description": " I am in a dingy looking stairwell."
                       "\n             Broken glass is everywhere, looks like an explosion happened?",
        "Exits": {"north": "Chapel", "east": "Kettle Room", "south": "Room", "west": "Dungeon"},
        "Items": ["broken glass"],
        "Objects": []
    },
    "Room": {
        "Description": "\nYou are in a plain, nondescript room.",
        "Exits": {"north": "Armory"},
        "Items": [],
        "Objects": []
    },
    "Kettle Room": {
        "Description": "\nThis looks like their version of a kitchen."
                       "\nLost of pots, pans, and kettles are in the sink...",
        "Exits": {"north": "Head Room", "west": "Stairs"},
        "Items": [],
        "Objects": []
    },
    "Head Room": {
        "Description": "\nIm standing in the room filled with animal heads."
                       "\nIt looks like these guys loved to hunt...",
        "Exits": {"east": "Pantry", "south": "Kettle Room"},
        "Items": [],
        "Objects": []
    },
    "Pantry": {
        "Description": "\nFound the pantry, Might as well take a bite!"
                       "\nI wonder why they need a pantry in a chapel?",
        "Exits": {"west": "Head Room", "east": "Lab"},
        "Items": ["Meat", "Bread"],
        "Objects": ["Basket"]
    },
    "Lab": {
        "Description": "\nA Lab? What kind of a chapel is this?"
                       "\nAnyways, I wonder what they might be doing in here?",
        "Exits": {"west": "Pantry"},
        "Items": [],
        "Objects": ["chemicals"]
    },
    "Dungeon": {
        "Description": "\nThe dungeon seems to be a bit dusty,"
                       "\nThere are skeletons on the ground...",
        "Exits": {"east": "Stairs", "south": "Torture Chamber"},
        "Items": ["metal chain", "key"],
        "Objects": ["gate"]
    },
    "Torture Chamber": {
        "Description": "\nOne of the worst rooms in the whole castle",
        "Exits": {"north": "Dungeon", "east": "Armory"},
        "Items": ["bones", "Sword"],
        "Objects": ["Skeleton", "Bones"]
    },
    "Armory": {
        "Description": "\nLooks like you found the weapons hub of this whole place,"
                       "\nReally Staring to look more like a castle rather than a chapel",
        "Exits": {"west": "Torture Chamber"},
        "Items": ["Handcuffs"],
        "Objects": []
    }
}

'''
View of the game map:

                 Gallery
		  	        |
Ballroom -------- Chapel ----- Tunnel
(Fireplace)         |
		  	        |              Repository -- Pantry -- Lab
		            |                 |
Dungeon --------- Stairs --------- Kitchen
   |                |
Torture --- Armory  |
                    |
                   Room
'''

moves = ["n", "e", "s", "w", "take", "slide", "move", "turn", "climb", "push", "circle", "inventory", "map"]
items = []
usable_items = []
edible_items = []
objects = []


directions = {
    'n': 'north',
    'e': 'east',
    's': 'south',
    'w': 'west',
}






############# Testing cases #############

def map_check(game_state):
    current_room = game_state.current_room

    print(f"Your current room is {current_room}")
  #←→↑↓«»

    game_map = {
        "Gallery": {"Exits": ["Chapel"]},
        "Chapel": {"Exits": ["Gallery", "Tunnel", "Head Room"]},
        "Tunnel": {"Exits": ["Chapel"]},
        "Repository": {"Exits": ["Chapel", "Pot Room", "Lab"]},
        "Pantry": {"Exits": ["Head Room"]},
        "Lab": {"Exits": ["Head Room"]},
        "Dungeon": {"Exits": ["Stairs", "Torture Chamber"]},
        "Stairs": {"Exits": ["Dungeon", "Kettle Room"]},
        "Kitchen": {"Exits": ["Stairs"]},
        "Torture Chamber": {"Exits": ["Dungeon", "Armory"]},
        "Armory": {"Exits": ["Torture Chamber"]},
        "Room": {"Exits": []}
    }



    # Define the map layout with room connections
    map_layout = [
        "                                                       Compass:     ↑N↑",
        "                   Gallery                                      « W [♦] E »",
        "                      |                                             ↓S↓",
        "Ballroom --------- Chapel ------- Tunnel",
        "(Fireplace)           |           ",
        "                      |            Repository -- Pantry -- Lab",
        "                      |               |",
        "Dungeon ---------- Stairs -------- Kitchen",
        "   |                  |",
        "Torture -- Armory     |",
        "                      |",
        "                    Room",
        "",
        ""
    ]

    # Print the map with the current room highlighted in green
    print("Game Map:")
    for room_line in map_layout:
        line = ""
        for room_name in room_line.split(" "):
            if room_name == current_room:
                line += Color.GREEN + room_name + Color.END + " "
            else:
                line += room_name + " "
        print(line)






def save_game(game_state):
    with open("game_state.json", "w") as file:
        json.dump(game_state.to_dict(), file)


def load_game():
    try:
        with open("game_state.json", "r") as file:
            return GameState.from_dict(json.load(file))
    except FileNotFoundError:
        return None




def main():
    os.system('cls')
    while True:
        game_state = load_game()
        if game_state is None:
            game_state = GameState()

        print_instructions()

        while game_state.current_room:
            display_room_info(game_state.current_room, game_map)
            command = input("\nWhat would you like to do?: ").strip().lower()

            if command == "save":
                save_game(game_state)
                print("Game saved.")
                continue
            
            if command == "inventory":
                inv_check(game_state)
                continue

            if command not in moves:
                print(f"You don't know how to '{command}'")
                separation()
                continue

            if command == "take":
                game_state = Take(game_state)
                separation()
            elif command == "move":
                game_state = move(game_state, game_map,  directions)
                separation()
            elif command == "map":
                map_check(game_state)

main()