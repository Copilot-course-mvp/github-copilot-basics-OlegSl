import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step04_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()


class TestSanitizeTags(unittest.TestCase):
    def test_lowercase(self):
        self.assertEqual(
            exercise.sanitize_tags(["FOO", "Bar", "BaZ", "MixedCASE", "lowerCASE"]),
            ["foo", "bar", "baz", "mixedcase", "lowercase"],
        )

    def test_trim_whitespace(self):
        self.assertEqual(
            exercise.sanitize_tags(["  foo  ", " bar", "baz  ","  MixedCASE  ", "  lowercase "]),
            ["foo", "bar", "baz", "mixedcase", "lowercase"],
        )

    def test_remove_non_alphanumeric_chars_except_hyphen(self):
        self.assertEqual(
            exercise.sanitize_tags(["C++", "Python!", "good-tag", "bad_tag"]),
            ["c", "python", "good-tag", "badtag"],
        )
        self.assertEqual(
            exercise.sanitize_tags(["Hello@World", "space bar", "keep-hyphen"]),
            ["helloworld", "spacebar", "keep-hyphen"],
        )

    def test_punctuation_is_removed(self):
        self.assertEqual(
            exercise.sanitize_tags(["Hello, World!", "tag?name", "end."]),
            ["helloworld", "tagname", "end"],
        )

    def test_remove_empty_tags_after_cleanup(self):
        self.assertEqual(exercise.sanitize_tags(["!!!", "   ", "#@$^&*"]), [])
        self.assertEqual(
            exercise.sanitize_tags(["  -  ", "@@@foo@@@", "   BAR   "]),
            ["-", "foo", "bar"],
        )

    def test_deduplicate_preserves_first_seen_order(self):
        self.assertEqual(
            exercise.sanitize_tags(["foo", " Foo ", "FOO", "bar", "Bar"]),
            ["foo", "bar"],
        )
        self.assertEqual(
            exercise.sanitize_tags(["a-b", "A-B", "a_b", "a b"]),
            ["a-b", "ab"],
        )

    def test_edge_cases_and_empty_input(self):
        self.assertEqual(exercise.sanitize_tags([]), [])
        self.assertEqual(
            exercise.sanitize_tags(["  ", "///", "__"]),
            [],
        )


if __name__ == "__main__":
    unittest.main()
