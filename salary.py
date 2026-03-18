import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("ln.pkl", "rb"))

st.title("🎓 Salary Prediction App")

st.write("Enter candidate details below:")

# ---- MAPPINGS (IMPORTANT: must match training encoding) ----
gender_map = {"Male": 1, "Female": 2 , 'Other' : 3}

city_tier_map = {"Tier 1": 1, "Tier 2": 2, "Tier 3": 3}

board_map = { "State": 1 , 'CBSE' : 2 , 'ICSE' : 3}

hsc_stream_map = {"Science": 1, "Commerce": 2, "Arts": 3}

degree_field_map = {
    "Engineering": 1,
    "Business" : 2,
    "Science": 3,
    "Other": 4,
    "Arts": 5
}

# ---- UI LAYOUT ----
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", list(gender_map.keys()))
    age = st.number_input("Age", 18, 60)

    city_tier = st.selectbox("City Tier", list(city_tier_map.keys()))
    ssc_percentage = st.number_input("SSC Percentage")

    ssc_board = st.selectbox("SSC Board", list(board_map.keys()))
    hsc_percentage = st.number_input("HSC Percentage")
    hsc_board = st.selectbox("HSC Board", list(board_map.keys()))

    hsc_stream = st.selectbox("HSC Stream", list(hsc_stream_map.keys()))

with col2:
    degree_percentage = st.number_input("Degree Percentage")

    degree_field = st.selectbox("Degree Field", list(degree_field_map.keys()))
    mba_percentage = st.number_input("MBA Percentage")

    internships_count = st.number_input("Internships Count" , 0,5)
    projects_count = st.number_input("Projects Count" , 0,10)
    certifications_count = st.number_input("Certifications Count" , 0,8)

    technical_skills_score = st.number_input("Technical Skills Score" , 1,10)
    soft_skills_score = st.number_input("Soft Skills Score" , 1,10)

with col3:
    aptitude_score = st.number_input("Aptitude Score" , 1,100) 
    communication_score = st.number_input("Communication Score" , 1,10)

    work_experience_months = st.number_input("Work Experience (Months)" , 0,36)

    leadership_roles = st.number_input("Leadership Roles" , 0,5)
    extracurricular_activities = st.number_input("Extracurricular Activities" , 0,10)

    backlogs = st.number_input("Backlogs" , 0,10)

# ---- PREDICTION ----
if st.button("Predict Salary"):

    input_data = np.array([[
        gender_map[gender],
        age,
        city_tier_map[city_tier],
        ssc_percentage,
        board_map[ssc_board],
        hsc_percentage,
        board_map[hsc_board],
        hsc_stream_map[hsc_stream],
        degree_percentage,
        degree_field_map[degree_field],
        mba_percentage,
        internships_count,
        projects_count,
        certifications_count,
        technical_skills_score,
        soft_skills_score,
        aptitude_score,
        communication_score,
        work_experience_months,
        leadership_roles,
        extracurricular_activities,
        backlogs
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Predicted Salary: {prediction:.2f} lakhs per annum")