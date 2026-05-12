import copy
from generator import generate_instance
from algorithms import schrage_basic, schrage, schrage_pmtn, carlier
from utils import Task, calculate_cmax


def test_calculate_cmax():
    tasks = [Task(1,1,2,5), 
             Task(2,2,3,4),
             Task(3,8,1,6),
             Task(4,7,2,3),
             Task(5,6,3,7),
             Task(6,4,4,1)]
    assert calculate_cmax(tasks) == 21

def test_schrage_both_versions_equal():
    tasks = generate_instance(20, seed=1)
    _, cmax_basic = schrage_basic(tasks)
    _, cmax_queue = schrage(tasks)
    assert cmax_basic == cmax_queue

def test_schrage_pmtn_lower_bound():
    for seed in range(10):
        tasks = generate_instance(20, seed=seed)
        _, cmax = schrage(tasks)
        _, lb = schrage_pmtn(tasks)
        assert lb <= cmax

def test_carlier_improves_or_equals_schrage():
    for seed in range(10):
        tasks = generate_instance(20, seed=seed)
        _, cmax_schrage = schrage(tasks)
        cmax_carlier, _ = carlier(copy.deepcopy(tasks))
        assert cmax_carlier <= cmax_schrage

def test_known_instance():
    tasks = generate_instance(10, seed=1234)
    _, cmax = schrage(tasks)
    assert cmax == 197
    
