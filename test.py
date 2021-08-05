import unittest
import main

class TestRoverNavigation(unittest.TestCase):
    def test_navigation(self):
        plateau = main.MarsPlateau(1)
        shape = input("Enter the shape of the plateau (e.g. '5 5'): ")
        coords = input("Enter the coordinates of the rover (e.g. '1 2 N'): ")
        commands = input("Enter the commands to navigate the rover (e.g. 'L M L M L M L M M'): ")
        output = input("Enter the expected output (e.g. '1 3 N'): ")
        
        plateau.set_plateau_shape(shape)
        plateau.set_rover_coords("rover_1", coords)
        result = plateau.navigate_rover("rover_1", commands)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()