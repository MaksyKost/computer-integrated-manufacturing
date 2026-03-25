# computer-integrated-manufacturing
Scheduling algorithms for computer-integrated manufacturing - single-machine RPQ, permutation flow shop, branch and bound (Python).

---
 
# Computer Integrated Manufacturing
 
This repository contains lab assignments from the **Computer Integrated Manufacturing** course at Wrocław University of Science and Technology (PWr). Each lab implements classical scheduling algorithms, progressing from introductory single-machine problems through RPQ heuristics to multi-machine flow shop optimization — all in **Python**.
 
---
 
## Labs
 
| # | Topic | Algorithm / Method | Problem Class |
|---|-------|--------------------|---------------|
| [Lab 0](./lab0_intro) | **Introduction to Scheduling** | Sorting-based heuristic | `1\|r_j\|C_max` |
| [Lab 2](./lab2_rpq) | **Single-Machine RPQ — Schrage & Carlier** | Schrage (list & priority queue), Schrage with preemption, Carlier (B&B) | `1\|r_j, q_j\|C_max` · `1\|r_j, q_j, pmtn\|C_max` |
| [Lab 3](./lab3_flow_shop) | **Permutation Flow Shop** | Johnson's algorithm, Brute Force, Branch & Bound | `FP\|\|C_max` |
 
---
 
## Repository Structure
 
```
computer-integrated-manufacturing/
│
├── lab0_intro/                 # Intro — 1|r_j|C_max, sorting heuristic
│   ├── main.py
│   └── generator.py
│
├── lab2_rpq/                   # 1|r_j, q_j|C_max — Schrage & Carlier
│   ├── main.py
│   ├── schrage.py              # Schrage (linear search + priority queue)
│   ├── schrage_pmtn.py         # Schrage with preemption
│   ├── carlier.py              # Carlier's Branch & Bound
│   └── generator.py
│
├── lab3_flow_shop/             # FP||C_max — Johnson, BF, BnB
│   ├── main.py
│   ├── johnson.py              # Johnson's algorithm (m=2, extension m>2)
│   ├── brute_force.py          # Brute Force (permutation tree)
│   ├── branch_and_bound.py     # Branch & Bound with lower bounds (LB0–LB4)
│   └──  generator.py
│
└── README.md
```
 
---
 
## Tech & Tools
 
- **Language:** Python 3.x
- **Data Structures:** Priority queues (`heapq`), permutation trees
- **Visualization:** Gantt chart rendering (`matplotlib`)
- **Version Control:** Git & GitHub
 
---
  
