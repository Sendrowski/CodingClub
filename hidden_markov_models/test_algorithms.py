import numpy as np
from hmmlearn import hmm
from unittest import TestCase

from algorithms import forward, backward, forward_backward, posterior_decoding, viterbi


class AlgorithmTestCase(TestCase):
    """
    Test cases for the algorithms module.
    """

    # adapted from https://en.wikipedia.org/wiki/Forward–backward_algorithm
    states = ['Healthy', 'Fever']

    observations = ['normal', 'cold', 'dizzy']

    start_probability = {'Healthy': 0.6, 'Fever': 0.4}

    transition_probability = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6},
    }

    emission_probability = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
    }

    def test_forward(self):
        """
        Test the forward algorithm.
        """
        p_native, m_native = forward(
            self.observations,
            self.states,
            self.start_probability,
            self.transition_probability,
            self.emission_probability
        )

        model = self.get_hmm_model()

        # convert observations to integer index
        obs_idx = np.array([[self.observations.index(x)] for x in ('normal', 'cold', 'dizzy')]).T

        # compute the probability
        p_log_hmm, posteriors_hmm = model.score_samples(obs_idx)
        p_hmm = np.exp(p_log_hmm)

        self.assertTrue(np.isclose(p_native, p_hmm))

    def test_backward(self):
        """
        Test the backward algorithm.
        """
        p_fwd, m_fwd = forward(
            self.observations,
            self.states,
            self.start_probability,
            self.transition_probability,
            self.emission_probability
        )

        p_bwd, m_bwd = backward(
            self.observations,
            self.states,
            self.start_probability,
            self.transition_probability,
            self.emission_probability
        )

        self.assertTrue(np.isclose(p_fwd, p_bwd))

    def get_hmm_model(self) -> hmm.CategoricalHMM:
        """
        Get the HMM model.
        """
        # create HMM instance
        model = hmm.CategoricalHMM(n_components=len(self.states))
        model.startprob_ = [self.start_probability[x] for x in self.states]
        model.transmat_ = [[self.transition_probability[x][y] for y in self.states] for x in self.states]
        model.emissionprob_ = [[self.emission_probability[x][y] for y in self.observations] for x in self.states]

        return model

    def test_forward_backward(self):
        """
        Test the forward-backward algorithm.
        """
        posteriors_native = forward_backward(
            self.observations,
            self.states,
            self.start_probability,
            self.transition_probability,
            self.emission_probability
        )

        posteriors_native_array = np.array([[p[x] for x in self.states] for p in posteriors_native])

        model = self.get_hmm_model()

        # convert observations to integer index
        obs_idx = np.array([[self.observations.index(x)] for x in ('normal', 'cold', 'dizzy')]).T

        # compute the probability
        _, posteriors_hmm = model.score_samples(obs_idx)

        np.testing.assert_array_almost_equal(posteriors_native_array, posteriors_hmm)

    def test_posterior_decoding(self):
        """
        Test the posterior decoding algorithm.
        """
        seq = posterior_decoding(
            self.observations,
            self.states,
            self.start_probability,
            self.transition_probability,
            self.emission_probability
        )

        np.testing.assert_array_equal(seq, ['Healthy', 'Healthy', 'Fever'])

    def test_viterbi(self):
        """
        Test the viterbi algorithm.
        """
        p_native, seq = viterbi(
            self.observations,
            self.states,
            self.start_probability,
            self.transition_probability,
            self.emission_probability
        )

        model = self.get_hmm_model()

        # convert observations to integer index
        obs_idx = np.array([[self.observations.index(x)] for x in ('normal', 'cold', 'dizzy')]).T

        # compute the probability
        p_log_hmm, seq_hmm = model.decode(obs_idx, algorithm='viterbi')
        p_hmm = np.exp(p_log_hmm)

        self.assertTrue(np.isclose(p_native, p_hmm))
        self.assertTrue(np.array_equal(seq, [self.states[s] for s in seq_hmm]))