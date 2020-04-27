import math


class Heliport:
    def __init__(self, input_filename):
        self.cases = [[1, 1.0], [2, 10.0]]

    # def read_case(self, file_handle):
    #     number_of_sides = int(file_handle.readline())
    #     return number_of_sides
    #
    # def read_file(self, input_filename):
    #     with open(input_filename) as f:
    #         self.read_case(f)
    #
    # def get_helipad_radii(self):
    #     return [1.0, 10.0]

    def print_output(self):
        for i, radius in enumerate(self.cases):
            if i > 0:
                print('')
            print(f'Case Number {i} radius is: {radius: .2f}')
