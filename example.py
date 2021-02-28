from Solver import *
from cube import *


def main():
    print("Start...")
    # c = cube()
    # print(side_to_special_repr_base_90)
    # print(side_to_special_repr_base_90('rrrrrrrrr'))
    # print(compress(cube()))
    # return 0
    # show(move("wwwwwwwwwrrrrrrrrrbbbbbbbbbooooooooogggggggggyyyyyyyyy", [U, U, U, F, F, F, L, R]))
    # return 0
    # c = cube()
    # show(c)
    # show(move(c, [U]), "U")
    # show(move(c, [U, R]), "UR")
    # show(move(c, [U, R, F]), "URF")
    # return 0
    # c3 = cube("ggygggggywwwwwwwwwoogoooooooyryyyyyygrrrrrrrrbbbbbbbbb")
    # c3_solved = move(c3, "F2 U F Ui Fi Fi U F Ui Fi U F Ui Fi U F Ui Fi U F Ui Fi F2 U F Ui Fi Fi U F Ui Fi")
    # print(STR(c3_solved))
    # return 0
    lc_2nd_layer_target = "xxxxxxxxxxxxwwwwwwxxxooooooxxxyyyyyyxxxrrrrrrbbbbbbbbb"
    lc_2nd_layer__left_p_target = "xxxxxxxxxxxxwwwwwwxxxooxoooxxxxyyyyyxxxrrrrrrbbbbbbbbb"
    lc_2nd_layer__right_p_target = "xxxxxxxxxxxxwwwwwwxxxooooooxxxyyyyyyxxxrrrrrrbbbbbbbbb"
    lc_top_cross = "xgxgggxgxxxxwwwwwwxxxooooooxxxyyyyyyxxxrrrrrrbbbbbbbbb"
    solved_pattern = "gggggggggwwwwwwwwwoooooooooyyyyyyyyyrrrrrrrrrbbbbbbbbb"
    c = cube("gggogggggywywwowwwryryooooowwwgyyyyyororrrrrrbbbbbbbbb")

    # c1 = cube("rggwgrwyoggowwwwwwgoyooooooggygyyyyyrywrrrrrrbbbbbbbbb")
    # r = solve(c1, lc_2nd_layer__right_p_target, limited_cube_moves())
    # print(r)
    c2 = cube("ggwggwyrryyrwwwwwwggwooooooggoyyyyyygoorrrrrrbbbbbbbbb")
    # r = solve(c2, lc_top_cross, limited_cube_moves())
    # print(r)
    # show(c2)
    # ccc = move(c2, "U2 F fi Ui f Fi U2 F fi Ui f Fi")
    # show(ccc)
    c3 = cube("wgrgggggyrwwwwwwwwoogoooooooygyyyyyyyrgrrrrrrbbbbbbbbb")
    c3 = cube("ggygggggywwwwwwwwwoogoooooooyryyyyyygrrrrrrrrbbbbbbbbb")
    r = solve(c3, solved_pattern, limited_cube_special_moves_extended())
    print(r)
    # c_1st_cross = move(c, "U F U fi U f U2 fi Ui f Fi")
    # print(STR(c_1st_cross))
    # show(c_1st_cross)
    # result = []
    # for _ in range(10):
    #     r = solve(c, lc_2nd_layer__left_p_target, limited_cube_moves())
    #     result.append("  ".join(r))
    # print("---------------------")
    # for r in result:
    #     print(r)
    # print("--------------------")
    # print(result)
    return 0

    result = solve(c, lc_1st_layer_target, limited_cube_moves())
    # result = solve(c, lc_2nd_layer_target, limited_cube_moves())
    # result = solve(c, solved_pattern, limited_cube_moves())
    print(result)

    return 0
    inc = lambda x: x + 1
    dbl = lambda x: x * 2
    big = lambda x: x + 10
    G = 97
    r = A_star_heap(
        0,
        lambda s, a: [(n, f(s)) for n, f in {'inc': inc, 'big': big, 'dbl': dbl}.items()],
        lambda s: G - s if s <= G else 10000,
        lambda s: s == G
    )
    print("r=", r)
    for a, s in r:
        print("action", a, "\tstate", s)
    return 0
    c = cube()
    # c1 = move(c, [Ri, Di, R, D])
    # c1 = move(c, "Ri Di R D")
    c1 = apply_moves(c, [Ri, Di, R, D])
    print(c1)
    show(c1)
    # show(U(c), 'U')
    # show(Ui(c), 'Ui')

    # show(R(c), 'R')
    # show(Ri(c), 'Ri')

    # show(L(c), 'L')
    # show(Li(c), 'Li')

    # show(D(c), 'D')
    # show(Di(c), 'Di')

    # show(F(c), 'F')
    # show(Fi(c), 'Fi')

    # show(B(c), 'B')
    # show(Bi(c), 'Bi')


if __name__ == "__main__":
    main()
