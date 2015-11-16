import unittest
import toys


class TestPlace(unittest.TestCase):
    """
    Test ToyRobot place method
    """
    def testInvalidCoordType(self):
        """
        test invalid (non-int) coordinate data args
        """
        message = "Invalid coordinates; you must enter a number"
        robot = toys.ToyRobot()
        self.assertEquals(message, robot.place('a', 1, 'NORTH'))
        self.assertEquals(message, robot.place('a', 'a', 'NORTH'))
        self.assertEquals(message, robot.place(1, 'a', 'NORTH'))
        self.assertEquals(message, robot.place((1, 1), 1, 'NORTH'))
        self.assertEquals(message, robot.place(1, (1, 1), 'NORTH'))

    def testValidCoords(self):
        """
        Test coordinate int range violation
        """
        TABLE_LENGTH = 5
        message = "Coordinates must be between 1 - %s" % TABLE_LENGTH
        robot = toys.ToyRobot()
        robot.place(1, 1, 'NORTH')
        self.assertEquals((1, 1), robot.position)
        self.assertEquals(message, robot.place(5, 1, 'NORTH'))
        self.assertEquals(message, robot.place(-1, 1, 'NORTH'))

    def testDirection(self):
        """
        Test validity of direction input
        """
        message = "Invalid direction; use NORTH / SOUTH / EAST / WEST"
        robot = toys.ToyRobot()
        self.assertEqual(message, robot.place(1, 1, ''))
        self.assertEqual(message, robot.place(1, 1, 'RIGHT'))
        robot.place(1, 1, 'EAST')
        self.assertEqual('EAST', robot.facing)


class TestSimulateMove(unittest.TestCase):
    """
    Test robot move simulator
    """
    def testDirectionalMove(self):
        """
        Test robot simulated move results
        """
        robot = toys.ToyRobot()
        robot.place(0, 0, 'NORTH')
        self.assertEqual((0, 1), robot.simulate_move())
        robot.place(0, 4, 'NORTH')
        self.assertEqual((0, 5), robot.simulate_move())


class TestMove(unittest.TestCase):
    """
    Test robot move function
    """
    def testIllegalMove(self):
        """
        Test invalid move
        """
        message = "Cannot move in this direction; robot will fall off"
        robot = toys.ToyRobot()
        robot.place(0, 0, 'SOUTH')
        self.assertEqual(message, robot.move())
        robot.place(0, 0, 'EAST')
        robot.move()
        self.assertEqual((1, 0), robot.position)


if __name__ == '__main__':
    unittest.main()
