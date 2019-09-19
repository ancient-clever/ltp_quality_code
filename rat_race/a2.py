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

        Change Rat row and col.
        
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
        
        return "{0} at ({1}, {2}) ate {3} sprouts.".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)
        
class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        A Maze with rat_1 and rat_2.
        
        >>> maze = Maze(
        [['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']],
        Rat('J', 1, 1),
        Rat('P', 1, 4))
        >>> maze.rat_1
        J at (1, 2) ate 0 sprouts.
        >>> maze.rat_2
        P at (1, 4) ate 0 sprouts.
        """
        
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        
        num_sprouts_left = 0 
        for i in range(len(maze)):
            num_sprouts_left += maze[i].count(SPROUT)

        self.num_sprouts_left = num_sprouts_left

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the given
        row and column of the maze.
        """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> int
        Return the character in the maze at the given row and column.
        """
        if (self.rat_1.row, self.rat_1.col) == (row, col):
            return self.rat_1.symbol
        if (self.rat_2.row, self.rat_2.col) == (row, col):
            return self.rat_2.symbol

        return self.maze[row][col]
        
        return self.maze[row][col]

    def move(self, rat, row_move, col_move):
        """ (Maze, Rat, int, int) -> NoneType

        Move the rat in the given direction, unless there is a wall in the way.
        Return True if and only if there wasn't a wall in the way.
        """

        old_row = rat.row
        old_col = rat.col

        new_row = old_row + row_move
        new_col = old_col + col_move

        target = self.get_character(new_row, new_col)

        if target == WALL:
            return False
        if target == HALL:
            rat.set_location(new_row, new_col) 
        elif target == SPROUT:
            rat.set_location(new_row, new_col) 
            rat.eat_sprout()                   
            self.num_sprouts_left -= 1         
            self.maze[new_row][new_col] = HALL 
        return True
    

    def __str__(self):
        """ (Maze) -> str
        Return a string representation of the Maze
        """
        s = ''
        
        m = self.maze
        m[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        m[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        for i in range(len(m)):
            for j in range(len(m[i])):
                s = s + m[i][j]
            s = s + '\n'

        s = s + str(self.rat_1) + '\n' + str(self.rat_2)
        return s

