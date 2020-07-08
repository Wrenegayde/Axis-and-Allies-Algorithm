from random import randint

class Unit(object):
    """
    Represents a unit in the game of axis and allies.
        
    """
    def __init__(self,attack=0,defense=0,cost=0,move=0,has_moved=0,power=None):
        """
        Default parameters set attack, defense, cost, move, and has_moved to 0
        """
        self.__atk_score = attack
        self.__def_score = defense
        self.__cost = cost
        self.__move = move #maximum number of spaces this unit can move
        self.__has_moved = has_moved #numbe of spaces moved this turn
        self.__power = power
        
    def __str__(self):
        return "unit"
    
    def __repr__(self):
        return "unit"
        
	def unit_type(self):
		return "unit"
	
    def roll_die(self):
        """
        Return a random number from 1-6 inclusive
        """
        return randint(1, 6)
        
    def attack_hits(self):
        """
        Return true if the unit hits, return false otherwise
        """
        if self.roll_die() <= self.__atk_score:
            return True
        else:
            return False
       
    def defense_hits(self):
        """
        Return true if the unit hits, return false otherwise
        """
        if self.roll_die() <= self.__def_score:
            return True
        else:
            return 
    
    def get_move(self):
        """
        Return the number of tiles that this unit can move in a turn
        """
        return self.__move
    
    def get_has_moved(self):
        """
        Return the number of tiels that this unit has moved this turn
        """
        return self.__has_moved

    def set_has_moved(self,new_has_moved):
        """
        Takes an integer as a parameter, representing a number of tiles that a unit moves.
        Sets the private local variable has_moved to this value
        """
        self.__has_moved = new_has_moved



class LandUnit(Unit):
    def __init__(self,attack=0,defense=0,cost=0,move=0,power=None):
        super().__init__(attack,defense,cost,move,0,power)

    def unit_type(self):
        return "land"
        
    def __str__(self):
        return "landunit"
    
    def __repr__(self):
        return "landunit"
   
     
class Infantry(LandUnit):
    def __init__(self,attack=1,defense=2,cost=3,move=1,power=None):
        super().__init__(attack,defense,cost,move,0,power)

    def __str__(self):
        return "infantry"
    
    def __repr__(self):
        return "infantry"


class Tank(LandUnit):
    def __init__(self,attack=3,defense=2,cost=5,move=2,power=None):
        super().__init__(attack,defense,cost,move,0,power)

    def __str__(self):
        return "tank"
    
    def __repr__(self):
        return "tank"


class AntiAircraft(LandUnit):
    def __init__(self, attack=0,defense=1,cost=5,move=1,power=None):
        super().__init__(attack,defense,cost,move,0,power)
        
    def aagun_hits(self, air_units):
        """
        Takes number of attacking air units as a parameter
        Returns number of hits on air units
        """
        total_hits = 0
        for x in range(air_units):
            if super().defense_hits():
                total_hits += 1
        return total_hits

    def __str__(self):
        return "antiaircraft"
    
    def __repr__(self):
        return "antiaircraft"

	

class AirUnit(Unit):
    def __init__(self,attack=0,defense=0,cost=0,move=0,power=None):
        super().__init__(attack,defense,cost,move,0,power)
        
    def unit_type(self):
        return "air"

    def __str__(self):
        return "airunit"
    
    def __repr__(self):
        return "airunit"
    

class Fighter(AirUnit):
    def __init__(self,attack=3,defense=4,cost=12,move=4,power=None):
        super().__init__(attack,defense,cost,move,0,power)

    def __str__(self):
        return "fighter"
    
    def __repr__(self):
        return "fighter"
        
        
class Bomber(AirUnit):
    def __init__(self,attack=4,defense=1,cost=15,move=6,power=None):
        super().__init__(attack,defense,cost,move,0,power)
        
    def bombing_raid(self, shot_down):
        """
        Takes a boolean of whether the bomber is shot down
        Returns the number of IPCs that the target loses
        """
        if shot_down:
            return 0
        else:
            return super.roll_die()

    def __str__(self):
        return "bomber"
    
    def __repr__(self):
        return "bomber"
        
        
        
