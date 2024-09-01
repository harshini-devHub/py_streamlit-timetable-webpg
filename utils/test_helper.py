"""Unit test for helper file"""

import unittest
import helper as h


class TestGetDay(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_get_day_mon(self):
        op = h.get_day("2024-08-19")
        self.assertEqual("Monday", op, "Test 1: Monday Failed")

    def test_get_day_tue(self):
        op = h.get_day("2024-08-20")
        self.assertEqual("Tuesday", op, "Test 2: Tuesday Failed")

    def test_get_day_wed(self):
        op = h.get_day("2024-08-21")
        self.assertEqual("Wednesday", op, "Test 3: Wednesday Failed")

    def test_get_day_thu(self):
        op = h.get_day("2024-08-22")
        self.assertEqual("Thursday", op, "Test 4: Thursday Failed")

    def test_get_day_fri(self):
        op = h.get_day("2024-08-23")
        self.assertEqual("Friday", op, "Test 5: Friday Failed")

    def test_get_day_sat(self):
        op = h.get_day("2024-08-24")
        self.assertEqual("Saturday", op, "Test 6: Saturday Failed")

    def test_get_day_sun(self):
        op = h.get_day("2024-08-25")
        self.assertEqual("Sunday", op, "Test 7: Sunday Failed")


class TestGetWeekType(unittest.TestCase):
    """Test cases for Hepler module"""

    s_date = "2024-01-01"

    def test_week_a(self):
        """Test cases for Week A"""
        op = h.get_week_type(self.s_date, "2024-01-04")
        self.assertEqual("week A", op, "Test 1: Failed")

        op = h.get_week_type(self.s_date, "2024-01-07")
        self.assertEqual("week A", op, "Test 2: Failed")

        op = h.get_week_type(self.s_date, "2024-01-29")
        self.assertEqual("week A", op, "Test 3: Failed")

        op = h.get_week_type(self.s_date, "2024-02-14")
        self.assertEqual("week A", op, "Test 4: Failed")

    def test_week_b(self):
        """Test cases for Week B"""
        op = h.get_week_type(self.s_date, "2024-01-08")
        self.assertEqual("week B", op, "Test 1: Failed")

        op = h.get_week_type(self.s_date, "2024-01-10")
        self.assertEqual("week B", op, "Test 2: Failed")

        op = h.get_week_type(self.s_date, "2024-01-14")
        self.assertEqual("week B", op, "Test 3: Failed")

        op = h.get_week_type(self.s_date, "2024-02-05")
        self.assertEqual("week B", op, "Test 4: Failed")


class TestGetTimetable(unittest.TestCase):
    """Test for timetable function"""

    maxDiff = None

    def test_harshini_weekA_mon(self):
        exp_op = {
            "week": "week A",
            "day": "Monday",
            "startTimes": [
                "08:40",
                "09:10",
                "10:10",
                "10:30",
                "11:35",
                "12:35",
                "13:35",
                "14:40",
            ],
            "durations": [
                "25 mins",
                "60 mins",
                "20 mins",
                "60 mins",
                "60 mins",
                "60 mins",
                "60 mins",
                "60 mins",
            ],
            "subjects": [
                "Registration",
                "Physics",
                "--- Break ---",
                "Maths",
                "Computer Science",
                "--- Lunch ---",
                "Maths",
                "FREE PERIOD",
            ],
        }
        op = h.get_timetable("Harshini", "2024-09-16")
        self.assertDictEqual(exp_op, op)

    def test_harshini_weekA_wed(self):

        exp_op = {
            "week": "week A",
            "day": "Wednesday",
            "startTimes": [
                "08:40",
                "09:10",
                "10:10",
                "10:30",
                "11:35",
                "12:35",
                "13:35",
                "14:40",
            ],
            "durations": [
                "25 mins",
                "60 mins",
                "20 mins",
                "60 mins",
                "60 mins",
                "60 mins",
                "60 mins",
                "60 mins",
            ],
            "subjects": [
                "Registration",
                "Computer Science",
                "--- Break ---",
                "Physics",
                "Maths",
                "--- Lunch ---",
                "Maths",
                "FREE PERIOD",
            ],
        }
        op = h.get_timetable("Harshini", "2024-09-04")
        self.assertDictEqual(exp_op, op)

    def test_harshini_weekB_fri(self):

        exp_op = {
            "week": "week B",
            "day": "Friday",
            "startTimes": [
                "08:40",
                "09:10",
                "10:10",
                "10:30",
                "11:35",
                "12:35",
                "13:35",
                "14:40",
            ],
            "durations": [
                "25 mins",
                "60 mins",
                "20 mins",
                "60 mins",
                "60 mins",
                "60 mins",
                "60 mins",
                "60 mins",
            ],
            "subjects": [
                "Registration",
                "Maths",
                "--- Break ---",
                "Physics",
                "FREE PERIOD",
                "--- Lunch ---",
                "Computer Science",
                "Maths",
            ],
        }
        op = h.get_timetable("Harshini", "2024-09-13")
        self.assertDictEqual(exp_op, op)


if __name__ == "__main__":
    unittest.main()
