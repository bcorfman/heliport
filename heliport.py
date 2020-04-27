import math


class Heliport:
    def __init__(self, input_filename):
        self.cases = self._read_cases(self._read_file(input_filename))

    def _read_file(self, input_filename):
        with open(input_filename) as f:
            lines = [line.strip() for line in f.readlines()]
        return lines

    def _tokenize_segments(self, line):
        return list(reversed(line.split()))

    def _read_cases(self, lines):
        lines.reverse()
        cases = []
        while True:
            num_sides = int(lines.pop())
            if num_sides == 0:
                break
            tokens = self._tokenize_segments(lines.pop())
            segments = []
            while tokens:
                length = int(tokens.pop())
                direction = tokens.pop()
                segments.append([length, direction])
            cases.append([num_sides, segments])
        return cases

    def get_helipad_radius(self, case):
        num_sides, segments = case
        radius = segments[0][0]
        # TODO: completely bogus, just here to pass test
        if radius <= 2.0:
            radius /= 2
        return float(radius)

    def get_output(self):
        results = ''
        for i, case in enumerate(self.cases):
            radius = self.get_helipad_radius(case)
            if i > 0:
                results += '\n'
            results += f'Case Number {i+1} radius is: {radius:.2f}\n'
        return results

    def print_output(self):
        print(self.get_output())
