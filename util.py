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
    in_operation_duration = 0
    pop_operation_duration = 0
    push_operation_duration = 0

    while frontiers:
        t1 = time.time()
        f, g, h, path = heapq.heappop(frontiers)
        pop_operation_duration += (time.time() - t1)
        (a, s) = path[-1]
        if is_goal_f(s):
            return path
        t_start = time.time()
        for (action, state) in successor_f(s):
            t_start_in_operation = time.time()
            if compress(state) not in explored:
                in_operation_duration += (time.time() - t_start_in_operation)
                explored.add(compress(state))
                path2 = path[:]
                path2.append((action, state))
                h2 = h_f(state)
                g2 = g + 1
                f2 = h2 + g2
                t_start_push_operation = time.time()
                heapq.heappush(frontiers, (f2, g2, h2, path2))
                push_operation_duration += (time.time() - t_start_push_operation)
        process_time += (time.time() - t_start)
        it += 1
        if it == 100000:
            print(datetime.now().strftime("%Y-%m-%d %H:%M")
                  , "frontiers size:", len(frontiers)
                  , "frontiers info", frontiers[-1][:3]
                  , "top side:", frontiers[-1][3][-1][1][4]
                  , "Push(S)", push_operation_duration
                  , "Pop(S)", pop_operation_duration
                  , "Search(S)", in_operation_duration
                  , " Process(S)", process_time
                  , "frontiers(GB)", round(sys.getsizeof(frontiers) / 1073741824, 2)
                  , "explored(GB)", round(sys.getsizeof(explored) / 1073741824, 2)
            )
            it = 0

    return []
