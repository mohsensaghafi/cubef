import heapq
import sys
import time
from datetime import datetime


def A_star(start_state, successor_f, h_f, is_goal_f):
    explored = []
    g = 1
    h = h_f(start_state)
    f = g + h
    p = [(None, start_state)]
    frontiers = [(f, g, h, p)]
    it = 0
    process_time = 0
    sort_time = 0
    IN_time = 0
    while frontiers:
        f, g, h, path = frontiers.pop(0)
        (a, s) = path[-1]
        if is_goal_f(s):
            return path
        t_start = time.time()
        for (action, state) in successor_f(s):
            t_start_IN = time.time()
            if state not in explored:
                t_end_IN = time.time()
                IN_time += (t_end_IN - t_start_IN)
                explored.append(state)
                path2 = path[:]
                path2.append((action, state))
                h2 = h_f(state)
                g2 = g + 1
                f2 = h2 + g2
                frontiers.append((f2, g2, h2, path2))
        t2 = time.time()
        process_time += (t2 - t_start)
        frontiers.sort(key=lambda x: x[:3])
        t3 = time.time()
        sort_time += (t3 - t2)
        it += 1
        if it == 1000:
            dt = datetime.now().strftime("%Y-%m-%d %H:%M")
            print(dt, "forntiers size:", len(frontiers), frontiers[-1][:3], "top:", frontiers[-1][3][-1][1][4],
                  "Total Sort Time (S)", sort_time, "Total Search process (S)", IN_time, "Total Process time (S)",
                  process_time)
            it = 0

    return []
