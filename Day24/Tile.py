import math


class Tile:
    def __init__(self, state, dimension_info, grid):
        self.state = state
        self.dimension_info = dimension_info
        self.grid = grid
        self.neighbors = None
        if state:
            self.get_neighbors()
        self.anticipated_state = None

    def toggle(self):
        self.state = not self.state

    def get_state(self):
        return self.state

    def __str__(self):
        result = ""
        if self.state:
            result += "On: "
        else:
            result += "Off: "
        result += str(self.dimension_info)
        return result

    def get_next_cycle_state(self):
        if self.neighbors is None:
            self.get_neighbors()
        active_neighbors = 0
        for neighbor in self.neighbors.values():
            if self.grid.get_tile_state(neighbor.dimension_info, False):
                active_neighbors += 1

        # ---core logic--- #
        if self.state:
            if active_neighbors > 2 or active_neighbors == 0:
                self.anticipated_state = False
                return False
            else:
                self.anticipated_state = True
                return True
        else:
            if active_neighbors == 2:
                self.anticipated_state = True
                return True
            else:
                self.anticipated_state = False
                return False
        # ----------------- #

    def get_neighbors(self):
            e = [round(self.dimension_info[0], 1),
                 round(self.dimension_info[1] + 100, 1)]
            ne = [round(self.dimension_info[0] + 100 * math.sqrt(3), 1),
                  round(self.dimension_info[1] + 50, 1)]
            se = [round(self.dimension_info[0] - 100 * math.sqrt(3), 1),
                  round(self.dimension_info[1] + 50, 1)]
            w = [round(self.dimension_info[0], 1),
                 round(self.dimension_info[1] - 100, 1)]
            nw = [round(self.dimension_info[0] + 100 * math.sqrt(3), 1),
                  round(self.dimension_info[1] - 50, 1)]
            sw = [round(self.dimension_info[0] - 100 * math.sqrt(3), 1),
                  round(self.dimension_info[1] - 50, 1)]
            prelist = [e, ne, se, w, nw, sw]
            for i in prelist:
                for j in range(0, 2):
                    if i[j] == 0:
                        i[j] = 0.0

            self.neighbors = {str(e): self.grid.get_tile(e, self.state),
                              str(ne): self.grid.get_tile(ne, self.state),
                              str(se): self.grid.get_tile(se, self.state),
                              str(w): self.grid.get_tile(w, self.state),
                              str(nw): self.grid.get_tile(nw, self.state),
                              str(sw): self.grid.get_tile(sw, self.state)}
