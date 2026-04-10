from main import calculate_cmax


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
