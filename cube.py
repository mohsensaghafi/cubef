import functools
import itertools

from functional_helper import comp

COLOR_CODE = {
    'w': 0,
    'r': 1,
    'b': 2,
    'o': 3,
    'g': 4,
    'y': 5,
}


def cube(init_value=None):
    """
    model a cube as each element of U L F R B D
    """
    if init_value is None:
        return [i for i in itertools.chain(
            itertools.repeat('w', 9),
            itertools.repeat('r', 9),
            itertools.repeat('b', 9),
            itertools.repeat('o', 9),
            itertools.repeat('g', 9),
            itertools.repeat('y', 9)
        )]
    elif init_value == "":
        return [i for i in range(54)]
    elif isinstance(init_value, list):
        return init_value[:]
    else:
        return list(init_value)


def show(cube, title=''):
    print("""{54}
        [{0}][{1}][{2}]
        [{3}][{4}][{5}]
        [{6}][{7}][{8}]
[{9}][{10}][{11}]   [{18}][{19}][{20}]   [{27}][{28}][{29}]   [{36}][{37}][{38}]
[{12}][{13}][{14}]   [{21}][{22}][{23}]   [{30}][{31}][{32}]   [{39}][{40}][{41}]
[{15}][{16}][{17}]   [{24}][{25}][{26}]   [{33}][{34}][{35}]   [{42}][{43}][{44}]
        [{45}][{46}][{47}]
        [{48}][{49}][{50}]
        [{51}][{52}][{53}]""".format(*cube, title))


def U(c):
    return [c[i] for i in [
        6, 3, 0,
        7, 4, 1,
        8, 5, 2,

        18, 19, 20,
        12, 13, 14,
        15, 16, 17,

        27, 28, 29,
        21, 22, 23,
        24, 25, 26,

        36, 37, 38,
        30, 31, 32,
        33, 34, 35,

        9, 10, 11,
        39, 40, 41,
        42, 43, 44,

        45, 46, 47,
        48, 49, 50,
        51, 52, 53]]


def Ui(c):
    return [c[i] for i in [
        2, 5, 8,
        1, 4, 7,
        0, 3, 6,

        36, 37, 38,
        12, 13, 14,
        15, 16, 17,

        9, 10, 11,
        21, 22, 23,
        24, 25, 26,

        18, 19, 20,
        30, 31, 32,
        33, 34, 35,

        27, 28, 29,
        39, 40, 41,
        42, 43, 44,

        45, 46, 47,
        48, 49, 50,
        51, 52, 53]]


def R(c):
    return [c[i] for i in [
        0, 1, 20,
        3, 4, 23,
        6, 7, 26,

        9, 10, 11,
        12, 13, 14,
        15, 16, 17,

        18, 19, 47,
        21, 22, 50,
        24, 25, 53,

        33, 30, 27,
        34, 31, 28,
        35, 32, 29,

        8, 37, 38,
        5, 40, 41,
        2, 43, 44,

        45, 46, 42,
        48, 49, 39,
        51, 52, 36]]


def Ri(c):
    return [c[i] for i in [
        0, 1, 42,
        3, 4, 39,
        6, 7, 36,

        9, 10, 11,
        12, 13, 14,
        15, 16, 17,

        18, 19, 2,
        21, 22, 5,
        24, 25, 8,

        29, 32, 35,
        28, 31, 34,
        27, 30, 33,

        53, 37, 38,
        50, 40, 41,
        47, 43, 44,

        45, 46, 20,
        48, 49, 23,
        51, 52, 26]]


def L(c):
    return [c[i] for i in [
        44, 1, 2,
        41, 4, 5,
        38, 7, 8,

        15, 12, 9,
        16, 13, 10,
        17, 14, 11,

        0, 19, 20,
        3, 22, 23,
        6, 25, 26,

        27, 28, 29,
        30, 31, 32,
        33, 34, 35,

        36, 37, 51,
        39, 40, 48,
        42, 43, 45,

        18, 46, 47,
        21, 49, 50,
        24, 52, 53]]


