##############################################################################
#  This is code for the general game to run
#  We can use this as the skeleton to build the cohesive game
#  
#
#
##############################################################################

#Imports
import Powers
import Territorries
import Units as un
import Setup

def buy_units(power):
    UNITS = [un.Infantry(), un.Tank(), un.AntiAircraft(), un.Fighter(), un.Bomber(), un.Battleship(), un.Carrier(), un.Transport(), un.Submarine()]
    UNIT_NAMES = [str(unit) for unit in UNITS]
    
    spent_ipcs = 0
    finished = False
    bought_units = []
    
    keep_going = input("Do you want to buy any more units? (y/n): ")
    if keep_going.lower() == "n":
        finished = True
    
    while spent_ipcs <= power.IPCs() and not finished:
        buying_type = input("What type of unit would you like to buy: ")
        
        #converts buying_type from a string to a unit
        if buying_type in UNIT_NAMES:
            buying_type = UNITS[UNIT_NAMES.index(buying_type)]
        else:
            print("That is not a valid unit name")
            continue
        
        
        buying_num = input("How many would you like to buy: ")
        try:
            buying_num = int(buying_num)
            total_cost = buying_num * buying_type.get_cost()
            if total_cost <= power.IPCs() and buying_num > 0:
                spent_ipcs += total_cost
                power.spend_IPCs(total_cost)
                bought_units = bought_units + [buying_type for x in range(buying_num)]
            else:
                raise ValueError
        except ValueError:
            print("That is not a number of units that you can buy")
            continue

    return bought_units #Will return the bought units as a list to be used later in the place units

def declare_attacks(power):
    '''
    declare attacks can handle whether attacks are legal as well as do the
    edge cases like strategic bombings, bltizes, amphibious assaults, etc. and 
    then it will call the combat function as many times as it needs
    '''
    #in amphibious assaults, send an extra int parameter to do_combat for the number of bombard hits from the battleships (it defaults to 0)
    #combat(power, defender, units, territory)
    
def noncombat_move(power):
    
    pass

def place_units(power, units):
    #Uses the list created in the buy_units function
    pass

def collect_IPCs(power):
    pass

def take_turn(power):
    bought_units = buy_units(power)
    declare_attacks(power)
    noncombat_move(power)
    place_units(power, bought_units)
    power.collect_IPCs()

def check_win():
    #Returns a boolean to check if a side has won
    #True if so, False if not
    pass

def main():
    #We can have the setup function return the 5 powers as a list
    powers = Setup.setup()
    
    win = False
    while not win:
        for power in powers:
            take_turn(power)
        if check_win():
            break
    
    """
    #Test case
    Russia = Powers.Power("Allies", [], 24, "USSR")
    print(buy_units(Russia))
    print("remaining IPCs: " + str(Russia.IPCs()))
    """
    
    

if __name__ == '__main__':
    main()
