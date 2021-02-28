import heapq
import sys
import time
from datetime import datetime

from cube import compress


def A_star(start_state, successor_f, h_f, is_goal_f):
    explored = set()
    g = 1
    h = h_f(start_state)
    f = g + h
    p = [(None, start_state)]
    frontiers = []
    heapq.heappush(frontiers, (f, g, h, p))
    it = 0
    process_time = 0
    IN_time = 0
    pop_time = 0
    push_time = 0

    while frontiers:
        t_pop_start = time.time()
        f, g, h, path = heapq.heappop(frontiers)
        t_pop_end = time.time()
        pop_time += (t_pop_end - t_pop_start)
        (a, s) = path[-1]
        if is_goal_f(s):
            return path
        t_start = time.time()
        for (action, state) in successor_f(s):
            t_start_IN = time.time()
            if compress(state) not in explored:
                t_end_IN = time.time()
                IN_time += (t_end_IN - t_start_IN)
                explored.add(compress(state))
                path2 = path[:]
                path2.append((action, state))
                h2 = h_f(state)
                g2 = g + 1
                f2 = h2 + g2
                t_push_start = time.time()
                heapq.heappush(frontiers, (f2, g2, h2, path2))
                t_push_end = time.time()
                push_time += (t_push_end - t_push_start)
        t2 = time.time()
        process_time += (t2 - t_start)
        it += 1
        if it == 100000:
            dt = datetime.now().strftime("%Y-%m-%d %H:%M")
            print(dt, "forntiers size:", len(frontiers), frontiers[-1][:3], "top:", frontiers[-1][3][-1][1][4],
                  " Push(S)", push_time, " Pop(S)", pop_time, " Search(S)", IN_time, " Process(S)",
                  process_time,
                  "frontiers(GB)", round(sys.getsizeof(frontiers) / 1073741824, 2),
                  "explored(GB)", round(sys.getsizeof(explored) / 1073741824, 2)
                  )
            it = 0

    return []
