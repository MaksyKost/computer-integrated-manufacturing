class Task:
    def __init__(self, task_id, r, p, q):
        self.id = task_id
        self.r = r
        self.p = p
        self.q = q

    def __repr__(self):
        return f"Task(id={self.id}, r={self.r}, p={self.p}, q={self.q})"


def calculate_cmax(pi):
    if not pi:
        return 0

    S = pi[0].r
    C = S + pi[0].p
    c_max = C + pi[0].q

    for j in range(1, len(pi)):
        S = max(pi[j].r, C)
        C = S + pi[j].p
        c_max = max(c_max, C + pi[j].q)

    return c_max


def calculate_cmax_full(pi):
    C_list = []
    S = pi[0].r
    C = S + pi[0].p
    c_max = C + pi[0].q
    C_list.append(C)

    for j in range(1, len(pi)):
        S = max(pi[j].r, C)
        C = S + pi[j].p
        c_max = max(c_max, C + pi[j].q)
        C_list.append(C)

    return c_max, C_list


def print_schedule(pi, label=""):
    if label:
        print(f"\n{'='*60}")
        print(f"  {label}")
        print(f"{'='*60}")

    col = 6
    header = f"{'k':>{col}} {'ID':>{col}} {'r':>{col}} {'p':>{col}} {'q':>{col}} {'S':>{col}} {'C':>{col}} {'C+q':>{col}}"
    print(header)
    print("-" * len(header))

    C = 0
    c_max = 0
    for k, task in enumerate(pi, start=1):
        S = max(task.r, C)
        C = S + task.p
        cq = C + task.q
        c_max = max(c_max, cq)
        print(f"{k:>{col}} {task.id:>{col}} {task.r:>{col}} {task.p:>{col}} {task.q:>{col}} {S:>{col}} {C:>{col}} {cq:>{col}}")

    print("-" * len(header))
    print(f"Kolejność: {' -> '.join(str(t.id) for t in pi)}")
    print(f"C_max = {c_max}")