def Li(c):
    return [c[i] for i in [
        18, 1, 2,
        21, 4, 5,
        24, 7, 8,

        11, 14, 17,
        10, 13, 16,
        9, 12, 15,

        45, 19, 20,
        48, 22, 23,
        51, 25, 26,

        27, 28, 29,
        30, 31, 32,
        33, 34, 35,

        36, 37, 6,
        39, 40, 3,
        42, 43, 0,

        44, 46, 47,
        41, 49, 50,
        38, 52, 53]]


def F(c):
    return [c[i] for i in [
        0, 1, 2,
        3, 4, 5,
        17, 14, 11,

        9, 10, 45,
        12, 13, 46,
        15, 16, 47,

        24, 21, 18,
        25, 22, 19,
        26, 23, 20,

        6, 28, 29,
        7, 31, 32,
        8, 34, 35,

        36, 37, 38,
        39, 40, 41,
        42, 43, 44,

        33, 30, 27,
        48, 49, 50,
        51, 52, 53]]


def Fi(c):
    return [c[i] for i in [
        0, 1, 2,
        3, 4, 5,
        27, 30, 33,

        9, 10, 8,
        12, 13, 7,
        15, 16, 6,

        20, 23, 26,
        19, 22, 25,
        18, 21, 24,

        47, 28, 29,
        46, 31, 32,
        45, 34, 35,

        36, 37, 38,
        39, 40, 41,
        42, 43, 44,

        11, 14, 17,
        48, 49, 50,
        51, 52, 53]]


def B(c):
    return [c[i] for i in [
        29, 32, 35,
        3, 4, 5,
        6, 7, 8,

        2, 10, 11,
        1, 13, 14,
        0, 16, 17,

        18, 19, 20,
        21, 22, 23,
        24, 25, 26,

        27, 28, 53,
        30, 31, 52,
        33, 34, 51,

        42, 39, 36,
        43, 40, 37,
        44, 41, 38,

        45, 46, 47,
        48, 49, 50,
        9, 12, 15]]


def Bi(c):
    return [c[i] for i in [
        15, 12, 9,
        3, 4, 5,
        6, 7, 8,

        51, 10, 11,
        52, 13, 14,
        53, 16, 17,

        18, 19, 20,
        21, 22, 23,
        24, 25, 26,

        27, 28, 0,
        30, 31, 1,
        33, 34, 2,

        38, 41, 44,
        37, 40, 43,
        36, 39, 42,

        45, 46, 47,
        48, 49, 50,
        35, 32, 29]]


def D(c):
    return [c[i] for i in [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,

        9, 10, 11,
        12, 13, 14,
        42, 43, 44,

        18, 19, 20,
        21, 22, 23,
        15, 16, 17,

        27, 28, 29,
        30, 31, 32,
        24, 25, 26,

        36, 37, 38,
        39, 40, 41,
        33, 34, 35,

        51, 48, 45,
        52, 49, 46,
        53, 50, 47]]


def Di(c):
    return [c[i] for i in [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8,

        9, 10, 11,
        12, 13, 14,
        24, 25, 26,

        18, 19, 20,
        21, 22, 23,
        33, 34, 35,

        27, 28, 29,
        30, 31, 32,
        42, 43, 44,

        36, 37, 38,
        39, 40, 41,
        15, 16, 17,

        47, 50, 53,
        46, 49, 52,
        45, 48, 51]]


def u(c):
    # TODO: need to be implemented.
    raise NotImplemented


def ui(c):
    # TODO: need to be implemented.
    raise NotImplemented


def r(c):
    # TODO: need to be implemented.
    raise NotImplemented


def ri(c):
    # TODO: need to be implemented.
    raise NotImplemented


def l(c):
    # TODO: need to be implemented.
    raise NotImplemented


def li(c):
    # TODO: need to be implemented.
    raise NotImplemented


def f(c):
    return [c[i] for i in [
        0, 1, 2,
        16, 13, 10,
        17, 14, 11,

        9, 48, 45,
        12, 49, 46,
        15, 50, 47,

        24, 21, 18,
        25, 22, 19,
        26, 23, 20,

        6, 3, 29,
        7, 4, 32,
        8, 5, 35,

        36, 37, 38,
        39, 40, 41,
        42, 43, 44,

        33, 30, 27,
        34, 31, 28,
        51, 52, 53]]


