import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_for_zero(self,):
        """Test num_buses with 0 people."""

        act = a1.num_buses(0)
        exp = 0
        self.assertEqual(act, exp)
        
    def test_for_one(self,):
        """Test num_buses with 1 people."""

        act = a1.num_buses(1)
        exp = 1
        self.assertEqual(act, exp)
        
    def test_for_fifty(self):
        """Test num_buses with 50 peoples."""

        act = a1.num_buses(50)
        exp = 1
        self.assertEqual(act, exp)

    def test_for_larger(self):
        """Test num_buses with 101 peoples."""
       
        act = a1.num_buses(101)
        exp = 3
        self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main(exit=False)
