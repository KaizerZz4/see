import sys, os, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import add, describe


class SmokeTests(unittest.TestCase):
    def test_add(self):
        # BREAK THIS LINE (== 5) on injection day to force a red CI check.
        self.assertEqual(add(2, 2), 5)

    def test_describe(self):
        self.assertEqual(describe(4), "even")
        self.assertEqual(describe(3), "odd")


if __name__ == "__main__":
    unittest.main()
