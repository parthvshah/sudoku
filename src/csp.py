def some(seq):
    # Return some element of seq that is true.
    for e in seq:
        if e: return e
    return False

def make_grid_keys(rows, columns):
    # returns cartesian product of rows and columns list
    return [row+column for row in rows for column in columns]

class readTestcase():
    def __init__(self, testcase):
        self.testcase = testcase
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.columns = self.digits
        self.squares = make_grid_keys(self.rows, self.columns)
        self.unitlist = ([make_grid_keys(self.rows, c) for c in self.columns] +
                         [make_grid_keys(r, self.columns) for r in self.rows] +
                         [make_grid_keys(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        # sets units of all squares in the grid
        self.units = dict((s, [u for u in self.unitlist if s in u])
                          for s in self.squares)
        # sets peers of all squares in the grid
        self.peers = dict(
            (s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)

    def grid_values(self):
        # assigns grid values to characters based on the testcase
        characters = [
            c for c in self.testcase if c in self.digits or c in '0.']
        assert len(characters) == 81
        return dict(zip(self.squares, characters))

    def solve_grid(self):
        # solves the grid by assigning values to the squares and propogating the elmination of values in its peers
        values = dict((s, self.digits) for s in self.squares)
        for s, d in self.grid_values().items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def assign(self, values, s, d):
        # assigns a value to a square by elminiation of other values in the square
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        # elminates the other_values in the square, and propogates elimination of the correct value in its peers.
        if d not in values[s]:
            return values 
        values[s] = values[s].replace(d, '')
        # If a square s is reduced to one value d2, then eliminate d2 from the peers.
        if len(values[s]) == 0:
            # Contradiction: removed last value
            return False  
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        # If a unit u is reduced to only one place for a value d, then put it there.
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                # Contradiction: no place for this value
                return False  
            elif len(dplaces) == 1:
                # d can only be in one place in unit; assign it there
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def search(self, values):
        # Using depth-first search and propagation, try all possible values.
        if values is False:
            ## Failed earlier
            return False 
        if all(len(values[s]) == 1 for s in self.squares): 
            ## Solved!
            return values 
        ## Chose the unfilled square s with the fewest possibilities
        n,s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return some(self.search(self.assign(values.copy(), s, d)) 
            for d in values[s])

    def display(self):
        # Display these values as a 2-D grid.
        values = self.search(self.solve_grid())
        width = 1+max(len(values[s]) for s in self.squares)
        line = '+'.join(['-'*(width*3)]*3)
        for r in self.rows:
            for c in self.columns:
                print(''.join(values[r+c].center(width)), end='')
                if c in '36':
                    print('|', end='')
            print()
            if r in 'CF':
                print(line)
        print()

def main(testcase):
    # testcase = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    solve_1 = readTestcase(testcase)
    # solve_1.display()