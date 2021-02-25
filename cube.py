import itertools

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
    if init_value == None:
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


def U(cube):
    return [cube[i] for i in [
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


def Ui(cube):
    return [cube[i] for i in [
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


def R(cube):
    return [cube[i] for i in [
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


def Ri(cube):
    return [cube[i] for i in [
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


def L(cube):
    return [cube[i] for i in [
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


def Li(cube):
    return [cube[i] for i in [
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


def F(cube):
    return [cube[i] for i in [
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


def Fi(cube):
    return [cube[i] for i in [
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


def B(cube):
    return [cube[i] for i in [
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


def Bi(cube):
    return [cube[i] for i in [
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


def D(cube):
    return [cube[i] for i in [
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


def Di(cube):
    return [cube[i] for i in [
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


def u(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def ui(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def r(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def ri(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def l(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def li(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def f(cube):
    return [cube[i] for i in [
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


def fi(cube):
    return [cube[i] for i in [
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


def b(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def bi(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def d(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def di(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def X(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def Xi(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def Y(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def Yi(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def Z(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def Zi(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def M(cube):
    # TODO: need to be implemented. Middle Layer
    raise NotImplemented


def Mi(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def E(cube):
    # TODO: need to be implemented. Equator Layer
    raise NotImplemented


def Ei(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def S(cube):
    # TODO: need to be implemented. Standing Layer (Layer between Front and Back)
    raise NotImplemented


def Si(cube):
    # TODO: need to be implemented.
    raise NotImplemented


def U2(cube):
    return U(U(cube))


def F2(cube):
    return F(F(cube))


def f2(cube):
    return f(f(cube))


def move(cube, moves):
    c = cube[:]
    if isinstance(moves, str):
        moves = list(map(get_move, moves.split(" ")))
    for move in moves:
        c = move(c)
    return c


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


def STR(cube):
    return "".join(cube)


def charMap(num):
    return chr(num + 33)


def shortten(num):
    n = num
    l = []
    for _ in range(4):
        l.append(charMap(n % 90))
        n //= 90
    return STR(l)


def shortVersion(cube):
    base_10 = 0
    result = []
    for index, c in enumerate(cube):
        base_10 *= 6
        base_10 += COLOR_CODE[c]
        if index % 9 == 8:
            result.append(shortten(base_10))
            base_10 = 0
    return STR(result)
