import pytest
from my_math import iseven

# def test_even_value():
#     assert iseven(4)==True
# def test_odd__value():
#     assert iseven(5)==False
@pytest.mark.parametrize("sam_inp, expec",[(2,True),(3,False),(-4,True),(-1,False)])

def test_value(sam_inp,expec):

    assert iseven(sam_inp)==expec

