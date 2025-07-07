import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from multiply import multiply

def test_multiply_cycle1():
    assert multiply(1, 1) == 1