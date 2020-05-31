from math import hypot
from datatypes import Circle, Point, Rect, CandidateEdges, Roof, RoofSegment

# My solution to Problem B (Heliport) from 2004 ACM Programming Contest World Finals.
# Problem set is found at: https://icpc.baylor.edu/download/worldfinals/problems/2004WorldFinalProblemSet.pdf


def find_helipad_radius(edges: CandidateEdges, roof: Roof) -> float:
    # If polygon is defined in counterclockwise direction, then if we are moving right at the start,
    # the first time we move up (Y) is when we start measuring the min X value. That is the largest
    # possible X value for the right side. Once this is done for all four sides, take the difference
    # between Xs and Ys, figure out which is greater and divide by 2 to get the radius.
    largest_radius = -99.0
    outline_points = roof.upper_right_points + roof.bottom_left_points
    for left in edges.left:
        for right in edges.right:
            for top in edges.top:
                for bottom in edges.bottom:
                    possible_location = Rect(left, top, right, bottom)
                    helipad_center = Point(left + (right - left) / 2, bottom + (top - bottom) / 2)
                    radius = find_largest_radius_inside(possible_location)
                    possible_helipad = Circle(helipad_center, radius)
                    points_inside = [point_in_circle(pt, possible_helipad) for pt in outline_points]
                    if not any(points_inside) and radius > largest_radius:
                        largest_radius = radius
    return largest_radius


def roof_outline(line: str) -> Roof:
    roof = Roof()
    segments = roof.upper_right_segments
    points = roof.upper_right_points
    second_stage = False
    tokens = line.split()
    pairs = zip(tokens[::2], tokens[1::2])
    loc = Point(0, 0)
    for units, direction in pairs:
        if direction == 'D' and not second_stage:
            second_stage = True
            last_added = segments.pop()
            segments = roof.bottom_left_segments
            segments.append(last_added)
            last_point = points.pop()
            points = roof.bottom_left_points
            points.append(last_point)
        units = int(units)
        seg = RoofSegment(units, direction)
        segments.append(seg)
        loc = update_location(loc, seg)
        points.append(loc)
    return roof


def candidate_edges(roof: Roof) -> CandidateEdges:
    top_edges, bottom_edges, left_edges, right_edges = set(), set(), set(), set()
    for i, segment in enumerate(roof.upper_right_segments):
        if segment.direction == 'U':
            top_edges.add(roof.upper_right_points[i].y)
        elif segment.direction == 'L' or segment.direction == 'R':
            right_edges.add(roof.upper_right_points[i].x)

    for i, segment in enumerate(roof.bottom_left_segments):
        if segment.direction == 'D':
            bottom_edges.add(roof.bottom_left_points[i].y)
        elif segment.direction == 'L' or segment.direction == 'R':
            left_edges.add(roof.bottom_left_points[i].x)
    return CandidateEdges(sorted(list(top_edges)), sorted(list(bottom_edges)),
                          sorted(list(left_edges)),  sorted(list(right_edges)))


def update_location(old_loc: Point, seg: RoofSegment) -> Point:
    loc = Point(old_loc.x, old_loc.y)
    if seg.direction == 'U':
        loc.y += seg.units
    elif seg.direction == 'D':
        loc.y -= seg.units
    elif seg.direction == 'R':
        loc.x += seg.units
    elif seg.direction == 'L':
        loc.x -= seg.units
    else:
        raise TypeError(f'Unknown direction type {seg.direction}')
    return loc


def read_file(input_filename) -> list:
    with open(input_filename) as f:
        lines = [line.strip() for line in f.readlines()]
    lines.reverse()  # lines are reversed so they can be popped when parsed
    return lines


def point_in_circle(point: Point, circle: Circle) -> bool:
    h = hypot(point.x - circle.center.x, point.y - circle.center.y)
    return h < circle.radius


def find_largest_radius_inside(rect: Rect) -> float:
    height = rect.top - rect.bottom
    width = rect.right - rect.left
    if rect.top < rect.bottom:
        raise ValueError("Invalid rect height")
    elif rect.right < rect.left:
        raise ValueError("Invalid rect width")
    return min(height, width) / 2


class Heliport:
    def __init__(self, filename='heliport.in'):
        self.input_filename = filename

    def run_cases(self, filename=None):
        if filename:
            self.input_filename = filename
        lines = read_file(self.input_filename)
        case = 1
        while True:
            number_of_segments = int(lines.pop())
            if number_of_segments == 0:
                break
            roof = roof_outline(lines.pop())
            edges = candidate_edges(roof)
            radius = find_helipad_radius(edges, roof)
            if case > 1:
                print()
            print(f'Case Number {case} radius is: {radius:.2f}')
            case += 1


h = Heliport()
h.run_cases()
