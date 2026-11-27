from src.operation import addition , subtraction

#create an function to test the addition function
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

#create an function to test the subtraction function
def test_subtraction():
    assert subtraction(2, 3) == -1
    assert subtraction(0, 0) == 0
    assert subtraction(-1, 1) == -2

