from datetime import datetime as dt
import streamlit as st

import utils.helper as h

st.title("CCHS Timetable Organiser")

class_name = st.text_input("Enter Class name:", value="11H", max_chars=3)

date_input = st.date_input("Select the date:")
i_date = dt.strptime(str(date_input), "%Y-%m-%d")

if i_date.weekday() >= 5:
    st.write("It's a weekend")
else:
    timet: dict = h.get_timetable(class_name, str(date_input))
    st.write(timet)
