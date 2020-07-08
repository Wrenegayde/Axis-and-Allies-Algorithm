import Units as un

def get_num_hits(unit_list, is_attacker):
    """
    Takes a list of units to roll for and a boolean (True for attacker, False for defender)
    Returns the number of hits that the units score
    """
    total_hits = 0
    for unit in unit_list:
        if is_attacker and unit.attack_hits():
            total_hits += 1
        elif not is_attacker and unit.defense_hits():
            total_hits += 1
        return total_hits

def take_casualties(unit_list, num_dead):
    """
    Takes the list of units that casualties are being chosen from and the number of casualties
    Prompts for console input to get the type and number of units to remove
    Loops until enough units have been removed from the unit_list or all units are dead
    Returns (casualty list, remaining unit list) as a tuple
    """
    if num_dead >= len(unit_list):
        return unit_list,[]
    
    casualty_list = []
    while num_dead > len(casualty_list) and len(unit_list) > 0:
        print("You have to remove " + str(num_dead) + " units.")
        print("You have " + str(unit_list))
        unit_to_remove = input("What type of unit do you want to remove: ").lower()
        how_many_to_remove = int(input("How many do you want to remove: "))
        
        num_of_removing_type = 0
        remove_locations = []
        for index,unit in enumerate(unit_list):
            if str(unit) == unit_to_remove:
                num_of_removing_type += 1
                remove_locations.append(index)
        		
        if num_of_removing_type > 0:
            if how_many_to_remove <= (num_dead - len(casualty_list)) and how_many_to_remove > 0 and how_many_to_remove <= num_of_removing_type:
                num_removed = 0
                for index in remove_locations:
                    casualty_list.append(unit_list[index - num_removed])
                    unit_list = unit_list[:index - num_removed] + unit_list[index - num_removed + 1:]
                    num_removed += 1
            else:
                print("That is not a valid number to remove")	
        else:
            print("That unit type name is invalid")
        
    return casualty_list, unit_list


def do_combat(attacker_units, defender_units, attacker_power, defender_power):
    keep_going_str = input("attacker, do you want to keep attacking? (y/n): ")
    keep_going = True
    	
    for index,unit in enumerate(defender_units):
        if str(unit) == "antiaircraft":
            num_air_attackers = 0
            for unit in attacker_units:
                if unit.unit_type() == "air":
                    num_air_attackers += 1
                    num_air_hits = defender_units[defender_units.index(un.AntiAircraft())].aagun_hits()
                			#remove casualties
                			#remove AAgun
    	
    while keep_going:
    		
        atk_hits = get_num_hits(attacker_units, True)
        casualty_zone,defender_units = take_casualties(defender_units, atk_hits, False)
        def_hits = get_num_hits(defender_units + casualty_zone, False)
        		
        temp_list,attacker_units = take_casualties(attacker_units, def_hits, True)
        		
        temp_list = []
        casualty_zone = []

