from datetime import datetime as dt
import streamlit as st
import json
import utils.helper as h

st.title(":violet[Timetable Organiser]:tulip:")


# Get the student name from the Timetable json and create a list
students: list = []
timetable_json: dict
with open("timetable.json", "r", encoding="utf-8") as f:
    timetable_json = json.load(f)
for s in timetable_json["students"]:
    students.append(s["name"])

# pass that list to the streamlit selectbox
student_name = st.selectbox("Select the student's name: ", students)
st.write("You have selected:", student_name)

date_input = st.date_input("Select the date:")
i_date = dt.strptime(str(date_input), "%Y-%m-%d")

if i_date.weekday() >= 5:
    st.write("It's a weekend")
else:
    schedule: dict = h.get_timetable(str(student_name), str(date_input))
    #    st.write(schedule)

    st.write(
        f"""The chosen date is a {schedule["day"].title()}. This falls in {schedule["week"].title()}.
            \n Below is the timetable: """
    )

    schedule_table: dict = {
        "Start_Times": schedule["startTimes"],
        "Duration": schedule["durations"],
        "Subjects": schedule["subjects"],
    }

    st.table(schedule_table)
