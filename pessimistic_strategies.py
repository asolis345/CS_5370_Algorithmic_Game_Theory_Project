import numpy as np

def max_min(cost_matrix) -> tuple:
    """ Finds the maximum minimum value in a cost matrix and returns the index of 
    the row containing it and the value itself.

    Args:
        cost_matrix (numpy.ndarray): A 2D numpy array representing a cost matrix.

    Returns:
        tuple: A tuple containing two values:
            - The index of the row containing the maximum minimum value.
            - The maximum minimum value in the cost matrix.
    """
    min_vals = []

    for row in cost_matrix:
        min_vals.append(np.min(row))
    
    # print(f'Row with max min value: {np.argmax(min_vals)}')
    return (np.argmax(min_vals), np.max(min_vals))


def min_max(cost_matrix) -> tuple:
    """Finds the minimum maximum value in a cost matrix and returns the index of 
    the column containing it and the value itself.

    Args:
        cost_matrix (numpy.ndarray): A 2D numpy array representing a cost matrix.

    Returns:
        tuple: A tuple containing two values:
            - The index of the column containing the minimum maximum value.
            - The minimum maximum value in the cost matrix.
    """
    tmp_matrix = np.array(cost_matrix).T
    max_vals = []
    
    for row in tmp_matrix:
        max_vals.append(np.max(row))

    # print(f'Column with min max value: {np.argmin(max_vals)}')
    return (np.argmin(max_vals), np.min(max_vals))


if __name__ == "__main__":
    
    matrix = [[3, 0],
              [1, 2]]
    matrix = [[1, 3],
              [4, 2]]
    matrix = [[0, 3, 1],
              [4, 1, 2]]
    
    print('Test matrix:')
    for r in matrix:
        print(r)
    
    action, value = max_min(matrix)
    print(f'Best action for ROW player: {action}\t\tValue of: {value:.2f}')
    action, value = min_max(matrix)
    print(f'Best action for COLUMN player: {action}\tValue of: {value:.2f}')
