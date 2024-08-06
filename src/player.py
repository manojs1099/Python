# player.py

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"Player {self.name} is currently in {self.current_room.name}"
