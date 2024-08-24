"""Unit test for helper file"""

import unittest
import utils.helper as h


class TestGetDay(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_get_day_mon(self):
        op = h.get_day("2024-08-19")
        self.assertEqual("mon", op, "Test 1: Monday Failed")

    def test_get_day_tue(self):
        op = h.get_day("2024-08-20")
        self.assertEqual("tue", op, "Test 2: Tuesday Failed")

    def test_get_day_wed(self):
        op = h.get_day("2024-08-21")
        self.assertEqual("wed", op, "Test 3: Wednesday Failed")

    def test_get_day_thu(self):
        op = h.get_day("2024-08-22")
        self.assertEqual("thu", op, "Test 4: Thursday Failed")

    def test_get_day_fri(self):
        op = h.get_day("2024-08-23")
        self.assertEqual("fri", op, "Test 5: Friday Failed")

    def test_get_day_sat(self):
        op = h.get_day("2024-08-24")
        self.assertEqual("sat", op, "Test 6: Saturday Failed")

    def test_get_day_sun(self):
        op = h.get_day("2024-08-25")
        self.assertEqual("sun", op, "Test 7: Sunday Failed")


class TestGetWeekType(unittest.TestCase):
    """Test cases for Hepler module"""

    s_date = "2024-01-01"
    s_class = "11H"

    def test_week_a(self):
        """Test cases for Week A"""
        op = h.get_week_type(self.s_date, "2024-01-04")
        self.assertEqual("weekA", op, "Test 1: Failed")

        op = h.get_week_type(self.s_date, "2024-01-07")
        self.assertEqual("weekA", op, "Test 2: Failed")

        op = h.get_week_type(self.s_date, "2024-01-29")
        self.assertEqual("weekA", op, "Test 3: Failed")

        op = h.get_week_type(self.s_date, "2024-02-14")
        self.assertEqual("weekA", op, "Test 4: Failed")

    def test_week_b(self):
        """Test cases for Week B"""
        op = h.get_week_type(self.s_date, "2024-01-08")
        self.assertEqual("weekB", op, "Test 1: Failed")

        op = h.get_week_type(self.s_date, "2024-01-10")
        self.assertEqual("weekB", op, "Test 2: Failed")

        op = h.get_week_type(self.s_date, "2024-01-14")
        self.assertEqual("weekB", op, "Test 3: Failed")

        op = h.get_week_type(self.s_date, "2024-02-05")
        self.assertEqual("weekB", op, "Test 4: Failed")


if __name__ == "__main__":
    unittest.main()
