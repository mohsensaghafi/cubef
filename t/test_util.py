import unittest
from cube import *


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



if __name__ == '__main__':
    unittest.main()