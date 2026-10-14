from simpleinterest import simple_interest

def test_SI():
    assert simple_interest(2000, 6, 10) == 1200

def test_SIZero():
    assert simple_interest(10000, 0, 0) == 0