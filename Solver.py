# TODO: implement the solver to solve the cube using A* method.
from functools import partial

from cube import *
from util import A_star_heap


def state_check(cube, pattern):
    return [(p == 'x' or c == p) for (c, p) in zip(cube, pattern)]


def possible_moves():
    return [U, Ui, F, Fi, L, Li, R, Ri, D, Di, B, Bi]


def successor_moves(s, fs):
    return [(f.__name__, STR(f(s))) for f in fs]


def solve(cube, target_pattern, possible_moves):
    """
    solver for cube:
    - set the presentation as string
    - define the target check and successor moves based on inputs
    - call A* method
    - collect the result and return
    """
    c1 = STR(cube)

    state_check_target = partial(state_check, pattern=target_pattern)
    cube_successor = partial(successor_moves, fs=possible_moves)

    def is_target_achived(s):
        return all(state_check_target(s))

    def calc_score(s):
        return state_check_target(s).count(False)

    result = A_star_heap(
        c1,
        cube_successor,
        calc_score,
        is_target_achived
    )
    print("result", result)
    if result and is_target_achived(result[-1][1]):
        return [item[0] for item in result][1:]
    else:
        raise TimeoutError("Couldn't find any solution")


def limited_cube_moves():
    """
    Moves for the limited cube
    """
    return [U, Ui, F, Fi, f, fi, U2, F2, f2]


def limited_cube_special_moves():
    """
    Moves for the limited cube
    """
    return [U, Ui, F, Fi, UiFiUF, UFUiFi]


def limited_cube_special_moves_extended():
    """
    Moves for the limited cube
    """
    return [U, Ui, F, Fi, UiFiUF, UFUiFi, f, fi, U2, F2, f2]


def UiFiUF(cube):
    return F(U(Fi(Ui(cube))))


def UFUiFi(cube):
    return Fi(Ui(F(U(cube))))
