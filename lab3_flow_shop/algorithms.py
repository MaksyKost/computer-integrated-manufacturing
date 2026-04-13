from utils import calculate_cmax

def johnson_basic(p, n):
    lp = 0
    rp = n - 1
    N = list(range(n))
    pi = [0] * n
    
    while N:
        min_val = float("inf")
        min_j = -1
        min_i = -1
        for j in N:
            for i in range(2):
                if p[i][j] < min_val:
                    min_val = p[i][j]
                    min_j = j
                    min_i = i
        if min_i == 0:
            pi[lp] = min_j
            lp += 1
        else:
            pi[rp] = min_j
            rp -= 1
        N.remove(min_j)
    return pi

def johnson_extended(p, n):
    p_virtual = [
        [p[0][j] + p[1][j] for j in range(n)],
        [p[1][j] + p[2][j] for j in range(n)]
    ]
    return johnson_basic(p_virtual, n)

def brute_force(p, n, m):
    best = [float('inf')]
    best_pi = [None]

    def recurse(pi, N):
        if not N:
            cmax = calculate_cmax(p, pi, n, m)
            if cmax < best[0]:
                best[0] = cmax
                best_pi[0] = pi.copy()
            return
        for j in list(N):
                pi.append(j)
                N.remove(j)
                recurse(pi, N)
                pi.remove(j)
                N.append(j)
    
    recurse([], list(range(n)))
    return best_pi[0], best[0]

def branch_and_bound(p, n, m):
    pi_init = list(range(n))
    UB_init = calculate_cmax(p, pi_init, n, m)
    best = [UB_init]
    best_pi = [pi_init.copy()]

    def recurse(pi, N):
        if not N:
            cmax = calculate_cmax(p, pi, n, m)
            if cmax < best[0]:
                best[0] = cmax
                best_pi[0] = pi.copy()
            return
        for j in list(N):
                pi.append(j)
                N.remove(j)
                LB_value = calculate_cmax(p, pi, len(pi), m) + sum(p[m-1][j] for j in N)
                if LB_value < best[0]:
                    recurse(pi, N)
                pi.remove(j)
                N.append(j)
    
    recurse([], list(range(n)))
    return best_pi[0], best[0]