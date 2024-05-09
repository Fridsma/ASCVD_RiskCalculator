import streamlit as st

def calculate_ascvd_risk(age, gender, race, total_cholesterol, hdl_cholesterol, systolic_bp, treated_hypertension, diabetes, smoker):
    # ASCVD risk calculation formula
    if gender == "Male":
        coef = [17.1141, 0.9396, 1.1232, 0.9323, 0.5530]
    else:
        coef = [31.7640, 1.1232, 0.9323, 0.5286, 0.6915]
    
    if race == "African American":
        coef[0] += 0.4970
    
    if treated_hypertension:
        coef[1] += 0.6546
    
    if diabetes:
        coef[2] += 0.6229
    
    if smoker:
        coef[3] += 0.1423
    
    ln_score = coef[0] + (coef[1] * age) + (coef[2] * total_cholesterol) + (coef[3] * hdl_cholesterol) + (coef[4] * systolic_bp)
    risk_score = 1 - (0.9533 ** (2.71828183 ** ln_score))
    
    return risk_score

st.title("ASCVD Risk Calculator")

age = st.slider("Age (years)", min_value=40, max_value=79, value=50, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
race = st.selectbox("Race", ["White", "African American"])
total_cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=500, value=200, step=1)
hdl_cholesterol = st.number_input("HDL Cholesterol (mg/dL)", min_value=20, max_value=150, value=50, step=1)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=90, max_value=200, value=120, step=1)
treated_hypertension = st.checkbox("Treated Hypertension")
diabetes = st.checkbox("Diabetes")
smoker = st.checkbox("Smoker")

if st.button("Calculate ASCVD Risk"):
    risk_score = calculate_ascvd_risk(age, gender, race, total_cholesterol, hdl_cholesterol, systolic_bp, treated_hypertension, diabetes, smoker)
    st.write(f"10-Year ASCVD Risk: {risk_score:.2%}")
