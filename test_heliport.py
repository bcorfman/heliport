import unittest
from heliport import Heliport


class TestHeliport(unittest.TestCase):
    def test_sample_output(self):
        h = Heliport('heliport.in')
        results = ''
        for i, item in enumerate([1.0, 10.0]):
            if i > 0:
                results += ''
            results += f'Case Number {i} radius is: {item:.2f}'
        self.assertEqual(h.print_output(), results)

    # def test_read_case(self):
    #     h = Heliport('heliport.in')
    #     h.read_case()
    #     self.assertEqual()
    #

if __name__ == '__main__':
    unittest.main()
