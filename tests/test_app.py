import unittest
from prueba_lib_pyspark import app


class AppTest(unittest.TestCase):
    """Test suite for `App` module"""

    def test_positive_add(self):
        self.assertEqual(app.add(2, 3), 5)

    def test_negative_add(self):
        self.assertEqual(app.add(-1, -2), -3)

    def test_zero_add(self):
        self.assertEqual(app.add(0, 0), 0)
