import numpy as np
import scipy
from scipy.optimize import linprog
np.set_printoptions(precision=4)


def linprog_optimization(cost_matrix: np.ndarray) -> scipy.optimize.OptimizeResult:
    """Takes `cost_matrix` and creates new augmented array
    so it is ready for `scipy.optimize.linprog` optimization

    Args:
        cost_matrix (np.ndarray): matrix of values for varying
        assignments across battlefields

    Returns:
        scipy.optimize.OptimizeResult: results of the `scipy.optimize.linprog` call
    """
    neg_tst_matrix = (cost_matrix).copy() * -1
    neg_identity = -np.identity(cost_matrix.shape[0])
    aug_neg_tst_matrix = np.vstack((neg_tst_matrix, np.ones(neg_tst_matrix.shape[1])))
    aug_neg_identity = np.vstack((neg_identity, np.zeros(neg_identity.shape[1])))

    a_t = np.hstack((aug_neg_tst_matrix, aug_neg_identity))
    b = np.zeros(a_t.T.shape[0])
    c = np.zeros(a_t.T.shape[1])
    result = linprog(c, a_t.T, b)
    return result


def cal_probabilities(vector: np.array) -> np.array:
    """Normalizes values to be between [0-1] and
    ensures sum of values == 1

    Args:
        vector (np.array): Array to be normalized

    Returns:
        np.array: normalized array
    """
    return (vector - vector.min()) / (vector - vector.min()).sum()


def cal_mne(cost_matrix: np.ndarray):
    """Returns the MSNE for a given `cost_matrix` in the 
    colonel blotto game.
    If the call to the `linprog` is unsuccessful this will
    return array of zeros.

    Args:
        cost_matrix (np.ndarray): matrix of values for varying
        assignments across battlefields

    Returns:
        np.array: Probability corresponding to frequency with which
        each assignment should be played
    """
    probs = np.zeros(cost_matrix.shape[0])
    result = linprog_optimization(cost_matrix)
    if result['success']:
        probs = cal_probabilities(result['x'][:-1])
    else:
        print(f'Unable to find MNE for:\n{cost_matrix}')
    return probs


if __name__ == "__main__":
    tst_matrix = np.array([[ -0.5, -0.5,  0.1, -0.6],
                            [  0.2, -0.5,  0.8,  0.1],
                            [ -0.4, -0.4,  0.2, -0.5],
                            [ -0.1, -0.6,  0.6,  0.1],
                            [ -0.8, -0.6, -0.1, -0.6]])
    
    row_player_strategies = cal_mne(tst_matrix)
    column_player_strategies = cal_mne(tst_matrix.T)

    print(f'The row players strategies are as follows:\n{row_player_strategies}')
    print(f'The column players strategies are as follows:\n{column_player_strategies}')
    