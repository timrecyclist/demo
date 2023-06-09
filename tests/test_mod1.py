import unittest
import demo.mod1 as d


class TestDemo(unittest.TestCase):
    d.demo()

    def setUp(self):
        self.x1 = 100
        self.x2 = 50
        self.x3 = 4.5
        self.x4 = 1.2

    def test_adder(self):
        result = self.x1 + self.x2
        self.assertEqual(result, 150)

        result = self.x3 + self.x4
        self.assertAlmostEqual(result, 5.7)

    def test_percent_change(self):
        result = d.percent_change(self.x2, self.x1)
        self.assertEqual(result, "50%")

        result = d.percent_change(self.x1, self.x2)
        self.assertEqual(result, "-100%")


if __name__ == "__main__":
    # For when you want to see immediately the first failure
    # unittest.main(failfast=True)

    # Runs all tests before outputting what failed
    unittest.main()
