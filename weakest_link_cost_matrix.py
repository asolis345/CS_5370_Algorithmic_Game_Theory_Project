import numpy as np

def calculate_weakest_link_cost_matrix(cost_matrix: np.ndarray) -> np.ndarray:
    """Creates a cost matrix for the "weakest link" strategy.
    This type of games has the player as loosing the entire scenario if they
    are beat on any battlefield

    Args:
        cost_matrix (np.ndarray): Original cost matrix 

    Returns:
        np.ndarray: Modified cost matrix
    """
    new_cost_matrix = []
    for r in cost_matrix:
        if np.any(r<0):
            r = np.ones(r.shape)*-1
        else:
            r = np.ones(r.shape)
        new_cost_matrix.append(r)
        
    return np.array(new_cost_matrix)
