

class Cube:
    def __init__(self, state, dimension_info):
        '''

        :param state: is this cube on or off (boolean)
        :param dimension_info: where is this cube in dimensions 0 through n
        :return: cube object
        '''
        self.state = state
        self.dimension_info = dimension_info

    def toggle(self):
        self.state = not self.state

    def __str__(self):
        result = ""
        if self.state:
            result += "On: "
        else:
            result += "Off: "
        result += str(self.dimension_info)
        return result
