import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

from assignment_permutations import create_assignment_permutation


def calculate_cost(assignment_a: list, assignment_b: list, weights: list=None) -> float:
    """
    Calculates the cost of two assignments based on their relative values and weights.

    Args:
        assignment_a (list): A list of values representing assignment A.
        assignment_b (list): A list of values representing assignment B.
        weights (list, optional): A list of weights for each value. If not provided,
            weights default to None.

    Returns:
        float: The final calculated score as a float value.
    """

    scores = []
    for i, _ in enumerate(assignment_a):
        score = 0
        if assignment_a[i] > assignment_b[i]:
            score = 1
        elif assignment_b[i] > assignment_a[i]:
            score = -1 

        score = score * weights[i] if weights != None else score

        scores.append(score)

    final_score =np.sum(np.array(scores))
    return final_score


def create_assignment_matrix(colonel_a_soldiers: list, colonel_b_soldiers: list , weights: list) -> np.ndarray:
    """
    Creates a cost matrix for all possible assignments of soldiers from two colonels.

    Args:
        colonel_a_soldiers (list): A list of soldiers under Colonel A.
        colonel_b_soldiers (list): A list of soldiers under Colonel B.
        weights (list): A list of weights for each value.

    Returns:
        numpy.ndarray: A cost matrix of shape (m, n), where m is the number of
        possible assignments for Colonel A and n is the number of possible assignments
        for Colonel B.
    """

    groups = 1 if weights == None else len(weights)

    colonel_a_assign = create_assignment_permutation(colonel_a_soldiers, groups)
    print(f"Colonel A has {len(colonel_a_assign)} potential assignments")
    print(f"Colonel A assignments are \n{colonel_a_assign}")

    colonel_b_assign = create_assignment_permutation(colonel_b_soldiers, groups)
    print(f"Colonel B has {len(colonel_b_assign)} potential assignments")
    print(f"Colonel B assignments are \n{colonel_b_assign}")

    cost_matrix = np.array([[0] * len(colonel_b_assign)] * len(colonel_a_assign), np.float16)

    for i, a in enumerate(colonel_a_assign):
        for j, b in enumerate(colonel_b_assign):
            cost_matrix[i][j] = calculate_cost(colonel_a_assign[i], colonel_b_assign[j], weights)

    print(f"The cost matrix for Colonel A and B is:")
    print(cost_matrix)
    return cost_matrix


if __name__ == "__main__":
    colonel_a = 3
    colonel_b = 3
    groups = [0.3, 0.7]
    # groups = np.ones((2)).tolist()
    print("Weights over battlefields:")
    print(groups)
    # groups = None
    cost_matrix = create_assignment_matrix(colonel_a, colonel_b, groups)
    print("")
