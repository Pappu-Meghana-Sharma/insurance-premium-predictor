import streamlit as st
import requests

# API_URL = "http://backend:8000/predict" 
API_URL ="https://insurance-premium-predictor-bbzf.onrender.com"

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
user_age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "user_age": user_age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        
        result = response.json()
        if response.status_code == 200 and "prediction_category" in result:
            
            #Main Prediction
            prediction = result["prediction_category"]
            st.success(f"Predicted Insurance Premium Category: **{prediction}**")
            
            # Confidence
            if "confidence" in result:
                confidence = result["confidence"]
                st.markdown(
                    f"""
                    <div style="
                        margin-top: 15px;
                        margin-bottom: 20px;
                        font-size: 18px;
                    ">
                        <b>Overall Confidence:</b>
                        <span style="color:#2E86C1; font-weight:600;">
                            {confidence * 100:.2f}%
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # Class probabilities
            if "class_probabilities" in result:
                probs = result["class_probabilities"]

                st.markdown("<b>Category-wise Probability</b>", unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown(
                        f"""
                        <div style="text-align:center; font-size:16px;">
                            <b>Low</b><br>
                            <span style="color:#27AE60; font-weight:600;">
                                {probs.get("Low", 0) * 100:.2f}%
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:
                    st.markdown(
                        f"""
                        <div style="text-align:center; font-size:16px;">
                            <b>Medium</b><br>
                            <span style="color:#F39C12; font-weight:600;">
                                {probs.get("Medium", 0) * 100:.2f}%
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col3:
                    st.markdown(
                        f"""
                        <div style="text-align:center; font-size:16px;">
                            <b>High</b><br>
                            <span style="color:#C0392B; font-weight:600;">
                                {probs.get("High", 0) * 100:.2f}%
                            </span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:
            st.error(f"API Error: {response.status_code}-{response.text}")
            st.write(result)
        

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running.")
        
        