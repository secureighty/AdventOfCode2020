'''
infinite grid of cubes. dynamically initialized.
i.e. we don't make every cube and set the all off, we only set cubes to on, and then their neighbors to off
class serves to store list of all on cubes
'''
from Day17.Cube import Cube


class Grid:
    def __init__(self, data, dimensions):
        '''

        :param data: string containing coordinates of starting plane on and off cubes
        :param dimensions:
        '''
        self.dimensions = dimensions
        self.loaded_cubes = {}
        self.parse(data)
        pass

    def parse(self, data):
        dim0 = 0
        for line in data.split("\n"):
            dim1 = 0
            for char in line:
                if char == "#":
                    cube_dimension_data = [dim1, dim0]
                    for i in range(2, self.dimensions):
                        cube_dimension_data.append(0)
                    self.loaded_cubes[str(cube_dimension_data)] = (Cube(True, cube_dimension_data, self))
                dim1 += 1
            dim0 += 1

    def get_cube(self, dimension_info, load=True):
        try:
            return self.loaded_cubes[str(dimension_info)]
        except:
            new_cube = Cube(False, dimension_info, self)
            if load:
                self.loaded_cubes[str(dimension_info)] = new_cube
            return new_cube

    def get_cube_state(self, dimension_info, load=True):
        return self.get_cube(dimension_info, load).get_state()

    def get_active_cube_count(self):
        count = 0
        for i in self.loaded_cubes:
            cube = self.loaded_cubes[i]
            if cube.state:
                count += 1
        return count

    def cycle(self):
        list = []
        for i in self.loaded_cubes:
            cube = self.loaded_cubes[i]
            list.append(cube)

        for cube in list:
            cube.get_neighbors()

        for i in self.loaded_cubes:
            cube = self.loaded_cubes[i]
            cube.get_next_cycle_state()

        for i in self.loaded_cubes:
            cube = self.loaded_cubes[i]
            cube.state = cube.anticipated_state

    def print_slice(self, dim_a, dim_b, dimension_info):
        '''

        :param dim_a: translates into x
        :param dim_b: translates into y
        :return: a slice on the x, y plane with the states of the cubes
        '''
        dim_b_data = []
        for i in self.loaded_cubes:
            dim_b_data.append(self.loaded_cubes[i].dimension_info[dim_b])
        y_small = min(dim_b_data)
        y_big = max(dim_b_data)
        y_size = y_big-y_small+1
        y_shift = 0
        if y_small < 0:
            y_shift = y_small * -1

        dim_a_data = []
        for i in self.loaded_cubes:
            dim_a_data.append(self.loaded_cubes[i].dimension_info[dim_a])
        x_small = min(dim_a_data)
        x_big = max(dim_a_data)
        x_size = x_big - x_small +1
        x_shift = 0
        if x_small < 0:
            x_shift = x_small * -1

        matrix = []
        # edit matrix in form matrix[y][x]
        for y in range(0, y_size):
            matrix.append([])
            for x in range(0, x_size):
                matrix[y].append(".")

        for i in self.loaded_cubes:
            cube = self.loaded_cubes[i]
            flag = True
            for dimension in range(0, len(dimension_info)):
                if dimension not in [dim_a, dim_b]:
                    if dimension_info[dimension] == cube.dimension_info[dimension]:
                        pass
                    else:
                        flag = False

            if cube.state and flag:
                matrix \
                    [cube.dimension_info[dim_b] + y_shift] \
                    [cube.dimension_info[dim_a] + x_shift] \
                    = "#"

        for y in matrix:
            string = ""
            for x in y:
                string += x
            print(string)
        print("\n")
