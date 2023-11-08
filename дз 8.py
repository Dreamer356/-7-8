import time

def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time
 тести для перевірки її працездатності.

import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class TestExecutionTimeMeasurement(unittest.TestCase):

    def test_execution_time_measurement(self):
        result, execution_time = measure_execution_time(add, 5, 3)
        self.assertEqual(result, 8)
        self.assertGreaterEqual(execution_time, 0)

    def test_execution_time_measurement_with_delay(self):
        result, execution_time = measure_execution_time(subtract, 10, 4)
        self.assertEqual(result, 6)
        self.assertGreaterEqual(execution_time, 0)

if __name__ == '__main__':
    unittest.main()
