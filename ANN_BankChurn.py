import streamlit as st
import numpy as np
from streamlit.source_util import page_icon_and_name
# import matplotlib.pyplot as plt
#from tensorflow.keras.models import load_model
import joblib


st.set_page_config(page_title="Customer Churn Predictor",
                   layout="wide"
                   )
st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #f8fafc, #eef2ff);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1e293b;
    padding-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 30px;
}

div[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    color: white;
    border-radius: 12px;
    height: 55px;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

div[data-testid="stButton"] > button:hover {
    transform: scale(1.3);
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)



st.markdown(
    """
    <div class='main-title'>
        🏦 Customer Churn Prediction
    </div>
    <div class='subtitle'>
        Predict customer retention using a Neural Network
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.image("image1.jpg", width=120)

    st.title("Dashboard")

#     st.info("""
#     Neural Network Churn Predictor

#     Features:
#     - Customer Analytics
#     - Churn Prediction
#     - Real-time Results
#     """)
# # st.image("C:/Users/SAGAR GUPTA/Downloads/image1.jpg",use_container_width=True)

# model=load_model("churn_model.keras")
# scaler=joblib.load("scaler.joblib")
# Encoder_Geo=joblib.load("Encoder_Geo.joblib")
# Encoder_Gender=joblib.load("Encoder_Gender.joblib")



# col1,col2=st.columns(2)
# # User Inputs
# with col1:
#     credit_score=st.number_input("Enter credit score",value=591)
#     Geography=st.selectbox("Select Geography",["France","Spain","Germany"])
#     Gender=st.selectbox("Select Gender",["Male","Female"])
#     Age=st.number_input("Enter Age",value=40)
#     Tenure=st.number_input("Enter Tenure",value=3)

# with col2:
#     # HasCrCard=st.checkbox("Has CrCard",value=True)
#     Balance=st.number_input("Enter Balance")
#     No_of_products=st.number_input("Enter No of Products",value=1)
#     HasCrCard=st.selectbox("Enter HasCrCard",[0,1])
#     IsActiveMember=st.selectbox("Enter IsActiveMember",[0,1])
#     EstimatedSalary=st.number_input("Enter EstimatedSalary")


# if st.button("Predict"):

#     Encoder_Ge=Encoder_Geo.transform([Geography])[0]
#     Encoder_Gen=Encoder_Gender.transform([[Gender]])[0]
#     Data = [credit_score, Encoder_Ge, Encoder_Gen, Age, Tenure, Balance, No_of_products, HasCrCard,IsActiveMember,EstimatedSalary]
#     input_data=np.array(Data).reshape(1,-1)
#     input_Scaler=scaler.transform(input_data)

#     Prediction=model.predict(input_Scaler)
#     # st.write(Prediction)

#     prediction_label=[np.argmax(Prediction)]
#     # st.write(prediction_label)

#     if (prediction_label[0]==0):
#         st.markdown("""
#                 <div style="
#                     background:#dcfce7;
#                     padding:25px;
#                     border-radius:15px;
#                     text-align:center;
#                     font-size:24px;
#                     font-weight:bold;
#                     color:#166534;">
#                     ✅ Customer Not Likely To Exit
#                 </div>
#                 """, unsafe_allow_html=True)
#         # st.success('✅ Customer Not Likely to Exit')
#     else:
#         st.markdown("""
#          <div style="
#              background:#fee2e2;
#              padding:25px;
#              border-radius:15px;
#              text-align:center;
#              font-size:24px;
#              font-weight:bold;
#              color:#991b1b;">
#              ⚠️ Customer Likely To Exit
#          </div>
#          """, unsafe_allow_html=True)
#         # st.error('⚠️ Customer Likely to Exit')
