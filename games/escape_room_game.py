import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.neighbors = {}

    def add_neighbor(self, direction, room):
        self.neighbors[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        return f"{self.name}\n\n{self.description}"

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.current_room = random.choice(list(self.rooms.values()))
        self.inventory = []

    def create_rooms(self):
        room_names = ["Entrance", "Hallway", "Kitchen", "Treasure Room", "Exit Room"]
        descriptions = {
            "Entrance": "You are at the entrance of a dark cave.",
            "Hallway": "A narrow hallway. It smells damp and musty.",
            "Kitchen": "An old kitchen with rusty appliances.",
            "Treasure Room": "The treasure room. You see a glittering chest in the corner.",
            "Exit Room": "The exit door is here, but it seems to be locked."
        }
        rooms = {name: Room(name, descriptions[name]) for name in room_names}

        directions = ["north", "south", "east", "west"]
        for room in rooms.values():
            potential_neighbors = [r for r in rooms.values() if r != room]
            neighbors = random.sample(potential_neighbors, k=random.randint(1, 4))
            random.shuffle(directions)
            for direction, neighbor in zip(directions, neighbors):
                room.add_neighbor(direction, neighbor)

        key = Item("Key", "A small rusty key. It might open something important.")
        rooms["Treasure Room"].add_item(key)

        return rooms

    def move(self, direction):
        if direction in self.current_room.neighbors:
            self.current_room = self.current_room.neighbors[direction]
            print(f"\nYou move to the {self.current_room.name}.\n")
        else:
            print("\nYou can't go that way.\n")

    def pick_up_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"\nYou picked up the {item.name}.\n")
                return
        print("\nThere is no such item here.\n")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.name == "Key" and self.current_room.name == "Exit Room":
                    print("\nYou use the key to unlock the exit door. You have escaped!\n")
                    self.inventory.remove(item)
                    return True
                else:
                    print("\nYou can't use that item here.\n")
                return False
        print("\nYou don't have that item.\n")
        return False

    def show_status(self):
        print(self.current_room)
        if self.current_room.items:
            print("\nItems in this room:")
            for item in self.current_room.items:
                print(f"- {item.name}")
        if self.inventory:
            print("\nYour inventory:")
            for item in self.inventory:
                print(f"- {item.name}")
        print()

    def play(self):
        print("Welcome to Cave Quest!")
        print()        
        print("You are in a dark cave.")	
        print("Search key for exit door and escape the cave by looking around the room to find the key and use it to open the exit door.")
        print()
        print("You see exits to the north, south, east, and west.")
        print("What would you like to do?")
        print()
        print("Type 'help' to see a list of commands.\n")
        self.show_status()

        while True:
            command = input("> ").strip().lower()
            if command in ["quit", "exit"]:
                print("\nThanks for playing Cave Quest!")
                break
            elif command == "help":
                print("\nCommands:\n")
                print("go [direction] - Move in a direction (north, south, east, west)")
                print("pick up [item] - Pick up an item")
                print("use [item] - Use an item")
                print("look - Look around")
                print("inventory - Check your inventory")
                print("quit - Quit the game\n")
            elif command.startswith("go "):
                direction = command.split(" ")[1]
                self.move(direction)
            elif command.startswith("pick up "):
                item_name = command[8:]
                self.pick_up_item(item_name)
            elif command.startswith("use "):
                item_name = command[4:]
                if self.use_item(item_name):
                    break
            elif command == "look":
                self.show_status()
            elif command == "inventory":
                print("\nYour inventory:")
                for item in self.inventory:
                    print(f"- {item.name}")
                print()
            else:
                print("\nInvalid command. Type 'help' to see a list of commands.\n")

if __name__ == "__main__":
    game = Game()
    game.play()
