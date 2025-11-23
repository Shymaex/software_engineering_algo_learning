import pytest
from tasks.data_stuctures.bracket_sequence.bracket_sequence import check_brackets

def test_excess_open_simple():
    assert check_brackets("{(}") is False
def test_excess_close_complex():
    assert check_brackets("[]]()({})") is False
def test_2_seq_combined():
    assert check_brackets("[]({[]})") is True
def test_complex_correct():
    assert check_brackets("(((({})){})[])") is True
def test_empty_seq():
    assert check_brackets("") is True
def test_excess_open():
    assert check_brackets("[[[(){()}]]") is False