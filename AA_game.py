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
    pass

def declare_attacks(power):
    '''
    declare attacks can handle whether attacks are legal as well as do the
    edge cases like strategic bombings, bltizes, amphibious assaults, etc. and 
    then it will call the combat function as many times as it needs
    '''
    
    #combat(power, defender, units, territory)
    
def noncombat_move(power):
    pass

def place_units(power):
    pass

def collect_IPCs(power):

def take_turn(power):
    buy_units(power)
    declare_attacks(power)
    noncombat_move(power)
    place_units(power)
    collect_IPCs(power)

def main():
    #We can have the setup function return the 5 powers as a list
    powers = Setup.setup()
    
    win = False
    while not win:
        for power in powers:
            take_turn(power)
    
    

if __name__ == '__main__':
    main()