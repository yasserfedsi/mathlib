import pytest
from mathlib import Vector

@pytest.fixture
def v1():
    return Vector([1.0, 2.0, 3.0])

@pytest.fixture
def v2():
    return Vector([4.0, 5.0, 6.0])

def test_vector_creation(v1):
    assert repr(v1) == "[1.0, 2.0, 3.0]"

def test_vector_add(v1, v2):
    result = v1.add(v2)
    assert repr(result) == "[5.0, 7.0, 9.0]"

def test_vector_add_oprator(v1, v2):
    result = v1 + v2
    assert repr(result) == "[5.0, 7.0, 9.0]"

def test_vector_dot(v1, v2):
    result = v1.dot(v2)
    assert result == 32.0

def test_zero_vector():
    v = Vector([0.0, 0.0, 0.0])
    assert v.dot(v) == 0