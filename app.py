import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AI Nursing Operations Dashboard",
    layout="wide"
)

st.title("🏥 AI Nursing Operations & Clinical Quality Dashboard")

st.caption(
    f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Hospital Overview",
        "Clinical Quality Dashboard",
        "Patient Safety Alerts",
        "Shift Handover",
        "SUS Evaluation",
        "Deployment Plan"
    ]
)

if page == "Hospital Overview":

    st.header("Hospital Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Doctors", 5)
    col2.metric("Nurses", 5)
    col3.metric("Patients", 30)

elif page == "Clinical Quality Dashboard":

    st.header("Clinical Quality Dashboard")

    quality = pd.DataFrame(
        [
            ["Falls Rate",1,"0 per shift"],
            ["Pressure Injuries",0,"0"],
            ["Hand Hygiene",94,"≥90%"],
            ["Medication Errors",2,"0"],
        ],
        columns=["Metric","Current","Target"]
    )

    st.dataframe(quality)

elif page == "Patient Safety Alerts":

    st.header("🚨 Patient Safety Alerts")

    st.error("Bed 01: High Fall Risk")
    st.error("Bed 05: Pressure Injury Risk")

elif page == "Shift Handover":

    st.header("Morning Shift Handover")

    st.success("Dashboard Reviewed During Shift Handover")

elif page == "SUS Evaluation":

    st.header("System Usability Scale")

    score = st.slider(
        "Usability Score",
        0,
        100,
        70
    )

    st.metric(
        "SUS Score",
        score
    )

elif page == "Deployment Plan":

    st.header("Clinical Deployment Plan")

    st.markdown("""
### Location
Ward Nurse Station

### Users
- Staff Nurses
- Charge Nurses
- Nurse Managers
""")
