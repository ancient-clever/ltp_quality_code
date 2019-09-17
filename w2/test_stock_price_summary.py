import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_empty_list(self,):
        """Test stock_price_summary with empty list."""

        act = a1.stock_price_summary([])
        exp = (0,0)
        self.assertEqual(act, exp)
        
    def test_one_zero(self,):
        """Test stock_price_summary with list of one zero."""

        act = a1.stock_price_summary([0,])
        exp = (0,0)
        self.assertEqual(act, exp)
        
    def test_one_gain(self,):
        """Test stock_price_summary with list of one gain."""

        act = a1.stock_price_summary([1,])
        exp = (1,0)
        self.assertEqual(act, exp)
        
    def test_one_loss(self,):
        """Test stock_price_summary with list of one loss."""

        act = a1.stock_price_summary([-1,])
        exp = (0,-1)
        self.assertEqual(act, exp)
        
    def test_normal(self,):
        """Test stock_price_summary with normal list."""

        act = a1.stock_price_summary([-1,1,0.5,-0.2,0])
        exp = (1.5,-1.2)
        self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main(exit=False)
