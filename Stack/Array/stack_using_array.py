import logging
import unittest
import numpy as np
from typing import List, Any

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class StackArray:
    def __init__(self, value: Any):
        self.array = np.array([value])
        self.length = 1
        self.top = self.array[self.length-1]

    def push(self, value: Any) -> bool:
        try:
            assert np.isnan(self.array[self.length])
        except IndexError:
            new_array = np.full(self.length * 2, np.nan)
            new_array[:self.length] = self.array
            self.array = new_array
            self.array[self.length] = value
        except AssertionError as e:
            logging.debug(e)
            return False
        else:
            self.array[self.length] = value
        finally:
            self.length += 1
        return True
    
    def pop(self) -> Any:
        if self.length == 0:
            return None
        
        temp = self.top
        self.array[self.length - 1] = np.nan
        self.length -= 1
        return temp


def is_equal_array(array_1: np.array, array_2: np.array):
    try:
        if array_1.size == array_2.size:
            np.testing.assert_array_equal(array_1, array_2)
        else:
            array_1_non_nan = [x for x in array_1 if not np.isnan(x)]
            array_2_non_nan = [x for x in array_2 if not np.isnan(x)]
            assert np.all(array_1_non_nan == array_2_non_nan)
    except AssertionError:
        return False
    return True

class Test(unittest.TestCase):    
    def test_push(self):
        s = StackArray(2)
        s.push(1)
        expected = np.array([2, 1])
        actual = s.array
        self.assertTrue(is_equal_array(actual, expected))
    
    def test_pop(self):
        s = StackArray(2)
        s.push(1)
        s.push(2)
        expected = 2
        actual = s.pop()
        self.assertEqual(actual, expected)

        expected = np.array([2, 1])
        actual = s.array
        self.assertTrue(is_equal_array(actual, expected))

if __name__ == '__main__':
    unittest.main()
