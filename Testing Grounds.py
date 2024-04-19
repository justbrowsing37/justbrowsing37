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


def map_check(game_state):
    current_room = game_state.current_room

    # Define the map with room names and their connections
    game_map = {
        "Gallery": {"Exits": ["Chapel"]},
        "Chapel": {"Exits": ["Gallery", "Tunnel", "Ballroom"]},
        "Tunnel": {"Exits": ["Chapel"]},
        "Head Room": {"Exits": ["Kettle Room", "Pot Room"]},
        "Pot Room": {"Exits": ["Head Room"]},
        "Lab": {"Exits": ["Head Room"]},
        "Dungeon": {"Exits": ["Stairs", "Torture Chamber"]},
        "Stairs": {"Exits": ["Dungeon", "Kettle Room"]},
        "Kettle Room": {"Exits": ["Stairs"]},
        "Torture Chamber": {"Exits": ["Dungeon", "Armory"]},
        "Armory": {"Exits": ["Torture Chamber"]},
        "Room": {"Exits": ["Stairs"]}
    }

    # Define the map layout with room connections
    map_layout = [
        "                 Gallery",
        "                    |",
        "Ballroom -------- Chapel ----- Tunnel",
        "(Fireplace)         |           ",
        "                    |              Head Room -- Pot Room -- Lab",
        "                    |                |",
        "Dungeon -------- Stairs -------- Kettle Room",
        "   |                |",
        "Torture -- Armory   |",
        "                    |",
        "                   Room"
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


# Example usage:
game_state = {"current_room": "Chapel"}
map_check(game_state)