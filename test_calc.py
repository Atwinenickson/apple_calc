import pytest
import calc

@pytest.fixture(scope='module')

def test_add():
    assert calc.add(7,5) == 12
    assert calc.add(7) == 9
    assert calc.add(7, 3) == 10

def test_subtract():
    assert calc.subtract(7, 5) == 2
    assert calc.subtract(7) == 1
    assert calc.subtract(17, 5) == 12

def test_multiply():
    assert calc.multiply(7, 5) == 35
    assert calc.multiply(7) == 21
    assert calc.multiply(10, 5) == 50

def test_divide():
    assert calc.divide(6, 2) == 3
    assert calc.divide(16) == 4
    assert calc.divide(10, 5) == 2
