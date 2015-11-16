"""
Must be run from run_toy_robots.py or run_toy_robots.sh
"""
TABLE_LENGTH = 5  # assume square table

DIRECTIONS = {
    'NORTH': {
        'coords': (0, 1),
        'left': 'WEST',
        'right': 'EAST'},
    'SOUTH': {
        'coords': (0, -1),
        'left': 'EAST',
        'right': 'WEST'},
    'EAST': {
        'coords': (1, 0),
        'left': 'NORTH',
        'right': 'SOUTH'},
    'WEST': {
        'coords': (-1, 0),
        'left': 'SOUTH',
        'right': 'NORTH'},
    }

class ToyRobot(object):
    """
    Create robot with coordinates and directional properties to move
    within grid coordinates
    """
    def __init__(self, x=0, y=0, f='NORTH'):
        """
        :param x: robot position relative to x coord
        :param y: robot position relative to y coord
        :param f: robot facing direction
        """
        self.position = (x, y)
        self.facing = f
        self.placed = False

    def place(self, x=0, y=0, f="NORTH"):
        """
        Set robot's coordinates and facing direction. Default places robot
        on 0,0 facing North
        """
        try:
            x, y = int(x), int(y)  # check coord type validity
            self.position = (x, y)
        except (ValueError, TypeError):
            return "Invalid coordinates; you must enter a number"

        if any([coord not in range(TABLE_LENGTH) for coord in x, y]):
            return "Coordinates must be between 1 - %s" % TABLE_LENGTH

        if f.upper() not in DIRECTIONS.keys():  # check direction validity
            return "Invalid direction; use NORTH / SOUTH / EAST / WEST"
        else:
            self.facing = f.upper()
        self.placed = True

    def simulate_move(self):
        """
        Simulate the move of the robot in relation to current direction

        :return: simulated positional coordinates
        """
        position = (
            self.position[0] + DIRECTIONS[self.facing]['coords'][0],
            self.position[1] + DIRECTIONS[self.facing]['coords'][1]
        )
        return position

    def move(self):
        """
        Move robot one unit if simulated move is valid
        """
        if not self.placed:
            return "Robot must be placed first"  # must be successfully placed
        if any([coord not in range(TABLE_LENGTH) for coord in
                self.simulate_move()]):  # check that coords are in range
            return "Cannot move in this direction; robot will fall off"
        else:
            self.position = self.simulate_move()

    def right(self):
        """
        Turn robot facing direction right
        """
        if not self.placed:
            return "Robot must be placed first"  # must be successfully placed
        self.facing = DIRECTIONS[self.facing]['right']

    def left(self):
        """
        Turn robot facing direction left
        """
        if not self.placed:
            return "Robot must be placed first"  # must be successfully placed

        self.facing = DIRECTIONS[self.facing]['left']

    def report(self):
        """
        :return: readable coordinate and directional representation of object
        """
        if not self.placed:
            return "Robot must be placed first"  # must be successfully placed

        return "Output: %s,%s,%s" % (self.position[0], self.position[1],
                                     self.facing)
