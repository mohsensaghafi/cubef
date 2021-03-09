from Solver import *
from SolverModifiedCube import modified_cube_moves, modified_cube_moves_special_extended
from cube import *


def main():
    """
    Cube Format:
    for each side we use the color character (b for Blue, g for Green, ...) from top left to bottom right row by row
    1  2  3
    4  5  6
    7  8  9

    for the while cube use the following sequence of sides (as above) to form the cube presentation in string
    Up, Left, Front, Right, Back, Down

    as flatten: (take care of Back and Down as the peace sequence might be flipped over
            UP
    Left    Frond   Right   Back
            Down

    Note: use cube() to generate a solved cube color
    """
    c = cube("gggogggggywywwowwwryryooooowwwgyyyyyororrrrrrbbbbbbbbb")

    """
    Patterns format:
    use color letter when that is a constraint (b for blue, g for green)
    and use x when that color is not a constraint at this moment.
    
    The sequence is the same as the Cube
    
    e.g.
    lc_2nd_layer_target = "xxxxxxxxxxxxwwwwwwxxxooooooxxxyyyyyyxxxrrrrrrbbbbbbbbb"
    lc_2nd_layer__left_p_target = "xxxxxxxxxxxxwwwwwwxxxooxoooxxxxyyyyyxxxrrrrrrbbbbbbbbb"
    lc_2nd_layer__right_p_target = "xxxxxxxxxxxxwwwwwwxxxooooooxxxyyyyyyxxxrrrrrrbbbbbbbbb"
    lc_top_cross = "xgxgggxgxxxxwwwwwwxxxooooooxxxyyyyyyxxxrrrrrrbbbbbbbbb"
    """
    solved_pattern = "gggggggggwwwwwwwwwoooooooooyyyyyyyyyrrrrrrrrrbbbbbbbbb"

    result = solve(c, solved_pattern, modified_cube_moves_special_extended())
    print(result)

    # apply list of moves on a cube
    # moves can be in a space separated string or a list of moves as function
    # e.g.
    # c_solved = move(c, "U F U fi U f U2 fi Ui f Fi")


if __name__ == "__main__":
    main()
