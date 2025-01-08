import unittest
from quadratic_solver import solution

class TestQuadraticSolver(unittest.TestCase):
    def test_two_roots(self):
        self.assertEqual(solution(1, 6, 5), (-5, -1))
    
    def test_one_root(self):
        self.assertEqual(solution(1, 4, 4), (-2,))
    
    def test_no_roots(self):
        self.assertIsNone(solution(1, 6, 45))
    
    def test_invalid_a(self):
        with self.assertRaises(ValueError):
            solution(0, 6, 5)

if __name__ == "__main__":
    unittest.main()
