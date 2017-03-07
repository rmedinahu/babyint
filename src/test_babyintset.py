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
    bset = BabyIntegerSet([1, 3, 5, 7])
    with pytest.raises(KeyError):
        bset.remove(11)

def test_get():
    assert 0 != 0

def test_clear():
    assert 0 != 0

def test_size():
    assert 0 != 0

def test_sum_all():
    assert 0 != 0

def test_factorial(): # JTMedina
    bset = BabyIntegerSet([1, 3, 5, 7])
    assert bset.product_all() == 105

def test_get_min():
    assert 0 != 0

def test_get_max():
    assert 0 != 0

def test_sortme():
    assert 0 != 0

def test_remove_seq():
    assert 0 != 0

def test_remove_all_odds():
    bset = BabyIntegerSet([1, 3, 5, 3])
    bset.remove_all_odds
    assert len(bset.dump_data()) == 0
