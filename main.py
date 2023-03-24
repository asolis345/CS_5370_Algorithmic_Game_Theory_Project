import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

from cost_matrix import create_assignment_matrix
from pessimistic_strategies import (max_min, min_max)


def setup_scenario_one():
    """Setups up simple scenario with colonel a troops = 3,
    colonel b troops = 5,
    2 equally weighted battlefields

    Returns:
        tuple: colonel a troops, colonel b troops, battlefield weights
    """
    colonel_a = 3
    colonel_b = 5
    groups = np.ones((2)).tolist()
    return (colonel_a, colonel_b, groups)    


def setup_scenario_two():
    """Setups up simple scenario with colonel a troops = 3,
    colonel b troops = 5,
    2 un-equally weighted battlefields

    Returns:
        tuple: colonel a troops, colonel b troops, battlefield weights
    """
    colonel_a = 3
    colonel_b = 5
    groups = [0.3, 0.7]
    return (colonel_a, colonel_b, groups)    


def setup_scenario_three():
    """Setups up simple scenario with colonel a troops = 4,
    colonel b troops = 3,
    3 un-equally weighted battlefields

    Returns:
        tuple: colonel a troops, colonel b troops, battlefield weights
    """
    colonel_a = 4
    colonel_b = 3
    groups = [0.1, 0.7, 0.2]
    return (colonel_a, colonel_b, groups)    

def run_scenario(colonel_a: int, colonel_b: int, groups: list[tuple]):
    """Runs complete scenario using pessimistic strategies

    Args:
        colonel_a (int): colonel a number of troops
        colonel_b (int): colonel b number of troops
        groups (list[int]): weights per battlefields
    """
    print("Weights over battlefields:")
    print(groups)
    cost_matrix = create_assignment_matrix(colonel_a, colonel_b, groups)

    action, value = max_min(cost_matrix)
    print(f'Best action for Colonel A player: {action}\tValue of: {value:4.3f}')
    action, value = min_max(cost_matrix)
    print(f'Best action for Colonel B player: {action}\tValue of: {value:4.3f}')
    print("")


if __name__ == "__main__":
    colonel_a, colonel_b, groups = setup_scenario_one()
    run_scenario(colonel_a, colonel_b, groups)

    colonel_a, colonel_b, groups = setup_scenario_two()
    run_scenario(colonel_a, colonel_b, groups)

    colonel_a, colonel_b, groups = setup_scenario_three()
    run_scenario(colonel_a, colonel_b, groups)

    