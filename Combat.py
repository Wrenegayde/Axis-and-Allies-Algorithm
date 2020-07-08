import Units

def get_num_hits(unit_list, is_attacker):
	total_hits = 0
	for unit in unit_list:
		if is_attacker and unit.attack_hits():
			total_hits += 1
		elif not is_attacker and unit.defense_hits():
			total_hits += 1
	return total_hits

def take casualties():
	pass

def do_combat(attacker_list, defender_list):
	pass
