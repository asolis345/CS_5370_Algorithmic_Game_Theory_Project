import sys
import numpy as np
np.set_printoptions(precision=4)

from cost_matrix import (create_assignment_matrix, create_assignment_permutation)
from pessimistic_strategies import (max_min, min_max)
from mixed_nash_equilibra import cal_mne
from plot_assignment_probability import (cal_prob_assignment_per_battlefield, plot_assignment_prob)
from weakest_link_cost_matrix import calculate_weakest_link_cost_matrix


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
    colonel_a = 3
    colonel_b = 2
    groups = [0.1, 0.7, 0.2]
    return (colonel_a, colonel_b, groups)    


def run_min_max_scenario(colonel_a: int, colonel_b: int, groups: list[tuple]):
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


def run_mneq_scenario(colonel_a: int, colonel_b: int, groups: list[tuple]):
    """Runs complete scenario using pessimistic strategies

    Args:
        colonel_a (int): colonel a number of troops
        colonel_b (int): colonel b number of troops
        groups (list[int]): weights per battlefields
    """
    print("Weights over battlefields:")
    print(groups)
    cost_matrix = create_assignment_matrix(colonel_a, colonel_b, groups)

    row_colonel_strategies = cal_mne(cost_matrix)
    column_colonel_strategies = cal_mne(cost_matrix.T)
    
    print(f'The A colonel strategies are as follows:\n{row_colonel_strategies}')
    print(f'The B colonel strategies are as follows:\n{column_colonel_strategies}')

    print(f'The A colonel best option is to play:\n{np.argmax(row_colonel_strategies)} with probability {np.max(row_colonel_strategies)}')
    print(f'The B colonel best option is to play:\n{np.argmax(column_colonel_strategies)} with probability {np.max(column_colonel_strategies)}')

    return (row_colonel_strategies, column_colonel_strategies)


def run_weakest_link_scenario(colonel_a: int, colonel_b: int, groups: list[tuple]):
    print("Weights over battlefields:")
    print(groups)
    cost_matrix = create_assignment_matrix(colonel_a, colonel_b, groups)

    row_cost_matrix = calculate_weakest_link_cost_matrix(cost_matrix)
    column_cost_matrix = calculate_weakest_link_cost_matrix(cost_matrix.T)

    row_colonel_strategies = cal_mne(row_cost_matrix)
    column_colonel_strategies = cal_mne(column_cost_matrix)

    print(f'The A colonel strategies are as follows:\n{row_colonel_strategies}')
    print(f'The B colonel strategies are as follows:\n{column_colonel_strategies}')

    return (row_colonel_strategies, column_colonel_strategies)


if __name__ == "__main__":
    ### Scenario Setup ###
    # colonel_a, colonel_b, groups = setup_scenario_one()
    # colonel_a, colonel_b, groups = setup_scenario_two()
    colonel_a, colonel_b, groups = setup_scenario_three()
    colonel_a_options = create_assignment_permutation(colonel_a, len(groups))
    colonel_b_options = create_assignment_permutation(colonel_b, len(groups))

    ### Run Strategy ###
    # run_min_max_scenario(colonel_a, colonel_b, groups)
    r_strategies, c_strategies = run_mneq_scenario(colonel_a, colonel_b, groups)
    r_strategies, c_strategies = run_weakest_link_scenario(colonel_a, colonel_b, groups)

    colonel_a_df = cal_prob_assignment_per_battlefield(colonel_a_options, r_strategies)
    plot_assignment_prob(colonel_a_df, 'Row', colonel_a, groups, True)
    
    colonel_b_df = cal_prob_assignment_per_battlefield(colonel_b_options, c_strategies)
    plot_assignment_prob(colonel_b_df, 'Column', colonel_b, groups, True)
