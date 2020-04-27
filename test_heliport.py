import unittest
from heliport import Heliport


class TestHeliport(unittest.TestCase):
    def test_sample_output(self):
        h = Heliport('heliport.in')
        results = ''
        for i, item in enumerate([1.0, 10.0]):
            if i > 0:
                results += '\n'
            results += f'Case Number {i+1} radius is: {item:.2f}\n'
        self.assertEqual(h.get_output(), results)

    def test_read_file(self):
        lines = ['4',
                 '2 R 2 U 2 L 2 D',
                 '10',
                 '10 R 10 U 10 L 10 U 10 R 5 U 30 L 20 D 20 R 5 D',
                 '0']
        h = Heliport('heliport.in')
        self.assertEqual(h._read_file('heliport.in'), lines)

    def test_read_cases(self):
        h = Heliport('heliport.in')
        lines = ['4',
                 '2 R 2 U 2 L 2 D',
                 '10',
                 '10 R 10 U 10 L 10 U 10 R 5 U 30 L 20 D 20 R 5 D',
                 '0']
        cases = h._read_cases(lines)
        test_cases = [[4, [[2, 'R'], [2, 'U'], [2, 'L'], [2, 'D']]],
                      [10, [[10, 'R'], [10, 'U'], [10, 'L'], [10, 'U'], [10, 'R'],
                            [5, 'U'], [30, 'L'], [20, 'D'], [20, 'R'], [5, 'D']]]]
        self.assertEqual(test_cases, cases)

    def test_tokenize_segments(self):
        h = Heliport('heliport.in')
        segment_line = '2 R 2 U 2 L 2 D'
        segment_tokens = ['D', '2', 'L', '2', 'U', '2', 'R', '2']
        self.assertEqual(h._tokenize_segments(segment_line), segment_tokens)

    # def test_read_case(self):
    #     h = Heliport('heliport.in')
    #     h.read_case()
    #     self.assertEqual()
    #


if __name__ == '__main__':
    unittest.main()
