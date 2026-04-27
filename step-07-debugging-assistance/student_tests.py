import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step07_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()


class TestSummarizeResponseTimes(unittest.TestCase):
    def test_empty_list(self):
        data = exercise.summarize_response_times([])
        self.assertEqual(data, {"min": 0.0, "max": 0.0, "avg": 0.0})

    def test_single_value(self):
        data = exercise.summarize_response_times([42])
        self.assertEqual(data, {"min": 42.0, "max": 42.0, "avg": 42.0})

    def test_filters_zero_values(self):
        data = exercise.summarize_response_times([0, 10, 20, 0])
        self.assertEqual(data, {"min": 10.0, "max": 20.0, "avg": 15.0})

    def test_all_negative_values(self):
        data = exercise.summarize_response_times([-5, -10, -2])
        self.assertEqual(data, {"min": 0.0, "max": 0.0, "avg": 0.0})

    def test_decimal_average(self):
        data = exercise.summarize_response_times([1, 2, 3])
        self.assertAlmostEqual(data["avg"], 2.0)
        self.assertEqual(data["min"], 1.0)
        self.assertEqual(data["max"], 3.0)

    def test_with_mixed_values(self):
        data = exercise.summarize_response_times([50, -10, 75, 0, 25, -3])
        self.assertEqual(data, {"min": 25.0, "max": 75.0, "avg": 50.0})

    def test_all_same_positive_values(self):
        data = exercise.summarize_response_times([5, 5, 5, 5])
        self.assertEqual(data, {"min": 5.0, "max": 5.0, "avg": 5.0})

    def test_summary_normal(self):
        data = exercise.summarize_response_times([120, 80, 100])
        self.assertEqual(data, {"min": 80.0, "max": 120.0, "avg": 100.0})

    def test_ignores_negative_and_handles_empty(self):
        data = exercise.summarize_response_times([-1, -9])
        self.assertEqual(data, {"min": 0.0, "max": 0.0, "avg": 0.0})


if __name__ == "__main__":
    unittest.main()
