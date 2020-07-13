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
import Units
import Setup

def buy_units(power):
    #Will return the bought units as a list to be used later in the place units
    pass

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
    
    

if __name__ == '__main__':
    main()
