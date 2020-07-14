import Territories
import Units as un

def find_path(start_terr, end_terr, this_path=[], shortest_path=[]):
    """
    Takes the start territory and end territory of the path you want
    Uses weird recursion and has not been tested! Test thoroughly as soon as setup is done!
    Returns the shortest path between them backwards, probably most useful for its length
    """
    if len(this_path) > len(shortest_path) and len(shortest_path) != 0:
        return shortest_path
    else:
        
        this_path.append(end_terr)

        if start_terr in end_terr.adj_territories():
            this_path.append(start_terr)
            if len(this_path) < len(shortest_path) or len(shortest_path) == 0:
                return this_path
            else:
                return shortest_path

        valid_paths = []
        for terr in end_terr.adj_territories():
            #This if statement prevents backtracking
            if not terr in this_path and (len(this_path) < len(shortest_path) or len(shortest_path) == 0):
                #recursive call
                next_path = find_path(start_terr, terr, this_path, shortest_path)
                if len(next_path) < len(shortest_path) or len(shortest_path) == 0:
                    shortest_path = next_path
                valid_paths.append(next_path)
        
        for path in valid_paths:
            if len(path) < len(shortest_path) or len(shortest_path) == 0:
                return path
        
        return shortest_path
             

def main():
    terr1 = Territories.Territory("US", [], [], "terr1")
    terr2 = Territories.Territory("US", [terr1], [], "terr2")
    terr3 = Territories.Territory("US", [terr2, terr1], [], "terr3")
    terr4 = Territories.Territory("US", [terr2, terr3], [], "terr4") 
    

    print(find_path(terr1, terr4))

if __name__ == "__main__":
    main()
