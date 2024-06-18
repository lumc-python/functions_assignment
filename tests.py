import pytest

from ex1_multiplication import multiply_positives
from ex2_function_updates import reverse_negatives
from ex3_palindrome import is_palindrome
from ex4_kmer_counting import unique_substrings, kmer_counts


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ([10, 20], 200),
        ([10], 10),
        ([10, -20], 10),
        ([-10], 1),
        ([], 1),
    ],
)
def test_ex1(test_input, expected_output):
    assert multiply_positives(test_input) == expected_output


@pytest.mark.parametrize(
    "test_input, expected_bool, expected_list",
    [
        ([10, 20], False, [10, 20]),
        ([], False, []),
        ([10, -20], True, [10, 20]),
        ([-0.5, 10, -20], True, [0.5, 10, 20]),
        ([-10], True, [10]),
        ([10], False, [10]),
    ],
)
def test_ex2(test_input, expected_bool, expected_list):
    assert reverse_negatives(test_input) == expected_bool
    assert test_input == expected_list


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("p", True),
        ("", True),
        ("madam", True),
        ("madama", False),
        ("able was I ere I saw elba", True),
        ("Able was I here I saw Elba", False),
        (["a", "a", "a"], True),
        (["a", "a", "b"], False),
        (["a", 1, "b"], False),
        (("a", 1, "a"), True),
    ],
)
def test_ex3(test_input, expected):
    assert is_palindrome(test_input) == expected


@pytest.mark.parametrize(
    "sequence, k, expected",
    [
        ("ACG", 1, {"A", "C", "G"}),
        ("ACG", 3, {"ACG"}),
        ("ACGT", 3, {"ACG", "CGT"}),
        ("ACGT" * 3 + "TTATT" * 5, 3, {"GTT", "TAT", "ATT", "ACG", "TTT", "TAC", "GTA", "CGT", "TTA"}),
        ("ACG", 0, set()),
        ("ACG", 5, set()),
    ],
)
def test_ex3_unique_substrings(sequence, k, expected):
    assert unique_substrings(sequence, k) == expected


@pytest.mark.parametrize(
    "sequence, k, expected",
    [
        ("ACG", 1, {"A": 1, "C": 1, "G": 1}),
        ("ACG", 3, {"ACG": 1}),
        ("ACGT", 3, {"ACG": 1, "CGT": 1}),
        ("ACGT" * 3 + "TTATT" * 5, 3, {'ACG': 3, 'CGT': 3, 'GTA': 2, 'TAC': 2, 'GTT': 1, 'TTT': 9, 'TTA': 5, 'TAT': 5, 'ATT': 5}),
        ("ACG", 0, {}),
        ("ACG", 5, {}),
        ("   ", 1, {" ": 3}),
        ("   ", 2, {"  ": 2}),
    ],
)
def test_ex3_kmer_counts(sequence, k, expected):
    assert kmer_counts(sequence, k) == expected
