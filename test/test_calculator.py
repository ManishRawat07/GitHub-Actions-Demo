from src.calculator import add,sub,mul,div,power,sqrt

def test_add():
    assert add(4,5)==(9)
    assert add(100,200)==(300)
    assert add(45.9,56)==(101.9) 

def test_sub():
    assert sub(100,29)==(71)
    assert sub(456,234)==(222)
    assert sub(34,5)==(29)

def test_mul():
    assert mul(2,10)==(20)
    assert mul(20982.2, 23.56)==(494340.632)
    assert mul(34,23)==(782)

def test_div():
    assert div(2,4)==(0.5)
    assert div(560,34)==(16.4705882353)
    assert div(123,335)==(0.3671641791)

def test_power():
    assert power(2,4)==(16)
    assert power(4,10)==(1048576)
    assert power(10,4)==(10000)

def test_sqrt():
    assert sqrt(2)==(1.4142135623730951)
    assert sqrt(56)==(7.48331477355)
    assert sqrt(234)==(15.297058540778355)