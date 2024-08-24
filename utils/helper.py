# this module reads the timetable from the file and returns the week type and subjects for the date

import json
from datetime import datetime as dt


def get_timetable(s_class: str, ip_date: str) -> dict:
    """this sub-routine takes user's class and date and outputs week and subjects for the day
    Args:
        s_class (str): Students class name
        date (str): date (YYYY-MM-DD) for which the timetable is needed.

    Returns:
        dict: Week type and subjects {"week": "Week A", "day":"mon", "subjects": ["Maths", "Sci", "PE", "Lunch", "English", "Physics"]}
    """
    output: dict = {}

    # Read the timetable from the file
    timetable: dict
    with open("timetable.json", "r", encoding="utf-8") as f:
        timetable = json.load(f)

    # Find out what the week type is
    week_type: str = get_week_type(
        start_date=timetable["weekStart"], input_date=ip_date
    )

    # Find out the day of the week
    day: str = get_day(input_date=ip_date)

    # Create output dict
    output["week"] = week_type
    output["day"] = day
    output["subjects"] = timetable[s_class][week_type][day]

    return output


def get_day(input_date: str) -> str:
    """Method to return weekday name

    Args:
        input_date (str): date string in YYYY-MM-DD format

    Returns:
        str: 3 character weekday name. Eg: "mon"
    """
    output: str = ""

    i_date = dt.strptime(input_date, "%Y-%m-%d")
    day: int = i_date.weekday()
    days_list: list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    output: str = days_list[day]

    return output


def get_week_type(start_date: str, input_date: str) -> str:
    """
    find the difference in days and then divide by 14.

    if remainder is less than 7 or 0 then week type is weekA else it is weekB

    """
    output: str = ""

    s_date = dt.strptime(start_date, "%Y-%m-%d")
    i_date = dt.strptime(input_date, "%Y-%m-%d")
    days_difference = (i_date - s_date).days

    # print(days_difference)

    remainder = days_difference % 14
    output = "weekA" if remainder < 7 else "weekB"

    return output
