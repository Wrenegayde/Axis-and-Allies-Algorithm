import Territories

class Power( object ):
    """Model one of the five powers in the game Axis and Allies"""
    def __init__(self, team, territories, IPCs, name, isPlayer):
        """
        Initialize the power with a team, territories, IPCs, and a name
        """
        self.__team = team
        self.__territories = territories
        self.__IPCs = IPCs
        self.__name = name
        self.__isPlayer = isPlayer
    
    def __str__(self):
        """Return the power's name as a string representation of the power"""
        return self.__name
    
    def __repr__(self):
        """Return the power's name as a string representation of the power"""
        return self.__name
    
    def team(self):
        """Return the power's team (Axis/Allies)"""
        return self.__team
    
    def territories(self):
        """Return the list of territories the power controls"""
        return self.__territories
    
    def IPCs(self):
        """Returns the IPCs (money) that the power currently has"""
        return self.__IPCs
    
    def spend_IPCs(self, num_spent):
        self.__IPCs -= num_spent
    
    def name(self):
        """Returns the power's name"""
        return self.__name

    def player(self):
        """Returns whether or not the power is controlled by a player"""
        return self.__name
    
    def collect_IPCs(self):
        for territory in self.__territories:
            self.__IPCs = self.__IPCs + territory.value()
    
