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