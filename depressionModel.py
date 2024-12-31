import streamlit as st
import joblib

# تحميل النموذج
model = joblib.load("depression_risk_model1.pkl")

# إضافة CSS لتوسيط النصوص
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# عنوان التطبيق مع التوسيط
st.markdown('<div class="centered-title">تقييم خطر الاكتئاب بناءً على وقت استخدام الجهاز</div>', unsafe_allow_html=True)


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
# إدخال عدد الدقائق
st.markdown('<div class="right-align">أدخل عدد دقائق استخدام جهازك في اليوم</div>', unsafe_allow_html=True)
app_usage = st.number_input("", min_value=0)
# زر التقييم
if st.button("تقييم"):
    user_data = [[app_usage]]
    prediction = model.predict(user_data)
    if prediction[0] == 1:
        st.write("⚠️ هناك احتمال لإصابتك بالاكتئاب.")
    else:
        st.write("✅ لا يوجد خطر للإصابة بالاكتئاب.")
