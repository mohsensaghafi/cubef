import unittest
from cube import *
from util import A_star


class Test(unittest.TestCase):
    def test_reverse_a_function(self):
        c = cube()
        self.assertEqual(c, apply_moves(c, [F, Fi]))
        self.assertEqual(c, apply_moves(c, "F Fi"))
        self.assertEqual(c, apply_moves(c, [F, Fi, U, Ui, U2, U2]))

    def test_make_some_moves(self):
        c = cube()
        expected = "grrbwbowbyogbrobrowrrybbyooyygrogbogyyowgwwgwbwwgygryr"
        self.assertEqual(expected, to_string(apply_moves(c, [U, R, F, Li, F, U2])))

    def test_a_star(self):
        inc = lambda x: x + 1
        dbl = lambda x: x * 2
        big = lambda x: x + 10
        G = 97
        r = A_star(
            0,
            lambda s: [(name, f(s)) for name, f in [('inc', inc), ('+10', big), ('dbl', dbl)]],
            lambda s: abs(G - s),
            lambda s: s == G
        )
        self.assertEqual(13, len(r))
        self.assertEqual(3,len(list(filter(lambda x: x[0] == '+10', r))))
        self.assertEqual(7, len(list(filter(lambda x: x[0] == 'inc', r))))
        self.assertEqual(2, len(list(filter(lambda x: x[0] == 'dbl', r))))


if __name__ == '__main__':
    unittest.main()
