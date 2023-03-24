
from itertools import permutations, product, combinations_with_replacement


def create_assignment_permutation(n_soldiers: int, m_groups: int) -> list[tuple]:
    """This function creates a sorted list of possible assignments
    based on the `n_soldiers` and `m_groups`

    Args:
        n_soldiers (int): number of soldiers 
        m_groups (int): number of groups/fronts

    Returns:
        list[tuple]: sorted list of possible assignments per front
    """

    perm = permutations(range(n_soldiers))
    bounds = combinations_with_replacement(range(n_soldiers+1), m_groups-1)

    comb = set()
    for p,b in product(perm, bounds):
        b = (0,)+b+(n_soldiers+1,)
        L = [p[b[i]:b[i+1]] for i in range(m_groups)]
        assignments = [len(i) for i in L]
        comb.add(tuple(assignments))

    return sorted(comb)


if __name__ == "__main__":
    colonel_a = 3
    colonel_b = 5
    groups = 3

    # print('starting')
    # print(create_assignment_permutation(colonel_a, groups))
    # print('starting')
    # create_assignment_permutation(colonel_b, groups)
    for i in range(5, 8):
        for j in range(3, 6):
            print(f"Creating assignments for {i} troops and {j} fronts")
            assignments = create_assignment_permutation(i, j)
            print(f"Total assignments is: {len(assignments)}")
            print(assignments)
