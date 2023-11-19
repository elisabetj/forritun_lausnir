class Player:
    
    def __init__(self, first_name, last_name):
        """Initializes a new instance of a Player."""
    
        self.first_name = first_name
        self.last_name = last_name
        self.goals = 0

    def __str__(self):
        """Returns a string representation of self."""
    
        return f"{self.first_name} {self.last_name}, Goals: {self.goals}"

    def add_goals(self, goals):
        """Adds the given goals to the goals of self."""

        self.goals += goals