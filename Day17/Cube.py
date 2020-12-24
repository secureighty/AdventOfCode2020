class Cube:
    def __init__(self, state, dimension_info, grid):
        '''

        :param state: is this cube on or off (boolean)
        :param dimension_info: where is this cube in dimensions 0 through n
        :return: cube object
        '''
        self.state = state
        self.dimension_info = dimension_info
        self.neighbors = None
        self.grid = grid
        if state:
            self.get_neighbors()
        self.anticipated_state = None

    def toggle(self):
        self.state = not self.state

    def get_next_cycle_state(self):
        if self.neighbors is None:
            self.get_neighbors()
        active_neighbors = 0
        for i in self.neighbors:
            neighbor = self.neighbors[i]
            if self.grid.get_cube_state(neighbor.dimension_info, False):
                active_neighbors += 1

        # ---core logic--- #
        if self.state:
            if active_neighbors == 2 or active_neighbors == 3:
                self.anticipated_state = True
                return True
            else:
                self.anticipated_state = False
                return False
        else:
            if active_neighbors == 3:
                self.anticipated_state = True
                return True
            else:
                self.anticipated_state = False
                return False
        # ----------------- #

    def __str__(self):
        result = ""
        if self.state:
            result += "On: "
        else:
            result += "Off: "
        result += str(self.dimension_info)
        return result

    def get_neighbors(self):
        self.neighbors = {}
        modifier_array = []
        for dimension in self.dimension_info:
            modifier_array.append(-1)

        # do while
        modified_array = []
        for i in range(0, len(self.dimension_info)):
            modified_array.append(modifier_array[i] + self.dimension_info[i])
        self.neighbors[str(modified_array)] = self.grid.get_cube(modified_array, self.state)
        modified_array = []

        while iterate_modifier_array(modifier_array):
            for i in range(0, len(self.dimension_info)):
                modified_array.append(modifier_array[i] + self.dimension_info[i])
            self.neighbors[str(modified_array)] = self.grid.get_cube(modified_array, self.state)
            modified_array = []

        self.neighbors.pop(str(self.dimension_info))

    def get_state(self):
        return self.state


def iterate_modifier_array(modifier_array):
    i = 0
    while i < len(modifier_array):
        if modifier_array[i] != 1:
            modifier_array[i] += 1
            return True
        else:
            modifier_array[i] = -1
            i += 1
    return False
