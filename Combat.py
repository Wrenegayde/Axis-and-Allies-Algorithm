import Units as un

def get_num_hits(unit_list, is_attacker):
    """
    Takes a list of units to roll for and a boolean (True for attacker, False for defender)
    Returns a tuple (all other hits, submarine hits)
    """
    total_hits = 0
    sub_hits = 0
    for unit in unit_list:
        if str(unit) != "submarine":
            if is_attacker and unit.attack_hits():
                total_hits += 1
            elif not is_attacker and unit.defense_hits():
                total_hits += 1
        else:
            if is_attacker and unit.attack_hits():
                sub_hits += 1
            elif not is_attacker and unit.defense_hits():
                sub_hits += 1
    return total_hits,sub_hits

def take_casualties(unit_list, num_dead, terrains=["sea","land","air"], power):
    """
    Takes the list of units that casualties are being chosen from and the number of casualties
    Prompts for console input to get the type and number of units to remove
    Loops until enough units have been removed from the unit_list or all units are dead
    Returns (casualty list, remaining unit list) as a tuple
    """
    casualty_list = []
     #If there are no units that can be validly removed, then return.
    #e.g. submarine shoots at planes
    terrains_in_unit_list = set([unit.unit_type() for unit in unit_list])
    unit_list_has_valid_terrains = False
    unit_list_has_only_valid_terrains = True
    for terrain in terrains:
        if terrain in terrains_in_unit_list:
            unit_list_has_valid_terrains = True
        else:
            unit_list_has_only_valid_terrains = False
    if not unit_list_has_valid_terrains:
        return casualty_list, unit_list
    
    #If there are more casualties than remaining units, then they all die
    if num_dead >= len(unit_list) and unit_list_has_only_valid_terrains:
        return unit_list,[]
    
    if power.player():
        while num_dead > len(casualty_list) and len(unit_list) > 0:
            print("You have to remove " + str(num_dead) + " units total.")
            print("You have " + str(unit_list))
            #Ask which unit type to remove and how many
            unit_to_remove = input("What type of unit do you want to remove: ").lower()
            how_many_to_remove = int(input("How many do you want to remove: "))
            
            num_of_removing_type = 0
            remove_locations = []

            #Find all of the units that we want to remove
            for index,unit in enumerate(unit_list):
                if str(unit) == str(unit_to_remove):
                    unit_to_remove = unit
                    num_of_removing_type += 1
                    remove_locations.append(index)
                    
            #Remove all of the ones that we found up until we have removed the number that we wanted to
            if num_of_removing_type > 0 :
                if unit_to_remove.unit_type() in terrains:
                    if how_many_to_remove <= (num_dead - len(casualty_list)) and how_many_to_remove > 0 and how_many_to_remove <= num_of_removing_type:
                        num_removed = 0
                        for index in remove_locations:
                            if num_removed < how_many_to_remove:
                                casualty_list.append(unit_list[index - num_removed])
                                unit_list = unit_list[:index - num_removed] + unit_list[index - num_removed + 1:]
                                num_removed += 1
                    else:
                        print("That is not a valid number to remove")	
                else:
                    print("That unit type name is invalid. Remember that it must be from " + str(terrains))
    else:
        while num_dead > len(casualty_list) and len(unit_list) > 0:
            #Ask which unit type to remove and how many
            unit_to_remove = #COM CODE
            how_many_to_remove = #COM CODE
            
            num_of_removing_type = 0
            remove_locations = []

            #Find all of the units that we want to remove
            for index,unit in enumerate(unit_list):
                if str(unit) == str(unit_to_remove):
                    unit_to_remove = unit
                    num_of_removing_type += 1
                    remove_locations.append(index)
                    
            #Remove all of the ones that we found up until we have removed the number that we wanted to
            if num_of_removing_type > 0 :
                if unit_to_remove.unit_type() in terrains:
                    if how_many_to_remove <= (num_dead - len(casualty_list)) and how_many_to_remove > 0 and how_many_to_remove <= num_of_removing_type:
                        num_removed = 0
                        for index in remove_locations:
                            if num_removed < how_many_to_remove:
                                casualty_list.append(unit_list[index - num_removed])
                                unit_list = unit_list[:index - num_removed] + unit_list[index - num_removed + 1:]
                                num_removed += 1
        
    return casualty_list, unit_list


