import unittest
import demo.mod2 as d


class TestDemo(unittest.TestCase):
    d.demo()

    def setUp(self):
        self.x1 = "test1"
        self.x2 = "test2"
        self.sep1 = ", "

    def test_adder(self):
        result = d.concat(self.x1, self.x2)
        self.assertEqual(result, "test1 test2")

        result = d.concat(self.x1, self.x2, self.sep1)
        self.assertAlmostEqual(result, "test1, test2")


if __name__ == "__main__":
    # For when you want to see immediately the first failure
    # unittest.main(failfast=True)

    # Runs all tests before outputting what failed
    unittest.main()
