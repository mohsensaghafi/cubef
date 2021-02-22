from unittest import TestCase

from util import A_star


class Test(TestCase):
    def test_a_star(self):
        assert ("foo".upper() == "FOO")
        inc = lambda x: x + 1
        dbl = lambda x: x * 2
        big = lambda x: x + 10
        G = 97
        r = A_star(
            0,
            lambda s: [f(s) for f in [inc, big, dbl]],
            lambda s: G - s,
            lambda s: s == G
        )
        print(r)