def check_win(attacker_units, defender_units, attacker_power, defender_power):
    if len(attacker_units) == 0:
        return defender_power
    elif len(defender_units) == 0:
        return attacker_power
    else:
        return None


def do_combat(attacker_units, defender_units, attacker_power, defender_power,battleship_hits=0, defending_territory):
    """
    takes four parameters 
        list of attacker units, list of defender units, attacker power, defender power
    returns the list of units remaining in the territory, the power that won
    """
    #Handle amphibious battleship hits 
    temp_list, attacker_units = take_casualties(attacker_units, battleship_hits, attacker_power)
    
    aagun_exists = False
    
    #Handle AAgun first strikes
    for index,def_unit in enumerate(defender_units):
        if str(def_unit) == "antiaircraft":
            aagun_exists = True
            num_air_attackers = 0
            for atk_unit in attacker_units:
                if atk_unit.unit_type() == "air":
                    num_air_attackers += 1
            num_air_hits = def_unit.aagun_hits(num_air_attackers)
                	
            temp_list,attacker_units = take_casualties(attacker_units, num_air_hits,terrains=["air"], attacker_power)
            
            defender_units = defender_units[:index] + defender_units[index+1:]
    
    winning_power = check_win(attacker_units, defender_units, attacker_power, defender_power)
	
    while winning_power == None:
        print("Attacker has: " + str(attacker_units))
        print("Defender has: " + str(defender_units))
    		
        atk_hits, atk_sub_hits = get_num_hits(attacker_units, True)
        print("Attacker hits: " + str(atk_hits + atk_sub_hits))
        
        temp_list, defender_units = take_casualties(defender_units, atk_sub_hits, terrains=["sea"], defender_power)
        casualty_zone, defender_units = take_casualties(defender_units, atk_hits, defender_power)
        
        def_hits, def_sub_hits = get_num_hits(defender_units + casualty_zone, False)
        print("Defender hits: " + str(def_hits + def_sub_hits))		
        
        temp_list, attacker_units = take_casualties(attacker_units, def_hits, attacker_power)
        temp_list, attacker_units = take_casualties(attacker_units, def_sub_hits, terrains=["sea"], attacker_power)		
        
        temp_list = []
        casualty_zone = []
        
        winning_power = check_win(attacker_units, defender_units, attacker_power, defender_power)
       
        if winning_power == None:
            if attacker_power.player():
                option = input(str(attacker_power) + ", do you want to keep attacking? (y/n): ").lower()
                while option != 'y' and option != 'n':
                    option = input(str(attacker_power) + ", do you want to keep attacking? (y/n): ").lower()

                if option == "n":
                    winning_power = defender_power

                else:
                    isValid = False
                    while not isValid:
                         option = input('Which territory would you like to retreat to, ' + str(attacker_power).lower() + '?')
                         for terr in defending_territory.adj_territories():
                            if str(terr) == option and terr.nation().team() == attacker_power().team():
                                for unit in attacker_units:
                                    retreat(unit, terr)
                                isValid = True
                                break
                    winning_power = defending_power
                    
            else:
                option = #COM CODE

                if option == "n":
                    winning_power = defender_power

                else:
                    isValid = False
                    while not isValid:
                        option = input('Which territory would you like to retreat to, ' + str(attacker_power).lower() + '?')
                        for terr in defending_territory.adj_territories():
                            if str(terr) == option and terr.nation().team() == attacker_power().team():
                                for unit in attacker_units:
                                    retreat(unit, terr)
                                isValid = True
                                break
                    winning_power = defending_power

    
    aagun_list = []          
    if aagun_exists:
        aagun_list = [un.AntiAircraft(power=winning_power)]
                
    if winning_power == defender_power:
        return defender_units + aagun_list, defender_power
    else:
        defending_territory.capture_territory(attacker_power)
        return attacker_units + aagun_list, attacker_power
             
        

#print(do_combat([un.Submarine() for x in range(10)], [un.Fighter()], "germany", "uk"))
