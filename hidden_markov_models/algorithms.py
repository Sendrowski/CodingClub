from typing import List, Dict, Iterable

import numpy as np


def forward(
        observations: Iterable[str],
        states: Iterable[str],
        start_prob: Dict[str, float],
        trans_prob: Dict[str, Dict[str, float]],
        emm_prob: Dict[str, Dict[str, float]]
) -> (float, np.ndarray[float]):
    """
    Forward algorithm.

    :param observations: sequence of observations
    :param states: sequence of states
    :param start_prob: dictionary of start probabilities
    :param trans_prob: dictionary of transition probabilities
    :param emm_prob: dictionary of emission probabilities
    :return: probability of the observation sequence and the forward probabilities matrix
    """
    # convert state names to indices for easier access
    state_indices = {state: i for i, state in enumerate(states)}

    # initialize the forward probabilities matrix
    fwd = np.zeros((len(observations), len(states)))

    # initialize the first time step with start probabilities
    for state in states:
        fwd[0][state_indices[state]] = start_prob[state] * emm_prob[state][observations[0]]

    # iterate over each observation (after the first)
    for i in range(1, len(observations)):
        for current in states:
            sum_prob = 0
            for previous in states:
                prob = fwd[i - 1][state_indices[previous]] * trans_prob[previous][current]
                sum_prob += prob
            fwd[i][state_indices[current]] = sum_prob * emm_prob[current][observations[i]]

    # probability of the observation sequence
    return np.sum(fwd[-1]), fwd


def backward(
        observations: Iterable[str],
        states: Iterable[str],
        start_prob: Dict[str, float],
        trans_prob: Dict[str, Dict[str, float]],
        emm_prob: Dict[str, Dict[str, float]]
) -> (float, np.ndarray[float]):
    """
    Backward algorithm.

    :param observations: sequence of observations
    :param states: sequence of states
    :param start_prob: dictionary of start probabilities
    :param trans_prob: dictionary of transition probabilities
    :param emm_prob: dictionary of emission probabilities
    :return: probability of the observation sequence and the backward probabilities matrix
    """
    # convert state names to indices for easier access
    state_indices = {state: i for i, state in enumerate(states)}

    # initialize the backward probabilities matrix
    bwd = np.zeros((len(observations), len(states)))

    # initialize the last time step with probabilities of 1
    bwd[-1][:] = 1

    # iterate over each observation backwards (excluding the last)
    for i in range(len(observations) - 2, -1, -1):
        for curr_state in states:
            sum_prob = 0
            for next_state in states:
                prob = bwd[i + 1][state_indices[next_state]] * trans_prob[curr_state][next_state] * \
                       emm_prob[next_state][observations[i + 1]]
                sum_prob += prob
            bwd[i][state_indices[curr_state]] = sum_prob

    # initial probability of the observation sequence
    p = sum(start_prob[state] * bwd[0][state_indices[state]] * emm_prob[state][observations[0]]
            for state in states)

    return p, bwd


def forward_backward(
        observations: Iterable[str],
        states: Iterable[str],
        start_prob: Dict[str, float],
        trans_prob: Dict[str, Dict[str, float]],
        emm_prob: Dict[str, Dict[str, float]]
) -> List[Dict[str, float]]:
    """
    Forward-backward algorithm.

    :param observations: sequence of observations
    :param states: sequence of states
    :param start_prob: dictionary of start probabilities
    :param trans_prob: dictionary of transition probabilities
    :param emm_prob: dictionary of emission probabilities
    :return: probability of the observation sequence
    """
    p, fwd = forward(observations, states, start_prob, trans_prob, emm_prob)
    _, bwd = backward(observations, states, start_prob, trans_prob, emm_prob)

    # Merging the two parts
    posterior = []
    for i in range(len(observations)):
        posterior.append({state: fwd[i][j] * bwd[i][j] / p for j, state in enumerate(states)})

    return posterior


def posterior_decoding(
        observations: Iterable[str],
        states: Iterable[str],
        start_prob: Dict[str, float],
        trans_prob: Dict[str, Dict[str, float]],
        emm_prob: Dict[str, Dict[str, float]]
) -> List[str]:
    """
    Posterior decoding.

    :param observations: sequence of observations
    :param states: sequence of states
    :param start_prob: dictionary of start probabilities
    :param trans_prob: dictionary of transition probabilities
    :param emm_prob: dictionary of emission probabilities
    :return: sequence of states with the highest posterior probability for each observation
    """
    posterior = forward_backward(observations, states, start_prob, trans_prob, emm_prob)

    return [max(x, key=x.get) for x in posterior]


def viterbi(
        observations: Iterable[str],
        states: Iterable[str],
        start_prob: Dict[str, float],
        trans_prob: Dict[str, Dict[str, float]],
        emm_prob: Dict[str, Dict[str, float]]
) -> (float, List[str]):
    """
    Viterbi algorithm.

    :param observations: sequence of observations
    :param states: sequence of states
    :param start_prob: dictionary of start probabilities
    :param trans_prob: dictionary of transition probabilities
    :param emm_prob: dictionary of emission probabilities
    :return: The probability of the most probable state sequence and the sequence itself
    """
    state_indices = {state: i for i, state in enumerate(states)}

    # initialize the Viterbi probability matrix and path pointers
    viterbi_prob = np.zeros((len(observations), len(states)))
    path_pointers = np.zeros((len(observations), len(states)), dtype=int)

    # initialize the first time step
    for state in states:
        viterbi_prob[0][state_indices[state]] = start_prob[state] * emm_prob[state][observations[0]]

    # iterate over each observation (after the first)
    for i in range(1, len(observations)):
        for curr_state in states:
            max_prob, max_state = max(
                (viterbi_prob[i - 1][state_indices[prev_state]] * trans_prob[prev_state][curr_state], prev_state)
                for prev_state in states
            )
            viterbi_prob[i][state_indices[curr_state]] = max_prob * emm_prob[curr_state][observations[i]]
            path_pointers[i][state_indices[curr_state]] = state_indices[max_state]

    # backtrack to find the most probable path
    last_state = np.argmax(viterbi_prob[-1])
    best_path = [states[last_state]]

    for i in range(len(observations) - 1, 0, -1):
        last_state = path_pointers[i][last_state]
        best_path.insert(0, states[last_state])

    # probability of the most probable path
    max_prob = np.max(viterbi_prob[-1])

    return max_prob, best_path
