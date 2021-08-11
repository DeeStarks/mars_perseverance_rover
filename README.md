# MARS PERSEVERANCE ROVER
This is a simple program that helps the perseverance rover to navigate the surface of Mars.

## PROBLEM STATEMENT
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. A rover’s position and location is represented by a combination of x and y co- ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation.

An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same Heading. Assume that the square directly North from (x, y) is (x, y+1).

### Input Description:
The first line of input is the upper-right coordinates of the plateau, the lower- left coordinates are assumed to be 0,0. The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the rover’s orientation. Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.

### Output Description:
The output for each rover should be its final coordinates and heading.


### Sample Input 1:
```
5 5
1 2 N 
L M L M L M L M M
```

### Sample Output 1:
```
1 3 N
```

### Sample Input 2:
```
5 5
3 3 E 
M M R M M R M R R M
```

### Sample Output 2:
```
5 1 E
```


## HOW IT WORKS
The program is implemented in an object oriented way in a class named `MarsPlateau`. `MarsPlateau` takes only 1 parameter - the number of rovers.

### Available methods:
* `set_plateau_shape` 
    - changes the shape/size of the plateau. It takes in 1 parameter - `plateau_shape`(in format `"5 5"`).
* `get_plateau_shape` 
    - returns shape of plateau.
* `set_rover_coords` 
    - changes the position of rover. It takes in 2 parameters - `rover_name` and `coords`(in format - `"1 2 N"`).
* `get_rover_coords` 
    - returns the rover's current position.
* `navigate_rover` 
    - which takes 2 parameters - `rover_name` and `commands`(in format `"L M L M L M L M M"`). It traverses the rover whose name was passed to the `rover_name` parameter, to the next point based on the command in the `commands` parameter. Accepted commands are - `"L"`, `"R"` and `"M"`.

### Example:
```python
# Initialize MarsPlateau with number of rovers, passed as a parameter. 
plateau = MarsPlateau(5)

# Change the shape of the plateau to 5x5 (referring to the upper-right coordinates of the plateau)
plateau.set_plateau_shape("5 5")

# Set a rover's position to 1,2 and facing North.
plateau.set_rover_coords("rover_1", "1 2 N") 

# Move a rover to the next point based on the commands and return the final position and heading.
plateau.navigate_rover("rover_1", "L M L M L M L M M") 

# Return a rover's current position.
plateau.get_rover_coords("rover_1")

# Return the plateau's shape.
plateau.get_plateau_shape() 
```


## USAGE
- Run `./script.sh` to run the program.
- Run `./script.sh test` to run the program with test cases.