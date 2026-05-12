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
├── lab2_rpq/
│   ├── generator.py    # generate_instance
│   ├── algorithms.py   # schrage_basic, schrage, schrage_pmtn, carlier
│   ├── utils.py        # Task, calculate_cmax, print_schedule
│   ├── main.py
│   └── test.py
│
├── lab3_flow_shop/
│   ├── algorithms.py   # johnson_basic, johnson_extended, brute_force, branch_and_bound
│   ├── utils.py        # generate_instancen, calculate_cmax, print_schedule
│   ├── main.py
│   └── test.py
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
  
