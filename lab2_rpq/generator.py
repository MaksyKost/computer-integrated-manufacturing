import random

from utils import Task


def generate_instance(n, seed, x_type="29"):
    random.seed(seed)
    tasks = []

    p_vals = [random.randint(1, 29) for _ in range(n)]
    A = sum(p_vals)

    for i in range(n):
        r = random.randint(1, A)
        p = p_vals[i]
        X = 29 if x_type == "29" else A
        q = random.randint(1, X)
        tasks.append(Task(i + 1, r, p, q))

    return tasks