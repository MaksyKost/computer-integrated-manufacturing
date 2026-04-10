import random

def generate_instancen(seed, n, m):
    random.seed(seed)
    p = [[0] * n for _ in range(m)]
    for j in range(n):
        for i in range(m):
            p[i][j] = random.randint(1, 29)
    return p


def calculate_cmax(p, pi, n, m):
    if not pi:
        return 0
    C = [[0] * n for _ in range(m)]
    C[0][0] = p[0][pi[0]]
    for j in range(1, n):
        C[0][j] = C[0][j - 1] + p[0][pi[j]]

    for i in range(1, m):
        C[i][0] = C[i - 1][0] + p[i][pi[0]]

    for i in range(1, m):
        for j in range(1, n):
            C[i][j] = max(C[i - 1][j], C[i][j - 1]) + p[i][pi[j]]
    return C[m - 1][n - 1]


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
    

def print_schedule(p, pi, n, m, label=""):
    if label:
        print(f"\n{'='*60}")
        print(f"  {label}")
        print(f"{'='*60}")

    C = [[0] * n for _ in range(m)]
    C[0][0] = p[0][pi[0]]
    for j in range(1, n):
        C[0][j] = C[0][j-1] + p[0][pi[j]]
    for i in range(1, m):
        C[i][0] = C[i-1][0] + p[i][pi[0]]
    for i in range(1, m):
        for j in range(1, n):
            C[i][j] = max(C[i-1][j], C[i][j-1]) + p[i][pi[j]]

    col = 6
    header = f"{'':>{col}}" + "".join(f"  job{pi[j]+1:>2}" for j in range(n))
    print(header)
    print("-" * len(header))
    for i in range(m):
        row = f"  M{i+1:>2}  " + "".join(f"{C[i][j]:>{col}}" for j in range(n))
        print(row)
    print("-" * len(header))
    print(f"Kolejność: {' -> '.join(str(pi[j]+1) for j in range(n))}")
    print(f"C_max = {C[m-1][n-1]}")

if __name__ == "__main__":
    m = 3
    n = 5
    
    p = generate_instancen(42, n, m)

    print(f"\n{'='*60}")
    print(f"Wygenerowano {n} zadań, {m} maszyn!")
    pi_natural = list(range(n))
    print_schedule(p, pi_natural, n, m, "Kolejność naturalna")

    # Johnson — m
    if m == 2:
        pi_j = johnson_basic(p, n)
        print_schedule(p, pi_j, n, m, "Johnson klasyczny")
        
    elif m == 3:
        pi_j = johnson_extended(p, n)
        print_schedule(p, pi_j, n, m, "Johnson zmodyfikowany")
    else:
        print(f"\n{'='*60}")
        print(f"Johnson nie stosuje się do {m} maszyn.")
        
    # Brute Force
    pi_bf, _ = brute_force(p, n, m)
    print_schedule(p, pi_bf, n, m, "Brute Force")

    # Branch & Bound
    pi_bnb, _ = branch_and_bound(p, n, m)
    print_schedule(p, pi_bnb, n, m, "Branch & Bound")