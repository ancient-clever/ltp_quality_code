import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_zero_k(self):
        """Test swap_k with k equals 0."""

        list_1 = [1, 2, 3, 4, 5, 6]
        k = 0 
        list_1_expected = [1, 2, 3, 4, 5, 6]
        
        a1.swap_k(list_1, k)

        self.assertEqual(list_1, list_1_expected)
 

    def test_one_k(self):
        """Test swap_k with k equals 1."""
        
        list_1 = [1, 2, 3, 4, 5, 6]
        k = 1 
        list_1_expected = [6, 2, 3, 4, 5, 1]
        
        a1.swap_k(list_1, k)

        self.assertEqual(list_1, list_1_expected)

    def test_max_k_even(self):
        """Test swap_k with k equals the max possible value,
        when length of list is even."""
        
        list_1 = [1, 2, 3, 4, 5, 6]
        k = len(list_1)//2
        list_1_expected = [4, 5, 6, 1, 2, 3]

        a1.swap_k(list_1, k)

        self.assertEqual(list_1, list_1_expected)


    def test_max_k_odd(self):
        """Test swap_k with k equals the max possible value,
        when length of list is odd."""
 
        list_2 = [1, 2, 3, 4, 5]
        k = len(list_2)//2
        list_2_expected = [4, 5, 3, 1, 2]

        a1.swap_k(list_2, k)
        
        self.assertEqual(list_2, list_2_expected)


if __name__ == '__main__':
    unittest.main(exit=False)
