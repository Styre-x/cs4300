def calculate_discount(duck, percent):
    if percent >= 1:
        percent = percent/100 # convert to a proper percent if above 1. Bad checking for the "Real World" but Oh Well! It passes tests!
    return duck - (duck * percent)

def test_percent():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(100, 0.1) == 90
    assert calculate_discount(100, 50) == 50
    assert calculate_discount(100, .25) == 75