from cube import U, Ui, F, Fi, f, fi, U2, F2, f2


# Helper Moves
# TODO: if this is useful on solving 3x3x3, maybe better to move it into Cube.py
# TODO: this function can be implemented using Comp. we need to solve the problem of function name.
# to identify the moves, the function.__name__ is used. in case of comp it will be always "lambda"
def UiFiUF(c):
    return F(U(Fi(Ui(c))))


# TODO: if this is useful on solving 3x3x3, maybe better to move it into Cube.py
# TODO: this function can be implemented using Comp. we need to solve the problem of function name.
# to identify the moves, the function.__name__ is used. in case of comp it will be always "lambda"
def UFUiFi(c):
    return Fi(Ui(F(U(c))))


def modified_cube_moves():
    """
    Moves for the modified cube
    """
    return {U, Ui, F, Fi, f, fi, U2, F2, f2}


def modified_cube_moves_special():
    """
    Moves for the modified cube
    """
    return {U, Ui, F, Fi, UiFiUF, UFUiFi}


def modified_cube_moves_special_extended():
    """
    Moves for the modified cube
    """
    return {U, Ui, F, Fi, UiFiUF, UFUiFi, f, fi, U2, F2, f2}
