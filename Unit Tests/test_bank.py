from bank import value

def test_hello_value():
    assert value("hello") == 0

def test_h_value():
    assert value("hey") == 20

def test_other_value():
    assert value("other") == 100

def test_upper_value():
    assert value("Hello") == 0

def test_numbers_value():
    assert value("10") == 100