def fi(c):
    return [c[i] for i in [
        0, 1, 2,
        28, 31, 34,
        27, 30, 33,

        9, 5, 8,
        12, 4, 7,
        15, 3, 6,

        20, 23, 26,
        19, 22, 25,
        18, 21, 24,

        47, 50, 29,
        46, 49, 32,
        45, 48, 35,

        36, 37, 38,
        39, 40, 41,
        42, 43, 44,

        11, 14, 17,
        10, 13, 16,
        51, 52, 53]]


def b(c):
    # TODO: need to be implemented.
    raise NotImplemented


def bi(c):
    # TODO: need to be implemented.
    raise NotImplemented


def d(c):
    # TODO: need to be implemented.
    raise NotImplemented


def di(c):
    # TODO: need to be implemented.
    raise NotImplemented


def X(c):
    # TODO: need to be implemented.
    raise NotImplemented


def Xi(c):
    # TODO: need to be implemented.
    raise NotImplemented


def Y(c):
    # TODO: need to be implemented.
    raise NotImplemented


def Yi(c):
    # TODO: need to be implemented.
    raise NotImplemented


def Z(c):
    # TODO: need to be implemented.
    raise NotImplemented


def Zi(c):
    # TODO: need to be implemented.
    raise NotImplemented


def M(c):
    # TODO: need to be implemented. Middle Layer
    raise NotImplemented


def Mi(c):
    # TODO: need to be implemented.
    raise NotImplemented


def E(c):
    # TODO: need to be implemented. Equator Layer
    raise NotImplemented


def Ei(c):
    # TODO: need to be implemented.
    raise NotImplemented


def S(c):
    # TODO: need to be implemented. Standing Layer (Layer between Front and Back)
    raise NotImplemented


def Si(c):
    # TODO: need to be implemented.
    raise NotImplemented


def U2(c):
    return U(U(c))


def F2(c):
    return F(F(c))


def f2(c):
    return f(f(c))


def apply_moves(c, moves):
    if isinstance(moves, str):
        return apply_moves_f(c, list(map(get_move, moves.split(" "))))
    else:
        return apply_moves_f(c, moves)


def apply_moves_f(c, moves_list):
    return comp(moves_list)(cube(c))


def get_move(move):
    d = {
        'R': R,
        'Ri': Ri,
        'L': L,
        'Li': Li,
        'U': U,
        'Ui': Ui,
        'D': D,
        'Di': Di,
        'F': F,
        'Fi': Fi,
        'B': B,
        'Bi': Bi,
        'f': f,
        'fi': fi,
        'f2': f2,
        'F2': F2,
        'U2': U2
    }
    return d.get(move, None)


def to_string(lst):
    return "".join(lst)


def split_sides(c):
    return [c[i:i + 9] for i in range(0, 54, 9)]


def to_base_6(side):
    return functools.reduce(lambda total, piece_color: total * 6 + COLOR_CODE[piece_color]
                            , side
                            , 0)


def to_base_b_rev(n, base=16):
    # for the sake of performance ignore the recursion due to not having tail-optimization in python
    result = []
    while n > 0:
        result.append(n % base)
        n //= base
    return result


# in our representation its only important they become unique,
# having everything reversed is not going to make any difference.
to_base_90 = functools.partial(to_base_b_rev, base=90)


def to_special_str_repr(lst):
    """
    this function receive a list which each item is a digit in our base (let say 90)
    and offset them with 33 to avoid not readable characters.
    then we use the ascii code from 33 to 127 to cast them into a readable char.
    then concat them together to form a string
    """
    return to_string([chr(i + 33) for i in lst])


side_to_special_repr_base_90 = comp([
    to_base_6,
    to_base_90,
    lambda lst: lst[:4],  # with our size, only 4 digit will cover the whole representations.
    to_special_str_repr
])


def compress(c):
    return to_string([side_to_special_repr_base_90(side) for side in split_sides(c)])
