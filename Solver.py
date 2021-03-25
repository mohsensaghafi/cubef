from functools import partial

from cube import *
from util import A_star


def state_check(c, pattern):
    return [(p == 'x' or c == p) for (c, p) in zip(c, pattern)]


def possible_moves():
    """
    This is the list of all moves that can apply on a cube
    Note: This is not the full list, some moves are not implemented yet.
    Todo: Update this list after complete implementation of the moves.
    """
    return {U, Ui, F, Fi, L, Li, R, Ri, D, Di, B, Bi}


def successor_moves(s, function_list):
    return {(func.__name__, to_string(func(s))) for func in function_list}


def solve(c, target_pattern, moves):
    """
    solver for cube:
    - set the presentation as string
    - define the target check and successor moves based on inputs
    - call A* method
    - collect the result and return
    """
    c1 = to_string(c)

    state_check_target = partial(state_check, pattern=target_pattern)
    cube_successor = partial(successor_moves, function_list=moves)

    def is_target_achieved(s):
        return all(state_check_target(s))

    def calc_score(s):
        return state_check_target(s).count(False)

    result = A_star(
        c1,
        cube_successor,
        calc_score,
        is_target_achieved,
        compress
    )
    print("result", result)
    if result and is_target_achieved(result[-1][1]):
        return [item[0] for item in result][1:]
    else:
        raise TimeoutError("Couldn't find any solution")

# TODO: implement some helper functions for solving steps for each cube
# Some of the candidate functions are:
# - first_layer_cross
# - first_layer_corners
# - second_layer_corners
# - third_layer_cross
# - ...
