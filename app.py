from datetime import datetime as dt
import streamlit as st

import utils.helper as h

st.title("CCHS Timetable Organiser")

class_name = st.selectbox("Select your class: ", ("11H", "11G"))
st.write("You have selected:", class_name)

date_input = st.date_input("Select the date:")
i_date = dt.strptime(str(date_input), "%Y-%m-%d")

if i_date.weekday() >= 5:
    st.write("It's a weekend")
else:
    schedule: dict = h.get_timetable(str(class_name), str(date_input))
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
