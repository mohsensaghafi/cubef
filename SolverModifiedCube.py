from cube import U, Ui, F, Fi, f, fi, U2, F2, f2


# Helper Moves
def UiFiUF(c):
    return F(U(Fi(Ui(c))))


def UFUiFi(c):
    return Fi(Ui(F(U(c))))


def modified_cube_moves():
    """
    Moves for the modified cube
    """
    return [U, Ui, F, Fi, f, fi, U2, F2, f2]


def modified_cube_moves_special():
    """
    Moves for the modified cube
    """
    return [U, Ui, F, Fi, UiFiUF, UFUiFi]


def modified_cube_moves_special_extended():
    """
    Moves for the modified cube
    """
    return [U, Ui, F, Fi, UiFiUF, UFUiFi, f, fi, U2, F2, f2]
