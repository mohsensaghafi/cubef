import heapq
import sys
import time
from datetime import datetime

from cube import shortVersion


def A_star(start_state, successor_f, h_f, is_goal_f):
    raise DeprecationWarning
    # print(start_state)
    # print(successor_f)
    # print(h_f)
    # print(is_goal_f)
    explored = []
    g = 1
    h = h_f(start_state)
    f = g + h
    p = [(None, start_state)]
    frontiers = [(f, g, h, p)]
    # print("init frontiers:", frontiers)
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
                # not mutch to the optimized solution. any solution is good for now
                # if is_goal_f(state):
                #     return path2
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


def A_star_heap(start_state, successor_f, h_f, is_goal_f):
    # print(start_state)
    # print(successor_f)
    # print(h_f)
    # print(is_goal_f)
    explored = set()
    g = 1
    h = h_f(start_state)
    f = g + h
    p = [(None, start_state)]
    frontiers = []
    heapq.heappush(frontiers, (f, g, h, p))
    # print("init frontiers:", frontiers)
    it = 0
    process_time = 0
    # sort_time = 0
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
            if shortVersion(state) not in explored:
                t_end_IN = time.time()
                IN_time += (t_end_IN - t_start_IN)
                explored.add(shortVersion(state))
                path2 = path[:]
                path2.append((action, state))
                # not mutch to the optimized solution. any solution is good for now
                # if is_goal_f(state):
                #     return path2
                h2 = h_f(state)
                g2 = g + 1
                f2 = h2 + g2
                t_push_start = time.time()
                heapq.heappush(frontiers, (f2, g2, h2, path2))
                t_push_end = time.time()
                push_time += (t_push_end - t_push_start)
        t2 = time.time()
        process_time += (t2 - t_start)
        # frontiers.sort(key=lambda x: x[:3])
        # t3 = time.time()
        # sort_time += (t3 - t2)
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
