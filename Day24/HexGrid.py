from Day24.Tile import Tile
import math


class HexGrid:
    def __init__(self):
        self.loaded_tiles = {}

    def get_tile(self, dimension_info, load=True):
        try:
            return self.loaded_tiles[str(dimension_info)]
        except KeyError:
            new_tile = Tile(False, dimension_info, self)
            if load:
                self.loaded_tiles[str(dimension_info)] = new_tile
            return new_tile

    def get_tile_state(self, dimension_info, load=True):
        return self.get_tile(dimension_info, load).get_state()

    def cycle(self):
        list = []
        for i in self.loaded_tiles:
            tile = self.loaded_tiles[i]
            list.append(tile)

        for tile in list:
            tile.get_neighbors()

        for tile in self.loaded_tiles.values():
            tile.get_next_cycle_state()

        for i in self.loaded_tiles:
            tile = self.loaded_tiles[i]
            tile.state = tile.anticipated_state

    def get_active_tiles(self):
        result = 0
        for i in self.loaded_tiles:
            tile = self.loaded_tiles[i]
            if tile.state:
                result += 1
        return result