class SeaUnit(Unit):
    def __init__(self,attack=0,defense=0,cost=0,move=0,power=None):
        super().__init__(attack,defense,cost,move,0,power)

    def unit_type(self):
        return "sea"

    def __str__(self):
        return "seaunit"
    
    def __repr__(self):
        return "seaunit"
    

class Battleship(SeaUnit):#run some test cases on how this constructor works
    def __init__(self,attack=4,defense=4,cost=24,move=2,power=None):
        super().__init__(attack,defense,cost,move,0,power)
        
        #Do we want a bombard() method here, or will we add that in our combat function?

    def __str__(self):
        return "battleship"
    
    def __repr__(self):
        return "battleship"
    

class Carrier(SeaUnit):
    def __init__(self,attack=1,defense=3,cost=18,move=2,cargo=[],power=None):
        super().__init__(attack,defense,cost,move,0,power)
        self.__cargo = cargo

    def add_cargo(self,new_cargo):
        """
        takes a unit to be added to the carrier as a 
        If the unit can be added to the carrier, returns None
        If the unit cannot be added, returns the unit object
        """
        if len(self.__cargo) < 2 and type(new_cargo) == type(Fighter()):
            self.__cargo.append(new_cargo)
            return None
        else:
            return new_cargo
        
    def pop_cargo(self):
        """
        If the carrier has any cargo, its unit object is returned and removed from the carrier's cargo list
        """
        if len(self.__cargo) > 0:
            return self.__cargo.pop()
        
    def get_cargo(self):
        """
        Returns the list of unit objects in this carrier's cargo list
        """
        return self.__cargo

    def __str__(self):
        return "carrier"
    
    def __repr__(self):
        return "carrier"


class Submarine(SeaUnit):
    def __init__(self,attack=2,defense=2,cost=8,move=2,power=None):
        super().__init__(attack,defense,cost,move,0,power)
    
    #do we want a first strike method, or does that go in the combat function?

    def __str__(self):
        return "submarine"
    
    def __repr__(self):
        return "submarine"
    

class Transport(SeaUnit):
    def __init__(self,attack=0,defense=1,cost=8,move=2,cargo=[],power=None):
        super().__init__(attack,defense,cost,move,0,power)
        self.__cargo = cargo

    def add_cargo(self,new_cargo):
        """
        takes a unit to be added to the carrier as a 
        If the unit can be added to the carrier, returns None
        If the unit cannot be added, returns the unit object
        """
        if len(self.__cargo) == 0 and new_cargo.unit_type() == "land":
            self.__cargo.append(new_cargo)
            return None
        elif len(self.__cargo) == 1 and type(new_cargo) == type(Infantry()) and type(self.__cargo[0]) == type(Infantry()):
            self.__cargo.append(new_cargo)
            return None
        else:
            return new_cargo
        
    def pop_cargo(self):
        """
        If the transport has any cargo, its unit object is returned and removed from the carrier's cargo list
        """
        if len(self.__cargo) > 0:
            return self.__cargo.pop()
        
    def get_cargo(self):
        """
        Returns the list of unit objects in this transport's cargo list
        """
        return self.__cargo

    def __str__(self):
        return "transport"
    
    def __repr__(self):
        return "transport"


class IndustrialComplex(Unit):
	def __init__(self,attack=0,defense=0,cost=15,move=0,power=None):
        super().__init__(attack,defense,cost,move,0,power)
		
	def __str__(self):
        return "industrial complex"
    
    def __repr__(self):
        return "industrial complex"

	
def main():
    boat = Carrier()
    print(boat.add_cargo(Fighter()))
    print(boat.add_cargo(Fighter()))
    print(boat.add_cargo(Fighter()))
    print(boat.add_cargo(Tank()))
    #print(boat.pop_cargo())
    
    print(boat.get_cargo())
    
    
if __name__ == "__main__":
    main()
