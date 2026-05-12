import itertools
import random
import math

class Job:
    def __init__(self, id, p, w, d):
        self.id = id
        self.p = p
        self.w = w
        self.d = d

    def __repr__(self):
        return f"Job(id={self.id}, p={self.p}, w={self.w}, d={self.d})"

def generate_instance(n, seed, x_type='A'):
    random.seed(seed) 
    #dla każdego j: p_j = nextInt(1, 29)
    p = [random.randint(1, 29) for _ in range(n)]
    A = sum(p)
    #dla każdego j: w_j = nextInt(1, 9)
    w = [random.randint(1, 9) for _ in range(n)]
    #dla każdego j: d_j = nextInt(1, X)
    X = A if x_type == 'A' else 29
    d = [random.randint(1, X) for _ in range(n)]
    
    return [Job(i+1, p[i], w[i], d[i]) for i in range(n)]

def evaluate_schedule(schedule):
    #wartość funkcji celu F(pi) = Suma w_j * T_j
    current_time = 0
    total_penalty = 0
    
    for job in schedule:
        current_time += job.p
        #T_j = max(C_j - d_j, 0)
        tardiness = max(current_time - job.d, 0)
        total_penalty += tardiness * job.w
        
    return total_penalty


#Przegląd zupełny 
def brute_force(jobs):
    #wszystkie n! kombinacji uszeregowania zadań
    best_cost = math.inf
    best_schedule = None
    
    #itertools.permutations generuje wszystkie możliwe kolejności
    for perm in itertools.permutations(jobs):
        cost = evaluate_schedule(perm)
        if cost < best_cost:
            best_cost = cost
            best_schedule = list(perm)
            
    return best_schedule, best_cost

#Algorytm zachłanny
def greedy(jobs):
    #sortowanie zadań rosnąco według d_j
    schedule = sorted(jobs, key=lambda j: j.d)
    return schedule, evaluate_schedule(schedule)

def dynamic_programming(jobs):
    #Iteracyjne programowanie dynamiczne wykorzystujące reprezentację 
    #podproblemów za pomocą masek bitowych.
    n = len(jobs)
    #rozmiar tablicy to 2^n (uwzględniając wartość 0)
    #wartości w memory przechowują najmniejszą karę dla danego podzbioru
    memory = [math.inf] * (1 << n)
    memory[0] = 0
    
    #backtracking zapisuje które zadanie zostało wykonane jako 
    # ostatnie, aby osiągnąć minimalny koszt.
    parent = [-1] * (1 << n) 

    #iteracja po wszystkich podzbiorach D (od 1 do 2^n - 1)
    for mask in range(1, 1 << n):
        #suma czasów (sum_p) dla aktualnego podzbioru zadań
        sum_p = 0
        for j in range(n):
            if mask & (1 << j):  #jeśli j-ty bit jest ustawiony, to zadanie jest w D
                sum_p += jobs[j].p
                
        #najlepsze zadanie do umieszczenia na końcu
        for j in range(n):
            if mask & (1 << j):
                #podzbiór bez j-tego zadania
                prev_mask = mask ^ (1 << j)
                
                #kara za spóźnienie dla zadanego elementu umieszczonego jako ostatniego
                tardiness = max(sum_p - jobs[j].d, 0)
                cost = tardiness * jobs[j].w + memory[prev_mask]
                
                if cost < memory[mask]:
                    memory[mask] = cost
                    parent[mask] = j  #do backtrackingu

    #odtwarzanie kolejności od końca
    mask = (1 << n) - 1  #maska początkowa ze wszystkimi bitami na 1
    schedule = []
    
    while mask > 0:
        last_job_idx = parent[mask]
        schedule.append(jobs[last_job_idx])
        mask ^= (1 << last_job_idx)
        
    schedule.reverse()
    
    return schedule, memory[(1 << n) - 1]

if __name__ == "__main__":
    N = 10
    SEED = 12345
    
    # Testujemy dla parametru X=A
    print("--- Test instancji (seed=12345, X=A) ---")
    jobs = generate_instance(N, SEED, x_type='A')
    
    print("Zadania w instancji:")
    for j in jobs:
        print(f"  {j}")
    print()

    bf_sched, bf_cost = brute_force(jobs)
    print(f"[Brute Force] Koszt: {bf_cost}, Kolejność ID: {[j.id for j in bf_sched]}")

    gr_sched, gr_cost = greedy(jobs)
    print(f"[Zachłanny]   Koszt: {gr_cost}, Kolejność ID: {[j.id for j in gr_sched]}")

    dp_sched, dp_cost = dynamic_programming(jobs)
    print(f"[Dyn. Progr]  Koszt: {dp_cost}, Kolejność ID: {[j.id for j in dp_sched]}")