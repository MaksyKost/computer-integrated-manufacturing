from algorithms import johnson_basic, johnson_extended, brute_force, branch_and_bound
from utils import generate_instancen, print_schedule

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