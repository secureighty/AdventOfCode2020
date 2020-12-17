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
        self.loaded_cubes = []
        self.parse(data)
        pass

    def parse(self, data):
        dim0 = 0
        dim1 = 0
        for line in data.split("\n"):
            dim1 = 0
            for char in line:
                if char == "#":
                    cube_dimension_data = [dim1, dim0]
                    for i in range(2, self.dimensions):
                        cube_dimension_data.append(0)
                    self.loaded_cubes.append(Cube(True, cube_dimension_data))
                dim1 += 1
            dim0 += 1

    def get_cube(self, dimension_info):
        for cube in self.loaded_cubes:
            for dimension in dimension_info:
                if dimension_info == cube.dimension_info:
                    return cube
        new_cube = Cube(False, dimension_info)
        self.loaded_cubes.append(new_cube)
        return new_cube

    def get_cube_state(self, dimension_info):
        return self.get_cube(dimension_info).state

    def cycle(self):
        pass

    def print_slice(self, dim_a, dim_b, dimension_info):
        '''

        :param dim_a: translates into x
        :param dim_b: translates into y
        :return: a slice on the x, y plane with the states of the cubes
        '''
        self.loaded_cubes.sort(key=lambda cube: cube.dimension_info[dim_b])
        y_small = self.loaded_cubes[0].dimension_info[dim_b]
        y_size = self.loaded_cubes[len(self.loaded_cubes)-1].dimension_info[dim_b] - y_small + 1
        y_shift = 0
        if y_small < 0:
            y_shift = y_small*-1
        self.loaded_cubes.sort(key=lambda cube: cube.dimension_info[dim_a])
        x_small = self.loaded_cubes[0].dimension_info[dim_a]
        x_size = self.loaded_cubes[len(self.loaded_cubes)-1].dimension_info[dim_a] - x_small + 1
        x_shift = 0
        if x_small < 0:
            x_shift = x_small*-1

        matrix = []
        # edit matrix in form matrix[y][x]
        for y in range(0, y_size):
            matrix.append([])
            for x in range(0, x_size):
                matrix[y].append(".")

        for cube in self.loaded_cubes:
            flag = True
            for dimension in range(0, len(dimension_info)):
                if dimension not in [dim_a, dim_b]:
                    if dimension_info[dimension] == cube.dimension_info[dimension]:
                        pass
                    else:
                        flag = False

            if cube.state and flag:
                matrix \
                    [cube.dimension_info[dim_b]+y_shift] \
                    [cube.dimension_info[dim_a]+x_shift] \
                    = "#"

        for y in matrix:
            string = ""
            for x in y:
                string += x
            print(string)



