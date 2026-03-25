import copy

from generator import generate_instance
from algorithms import schrage_basic, schrage, schrage_pmtn, carlier
from utils import print_schedule


if __name__ == "__main__":
    n_tasks = 10
    tasks = generate_instance(n_tasks, seed=1234, x_type="29")

    print(f"\nWygenerowano {n_tasks} zadań:")
    header = f"{'ID':>4} {'r':>4} {'p':>4} {'q':>4}"
    print(header)
    print("-" * len(header))
    for t in tasks:
        print(f"{t.id:>4} {t.r:>4} {t.p:>4} {t.q:>4}")

    pi_basic, cmax_basic = schrage_basic(tasks)
    print_schedule(pi_basic, "Schrage (wyszukiwanie w listach)")

    pi_queue, cmax_queue = schrage(tasks)
    print_schedule(pi_queue, "Schrage (z kolejką priorytetową)")

    pi_pmtn, cmax_pmtn = schrage_pmtn(tasks)
    print_schedule(pi_pmtn, "Schrage PMTN")

    cmax_carlier, pi_carlier = carlier(copy.deepcopy(tasks))
    print_schedule(pi_carlier, "Carlier")