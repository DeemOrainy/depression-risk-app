import streamlit as st
import joblib

# تحميل النموذج
model = joblib.load("depression_risk_model1.pkl")

st.markdown(
    """
    <style>
    .right-align {
        text-align: right;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# إدخال عدد الدقائق مع محاذاة لليمين
st.markdown('<div class="right-align">أدخل عدد دقائق استخدام جهازك في اليوم</div>', unsafe_allow_html=True)
app_usage = st.number_input("", min_value=0)
# إدخال عدد الدقائق
app_usage = st.number_input("أدخل عدد دقائق استخدام جهازك في اليوم", min_value=00)

# زر التقييم
if st.button("تقييم"):
    user_data = [[app_usage]]
    prediction = model.predict(user_data)
    if prediction[0] == 1:
        st.write("⚠️ هناك احتمال لإصابتك بالاكتئاب.")
    else:
        st.write("✅ لا يوجد خطر للإصابة بالاكتئاب.")
