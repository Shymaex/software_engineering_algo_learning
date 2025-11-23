def check_brackets(string):
    """
    Check is a string of brackets correct
    Args:
        string: string of brackets (){}[]
    Returns:
        bool: True/False (Correct/Incorrect)
    """
    brackets = []
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    for char in string:
        if char in open_brackets:
            brackets.append(char)
        elif char in close_brackets:
            if len(brackets) <= 0:
                return False
            if brackets[-1] == open_brackets[close_brackets.index(char)]:
                brackets.pop()
            else:
                return False
    if len(brackets) == 0:
        return True
    else:
        return False