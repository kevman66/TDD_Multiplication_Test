import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from multiply import multiply

def test_multiply_cycle1():
    assert multiply(1, 1) == 1

def test_multiply_cycle2():
    assert multiply(2, 2) == 4

def test_multiply_cycle3():
    assert multiply(-1, 1) == -1

def test_multiply_cycle4():
    assert multiply(23, 45) == 1035