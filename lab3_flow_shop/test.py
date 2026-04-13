import pytest

from utils import calculate_cmax, generate_instancen
from algorithms import johnson_basic, johnson_extended, brute_force, branch_and_bound


def test_calculate_cmax():
    p = [
        [4, 4, 1, 5],  # Machine 1 (p1j)
        [1, 3, 2, 1],  # Machine 2 (p2j)
        [4, 3, 3, 3],  # Machine 3 (p3j)
    ]
    pi = [0, 1, 2, 3]
    n = 4
    m = 3
    assert calculate_cmax(p, pi, n, m) == 20

def test_johnson_basic():
    p = [[1, 16, 19, 10], [14, 42, 5, 15]]
    n = 4
    pi = johnson_basic(p, n)
    assert calculate_cmax(p, pi, n, 2) == 77
    
def test_johnson_extended():
    p = [[4,4,1,5],[1,3,2,1],[4,3,3,3]]
    n = 4
    pi = johnson_extended(p, n)
    assert calculate_cmax(p, pi, n, 3) == 18
    
def test_bnb_optimal():
    p = [[4,4,1,5],[1,3,2,1],[4,3,3,3]]
    n, m = 4, 3
    _, cmax_bf = brute_force(p, n, m)
    _, cmax_bnb = branch_and_bound(p, n, m)
    assert cmax_bnb == cmax_bf
    
@pytest.mark.parametrize("n,m,seed", [
    (4, 2, 42),
    (5, 3, 123),
    (6, 4, 999),
])
def test_bnb_not_worse_than_bf(n, m, seed):
    p = generate_instancen(seed, n, m)
    _, cmax_bf = brute_force(p, n, m)
    _, cmax_bnb = branch_and_bound(p, n, m)
    assert cmax_bnb == cmax_bf