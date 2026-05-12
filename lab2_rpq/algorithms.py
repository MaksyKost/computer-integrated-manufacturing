import heapq
import copy

from utils import calculate_cmax_full


def schrage(tasks):
    N = sorted(tasks, key=lambda x: x.r, reverse=True)
    G = []

    t = min([task.r for task in N]) if N else 0
    c_max = 0
    pi = []

    while G or N:
        while N and N[-1].r <= t:
            task = N.pop()
            heapq.heappush(G, (-task.q, task.id, task))

        if G:
            _, _, task = heapq.heappop(G)
            pi.append(task)
            t += task.p
            c_max = max(c_max, t + task.q)
        else:
            t = N[-1].r

    return pi, c_max


def schrage_basic(tasks):
    N = list(tasks)
    G = []

    t = min((task.r for task in N), default=0)
    c_max = 0
    pi = []

    while G or N:
        ready_tasks = [task for task in N if task.r <= t]
        for task in ready_tasks:
            G.append(task)
            N.remove(task)

        if G:
            best_task = max(G, key=lambda x: x.q)
            G.remove(best_task)

            pi.append(best_task)
            t += best_task.p
            c_max = max(c_max, t + best_task.q)
        else:
            t = min(task.r for task in N)

    return pi, c_max


def schrage_pmtn(tasks):
    N = sorted(copy.deepcopy(tasks), key=lambda x: x.r, reverse=True)
    G = []

    t = min([task.r for task in N]) if N else 0
    c_max = 0
    pi = []

    while G or N:
        while N and N[-1].r <= t:
            task = N.pop()
            heapq.heappush(G, (-task.q, task.id, task))

        if G:
            _, _, task = heapq.heappop(G)
            if N and t + task.p > N[-1].r and N[-1].q > task.q:
                t_stop = N[-1].r
                task.p = task.p - (t_stop - t)
                t = t_stop
                heapq.heappush(G, (-task.q, task.id, task))
            else:
                pi.append(task)
                t += task.p
                c_max = max(c_max, t + task.q)
        else:
            t = N[-1].r

    return pi, c_max


def carlier(tasks, UB=None, best_pi=None):
    pi, U = schrage(tasks)

    if UB is None or U < UB:
        UB = U
        best_pi = list(pi)

    c_max, C_list = calculate_cmax_full(pi)

    b = -1
    for j in range(len(pi)):
        if C_list[j] + pi[j].q == c_max:
            b = j

    a = b
    p_sum = 0
    for j in range(b, -1, -1):
        p_sum += pi[j].p
        if pi[j].r + p_sum + pi[b].q == c_max:
            a = j

    c = -1
    for j in range(a, b):
        if pi[j].q < pi[b].q:
            c = j

    if c == -1:
        return UB, best_pi

    K = pi[c+1 : b+1]
    r_hat = min(t.r for t in K)
    q_hat = min(t.q for t in K)
    p_hat = sum(t.p for t in K)

    old_r = pi[c].r
    pi[c].r = max(pi[c].r, r_hat + p_hat)
    _, LB = schrage_pmtn(tasks)
    if LB < UB:
        UB, best_pi = carlier(tasks, UB, best_pi)
    pi[c].r = old_r

    old_q = pi[c].q
    pi[c].q = max(pi[c].q, q_hat + p_hat)
    _, LB = schrage_pmtn(tasks)
    if LB < UB:
        UB, best_pi = carlier(tasks, UB, best_pi)
    pi[c].q = old_q

    return UB, best_pi