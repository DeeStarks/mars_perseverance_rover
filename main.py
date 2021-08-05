class MarsPlateau:
    def __init__(self, plateau_shape, no_of_rovers):
        self.plateau_shape = tuple(map(int, plateau_shape.split()))
        self.no_of_rovers = int(no_of_rovers)
        self.rover_names = [f"rover_{no+1}" for no in range(self.no_of_rovers)]
        self.__cardinal_directions = ["N", "E", "S", "W"]
        self.__rovers_info = {rover: {"x_axis": 0, "y_axis": 0, "direction": self.__cardinal_directions[0]} for rover in self.rover_names}
        self.__coord_commands = ["L", "R", "M"]

    def change_plateau_shape(self, plateau_shape):
        self.plateau_shape = tuple(map(int, plateau_shape.split()))
        return f"Changed Plateau Shape to: {self.plateau_shape}"

    def get_rover_coords(self, rover_name):
        try:
            rover = self.__rovers_info[rover_name]
        except KeyError:
            return f"Rover \"{rover_name}\" does not exist\nAvailable Rovers: {self.rover_names}"
        return "{} {} {}".format(rover["x_axis"], rover["y_axis"], rover["direction"])

    def set_rover_coords(self, rover_name, coords):
        if rover_name not in self.rover_names:
            return f"Rover \"{rover_name}\" does not exist\nAvailable Rovers: {self.rover_names}"
        try:
            x, y, direction = coords.upper().split()
            if not x.isdigit() or not y.isdigit() or direction not in self.__cardinal_directions:
                return f"Invalid coordinate. Expected: x-axis, y-axis and direction in a format like \"1 1 N\". Got: {coords}"
            self.__rovers_info[rover_name]["x_axis"] = int(x)
            self.__rovers_info[rover_name]["y_axis"] = int(y)
            self.__rovers_info[rover_name]["direction"] = direction
            return self.get_rover_coords(rover_name)
        except ValueError:
            return f"Invalid coordinate. Expected: x-axis, y-axis and direction in a format like \"1 1 N\". Got: {coords}"

    def navigate_rover(self, rover_name, commands):
        if rover_name not in self.rover_names:
            return f"Rover \"{rover_name}\" does not exist\nAvailable Rovers: {self.rover_names}"
        commands = commands.upper().split()
        for cmd in commands:
            # Check for valid commands
            if cmd not in self.__coord_commands:
                return f"Unknown command \"{cmd}\"" 
            # Change rover's coordinates
            # First, getting index of the direction at which rover is currently facing
            direction_index = self.__cardinal_directions.index(self.__rovers_info[rover_name]["direction"])
            if cmd == "L":
                # If rover is facing North and the command says to turn left, set the new direction to West
                # which is at the last index of the self.__cardinal_directions
                if direction_index == 0:
                    self.__rovers_info[rover_name]["direction"] = self.__cardinal_directions[len(self.__cardinal_directions)-1]
                else:
                    self.__rovers_info[rover_name]["direction"] = self.__cardinal_directions[direction_index-1]
            elif cmd == "R":
                # If rover is facing West and the command says to turn right, set the new direction to North
                # which is at the first index of the self.__cardinal_directions
                if direction_index == len(self.__cardinal_directions)-1:
                    self.__rovers_info[rover_name]["direction"] = self.__cardinal_directions[0]
                else:
                    self.__rovers_info[rover_name]["direction"] = self.__cardinal_directions[direction_index+1]
            elif cmd == "M":
                # If rover is facing North and the command says to move forward, 
                # set the new coordinates to the current coordinates plus the current direction
                if self.__rovers_info[rover_name]["direction"] == "N":
                    if self.__rovers_info[rover_name]["y_axis"] + 1 > self.plateau_shape[1]:
                        return f"Rover can't move out of the plateau. \"{rover_name}\" is at {self.get_rover_coords(rover_name)}"
                    self.__rovers_info[rover_name]["y_axis"] += 1
                elif self.__rovers_info[rover_name]["direction"] == "E":
                    if self.__rovers_info[rover_name]["x_axis"] + 1 > self.plateau_shape[0]:
                        return f"Rover can't move out of the plateau. \"{rover_name}\" is at {self.get_rover_coords(rover_name)}"
                    self.__rovers_info[rover_name]["x_axis"] += 1
                elif self.__rovers_info[rover_name]["direction"] == "S":
                    if self.__rovers_info[rover_name]["y_axis"] - 1 < 0:
                        return f"Rover can't move out of the plateau. \"{rover_name}\" is at {self.get_rover_coords(rover_name)}"
                    self.__rovers_info[rover_name]["y_axis"] -= 1
                elif self.__rovers_info[rover_name]["direction"] == "W":
                    if self.__rovers_info[rover_name]["x_axis"] - 1 < 0:
                        return f"Rover can't move out of the plateau. \"{rover_name}\" is at {self.get_rover_coords(rover_name)}"
                    self.__rovers_info[rover_name]["x_axis"] -= 1
        return self.get_rover_coords(rover_name)

    def __str__(self):
        return f"==============\n\nPLATEAU SHAPE: {self.plateau_shape}\nNUMBER OF ROVERS: {self.no_of_rovers}\nROVERS: {self.rover_names}\n\n=============="

# if __name__ == "__main__":
#     plateau = MarsPlateau("5 5", 5)
#     plateau.set_rover_coords("rover_1", "3 3 E")
#     print(plateau.navigate_rover("rover_1", "M M R M M R M R R M"))
#     print(plateau.get_rover_coords("rover_2"))
#     print(plateau.get_rover_coords("rover_3"))