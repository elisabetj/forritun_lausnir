class Team:

    def __init__(self, name):
        """Initializes a new instance of a Team."""
        
        self.name = name
        self.players = []
    
    def __str__(self):
        """Returns a string representation of self.
        Players are orderder in descreasing order of goals scored.
        """

        return_str = f"{self.name}:"
        for player in sorted(self.players, key=lambda p: p.goals, reverse=True):
            return_str += f"\n\t{str(player)}"

        return return_str

    def add_player(self, player):
        """Adds the given student to the student list."""

        self.players.append(player)
            
    def most_goals_player(self):
        """Returns the player who has scored most goals.
        If two or more players have scored equal number of goals,
        the one that was added to the team first is returned.
        """
        
        return max(self.players, key = lambda p: p.goals)

    def __add__(self, other):
        '''Returns a new team whose name is the concatenation of
        the names of the two teams and whose players are the players
        in the first teams followd by the players in the second team.
        '''
        new_team = Team(f"{self.name}+{other.name}")
        for player in self.players:
            new_team.add_player(player)
        for player in other.players:
            new_team.add_player(player)
        
        return new_team
        