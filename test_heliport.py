from heliport import RoofSegment, Point, Circle, Rect, Heliport
from heliport import roof_outline, update_location, read_file, point_in_circle, candidate_edges, \
    find_largest_radius_inside, find_helipad_radius


class TestHeliport:
    """def test_sample_output(self):
        results = ''
        for i, item in enumerate([1.0, 10.0]):
            if i > 0:
                results += '\n'
            results += f'Case Number {i+1} radius is: {item:.2f}\n'
        assert self.heliport.get_output() == results"""

    def test_read_file(self):
        lines = ['4',
                 '2 R 2 U 2 L 2 D',
                 '10',
                 '10 R 10 U 10 L 10 U 10 R 5 U 30 L 20 D 20 R 5 D',
                 '0']
        assert read_file('heliport.in') == lines

    def test_roof_outline(self):
        line = '2 R 2 U 2 L 2 D'
        roof = roof_outline(line)
        assert roof.upper_right_segments == [RoofSegment(2, 'R'), RoofSegment(2, 'U')]
        assert roof.upper_right_points == [Point(2, 0), Point(2, 2)]
        assert roof.bottom_left_segments == [RoofSegment(2, 'L'), RoofSegment(2, 'D')]
        assert roof.bottom_left_points == [Point(0, 2), Point(0, 0)]

    def test_update_location(self):
        assert Point(2, 0) == update_location(Point(0, 0), RoofSegment(2, 'R'))
        assert Point(2, 2) == update_location(Point(2, 0), RoofSegment(2, 'U'))
        assert Point(0, 2) == update_location(Point(2, 2), RoofSegment(2, 'L'))
        assert Point(0, 0) == update_location(Point(0, 2), RoofSegment(2, 'D'))

    def test_outside_point_in_circle(self):
        point = Point(-8, -7)
        circle = Circle(Point(-4, -4), 5)
        assert point_in_circle(point, circle) is False

    def test_inside_point_in_circle(self):
        point = Point(7, -6)
        circle = Circle(Point(4, -4), 5)
        assert point_in_circle(point, circle) is True

    def test_candidate_edges_square_roof(self):
        line = '2 R 2 U 2 L 2 D'
        edges = candidate_edges(roof_outline(line))
        assert edges.top == [2]
        assert edges.bottom == [0]
        assert edges.left == [0]
        assert edges.right == [2]

    def test_candidate_edges_poly_roof(self):
        line = '10 R 10 U 10 L 10 U 10 R 5 U 30 L 20 D 20 R 5 D'
        edges = candidate_edges(roof_outline(line))
        assert edges.top == [10, 20, 25]
        assert edges.bottom == [0, 5]
        assert edges.left == [-20, 0]
        assert edges.right == [0, 10]

    def test_find_largest_radius_inside(self):
        rect = Rect(1, 10, 5, 2)
        assert 2.0 == find_largest_radius_inside(rect)
        rect = Rect(-10, 4, -5, 2)
        assert 1.0 == find_largest_radius_inside(rect)

    def test_find_helipad_radius(self):
        line = '10 R 10 U 10 L 10 U 10 R 5 U 30 L 20 D 20 R 5 D'
        roof = roof_outline(line)
        edges = candidate_edges(roof)
        edges.top = [25]
        edges.left = [-20]
        edges.bottom = [5]
        assert find_helipad_radius(edges, roof) == 10.0

    def test_run_cases(self):
        heliport = Heliport()
        heliport.run_cases()
