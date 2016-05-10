import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
        def test_is_eleven_prime(self):
                self.assertTrue(is_prime(11))

if __name__ =='__main__':
        unittest.main()

