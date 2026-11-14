import unittest

from FlamesCalculator import play_flames
from LovePercentage import calculate_love_percentage


class TestCalculators(unittest.TestCase):
    def test_play_flames(self):
        res = play_flames("John", "Jane")
        self.assertIn(
            res, ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        )

    def test_calculate_love_percentage(self):
        pct = calculate_love_percentage("Alice", "Bob")
        self.assertGreaterEqual(pct, 1)
        self.assertLessEqual(pct, 100)
        # Deterministic check
        self.assertEqual(pct, calculate_love_percentage("Alice", "Bob"))


if __name__ == "__main__":
    unittest.main()
