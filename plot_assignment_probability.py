import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def cal_prob_assignment_per_battlefield(assignments: list[tuple], ms_prob: np.array) -> pd.DateOffset:
    """Calculates the combined probability of assigning `n` troops to a battlefield

    Args:
        assignments (list[tuple]): List showing all possible assign combinations
        ms_prob (np.array): (M)ixed (S)trategy probability, i.e. probability in which strategy should
        be played

    Returns:
        pd.DateOffset: DataFrame illustrating probability of assigning `n` troops to a battlefield
    """
    assignment_df = pd.DataFrame(np.array(assignments))
    battle_field_labels = {f'Battlefield {i}':{} for i in assignment_df}

    for bf in assignment_df:
        for i, assignment in enumerate(assignment_df[bf]):
            if assignment not in battle_field_labels[f'Battlefield {bf}']:
                battle_field_labels[f'Battlefield {bf}'][assignment] = ms_prob[i]
            else:
                battle_field_labels[f'Battlefield {bf}'][assignment] += ms_prob[i]

    return pd.DataFrame(battle_field_labels)


def plot_assignment_prob(plot_data: pd.DataFrame, colonel_name: str, n_troops: int, bf_weights: list, save_fig: bool=False) -> None:
    """Utility function to plot output of `cal_prob_assignment_per_battlefield` 

    Args:
        plot_data (pd.DataFrame): pd.df with probabilities of assigning `n` troops to a battlefield
        colonel_name (str): Name used for title
        n_troops (int): Number of troops used for title
        save_fig (bool, optional): Flag used to indicate if plot should be saved. Defaults to False.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for c in plot_data:
        plt.scatter(np.arange(plot_data[c].size), plot_data[c].array, label=c)
    plt.xticks(np.arange(plot_data[c].size))
    plt.title(f'Weakest Link\nTroop Allocation Probability per Battlefield\nColonel: {colonel_name}, {n_troops} troops, {len(plot_data)} battlefields {bf_weights} weights')
    plt.ylabel('Probability of Assignment $p$')
    plt.xlabel('Number of Assigned Troops $t$')
    ax.legend(loc='upper center')
    if save_fig:
        plt.savefig(f'{colonel_name}_colonel_{n_troops}_troops_{len(plot_data)}_troops.png', bbox_inches='tight')
    else:
        plt.show()
