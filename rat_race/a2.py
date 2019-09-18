# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        A Rat with symbol. row and column.
        
        >>> rat = Rat('J', 1, 1)
        >>> rat.symbol
        'J'
        >>> rat.row
        1
        >>> rat.col
        1
        """
        
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Chanhe Rat row and col.
        
        >>> rat = Rat('J', 1, 1)
        >>> rat.set_location(2, 3)
        >>> rat.row
        2
        >>> rat.col
        3
        """
        
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Increase num_sprouts_eaten by one.
        
        >>> rat = Rat('J', 1, 1)
        >>> rat.num_sprouts_eaten
        0
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.
        
        >>> rat = Rat('J', 1, 1)
        >>> rat.__str__()
        J at (4,3) ate 0 sprouts.
        """
        
        return "{0} at ({1},{2}) ate {3} sprouts".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)
        
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

if __name__ == "__main__":
    rat = Rat('J', 1, 1)
    print(rat.symbol)
    print(rat.row)
    print(rat.col)
