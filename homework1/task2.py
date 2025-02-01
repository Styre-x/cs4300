def integers():
    return 2+2

def floats():
    return .1 + .1

def strings():
    return "Hello, " + "World"

def bools():
    return True or False

def test_all():
    assert integers() == 4
    assert floats() == 0.2
    assert strings() == "Hello, World"
    assert bools() == True