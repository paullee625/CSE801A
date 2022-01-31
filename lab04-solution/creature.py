# It is safe to change the code in this cell -- in fact you should!


class Creature:
    
    def __init__(self, init_score, world_size, start_location, init_facing='N'):
        """
        Initialize a creature.
        
        Args:
            self: This object
            init_score: A number that gives the creature an initial score.
                        A creature is only "alive" if it has a score greater than zero.
            world_size: A tuple or list that gives the creature information about the size 
                        of the world.
                        The first entry in the pair should refer to the horizontal (x) dimension 
                        of the world.
                        The second entry in the pair should refer to the vertical (y) dimension 
                        of the world.
                        NOTE: The world's "origin" (0,0) coordinate is in the upper-left corner.
            start_location: A tuple or list that gives the creature an initial location within 
                            the world.
                            Its value for each pair of coordinates should be 0 <= position < world_dim,
                            where position and world dim refer to either the horizontal (x) or vertical (y)
                            dimension of the world.
            init_facing: An initial facing.
                         Facing is one of four values: N, E, S, W representing one of the four cardinal
                         direction: (N)orth, (S)outh, (E)ast, or (W)est.  Here, North points upward on 
                         the display; South downward; West to the left; and East to the right.
        """
        self.score = init_score  # Creatures are online "alive" if their score is > 0
        self.world_size = world_size # How big is our world (width, height)
        self.current_location = start_location # (x,y) position of creature
        self.facing = init_facing # N,E,S,W direction the creature is facing
        self.initial = [init_score, start_location, init_facing] # Backup for resetting
        
    def reset(self):
        """
        Resets the creature to initial conditions.
        
        Args:
            self: This object
            
        Returns:
            None, but the creature is updated to initial conditons
        """
        self.score = self.initial[0]
        self.current_location = self.initial[1]
        self.facing = self.initial[2]

        
    def is_alive(self):
        """
        Checks to see if the creature is alive.  A creature is only alive if its score 
        is greater than zero.
        
        Args:
            self: This object
            
        Returns:
            a Boolean value True or False if the creature is alive.
        """
        return self.score > 0
    
    
    def kill(self):
        """
        Kill the creature.
        
        Args:
            self: This object
            
        Returns:
            None, but will set the creature's score to 0 to kill it.
        """
        self.score = 0
    
    
    
    def rotate_left(self):
        """
        Rotates the creature's facing 90 degrees to the left.  
        If a creature is facing north and it rotates
        90 degrees to the left four times, the sequence of facings 
        would be: N -> W -> S -> E -> N
        
        Args:
            self: This object
            
        Returns:
            None, but the creature is rotated.
        """
        if self.facing == 'N':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'S'
        elif self.facing == 'S':
            self.facing = 'E'
        elif self.facing == 'E':
            self.facing = 'N'
        else:
            raise Exception(f'Unknown facing {self.facing}')
    
    
    def rotate_right(self):
        """
        Rotates the creature's facing 90 degrees to the right.  If a creature is 
        facing north and it rotates 90 degrees to the right four times, 
        the sequence of facings would be: N -> E -> S -> W -> N
        
        Args:
            self: This object
            
        Returns:
            None, but the creature is rotated.
        """
        if self.facing == 'N':
            self.facing = 'E'
        elif self.facing == 'E':
            self.facing = 'S'
        elif self.facing == 'S':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'N'
        else:
            raise Exception(f'Unknown facing {self.facing}')
    
    
    
    def move_forward(self):
        """
        Changes the creature's current_location to move one unit in the direction 
        the creature is facing. So, if a creature is facing North, it will move one 
        unit *up*.  Since the origin (0,0) cell of the world is in the upper-left corner, 
        this would mean the creature's location in the y-dimension is decreased by one unit.
        
        NOTES:
            * The origin is in the upper-left corner.  That means movement up and left 
              decreases the value of the location coordinates; moving down or right 
              increases them.
              
            * The world is finite sized.  This means the creature *CANNOT* have a negative 
              coordinate or a value greater-than or equal-to the world_size for any particular 
              dimension.  For exmaple, if the world size is (5,5), the creature can never have 
              a current_location (5,2) or (2,5) because those would both be outside the 
              dimensions of the world.  (The highest value in any dimension in a 5x5 world  
              would be 4.)
              
            * If a creature cannot move (e.g. it's at the edge of the world), then the creature 
              will stay where it is presently located.
              
            * YOU WILL HAVE TO ENSURE THAT THE CREATURE DOES NOT MOVE INTO AN INVALID 
              COORDINATE AS DESCRIBED ABOVE.  The game will kill it otherwise.  Or crash.
        
        Args:
            self: This object
            
        Returns:
            None, but the creature tries to move.
        """
        cur_x, cur_y = self.current_location 
        new_x, new_y = cur_x, cur_y
        max_x, max_y = self.world_size
        if self.facing == 'N':
            if cur_y > 0:
                new_y = cur_y - 1
        elif self.facing == 'S':
            if cur_y < max_y - 1:
                new_y = cur_y + 1
        elif self.facing == 'W':
            if cur_x > 0:
                new_x = cur_x - 1
        elif self.facing == 'E':
            if cur_x < max_x - 1:
                new_x = cur_x + 1
        else:
            raise Exception(f'Unknown facing {self.facing}')
        self.current_location = (new_x, new_y)