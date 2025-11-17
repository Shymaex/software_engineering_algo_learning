from tasks.data_stuctures.bracket_sequence.solution import check_brackets

def test():
    """
    Tests that 'check_brackets' detects correсt and incorrect bracket sequences 
    """
    print("Tests started")
    assert check_brackets("{(}") is False
    assert check_brackets("[]]()({})") is False
    assert check_brackets("[]({[]})") is True
    assert check_brackets("(((({})){})[])") is True
    assert check_brackets("") is True
    assert check_brackets("[[[(){()}]]") is False
    print("Tests were successful")

test()