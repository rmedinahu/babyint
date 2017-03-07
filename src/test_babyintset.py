# test_babyintset.py
# Demonstrates unit testing using the pytest module.
# pytest must be installed through pip.

import pytest

from baby_int_set import BabyIntegerSet, UnsupportedTypeError

def test_init():
    bset = BabyIntegerSet()
    assert len(bset.dump_data()) == 0

def test_init_empty():
    bset = BabyIntegerSet([1, 3, 5, 3])
    assert len(bset.dump_data()) == 3

def test_add_exception():
    bset = BabyIntegerSet()
    with pytest.raises(UnsupportedTypeError) as exeinfo:
        bset.add('9')
    assert 'not a valid integer' in str(exeinfo)

def test_add():
    bset = BabyIntegerSet([1, 3, 5, 3])
    bset.add(3)
    assert len(bset.dump_data()) == 3

def test_addSeq():
    bset = BabyIntegerSet([1, 3, 5, 3])
    bset.addSeq([1, 3, 5, 7])
    assert len(bset.dump_data()) == 4

def test_remove():
    bset = BabyIntegerSet([1, 3, 5, 3])
    assert bset.remove(3) == [1, 5]

def test_get():
    baby = BabyIntegerSet([2,4,4])
    with pytest.raises(KeyError):
         baby.get(1)
    baby.get(2)
        
def test_clear():
    bset = BabyIntegerSet([1, 4, 7])
    bset.clear()
    assert len(bset.dump_data()) == 0

def test_size():
    bset = BabyIntegerSet([1, 3, 5, 2])
    bset.size()
    assert len(bset.dump_data()) == 4

def test_sum_all():
    assert 0 != 0

def test_factorial(): # JTMedina
    bset = BabyIntegerSet([1, 3, 5, 7])
    assert bset.product_all() == 105

def test_get_min():
    bset = BabyIntegerSet([3, 2, 4, 5, 6, 7])
    assert bset.get_min() == 2

def test_get_max():
    bset = BabyIntegerSet([1, 3, 5, 4])
    assert(bset.get_max()) == 5

def test_sortme():
    bset = BabyIntegerSet([5, 7, 1, 3])
    bset.sortme()
    assert (bset.dump_data()) == [1, 3, 5, 7]

def test_remove_seq():
    assert 0 != 0

def test_remove_all_odds():
<<<<<<< HEAD
    bset = BabyIntegerSet([1, 3, 5, 3])
    bset.remove_all_odds
    assert len(bset.dump_data()) == 0
=======
    assert 0 != 0
if __name__ ==  '__main__':
    pytest.main()
>>>>>>> aa18a64f2dea9c18b8a5ab6fcb2cbd047747196e
