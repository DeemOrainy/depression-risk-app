import streamlit as st
import joblib

# تحميل النموذج
model = joblib.load("depression_risk_model1.pkl")

# إضافة CSS لتنسيق العنوان، النصوص، والزر
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
    }
    .right-align {
        text-align: right;
        font-size: 18px;
    }
    .center-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# عنوان التطبيق مع التوسيط
st.markdown('<div class="centered-title">تقييم خطر الاكتئاب بناءً على وقت استخدام الجهاز</div>', unsafe_allow_html=True)

# إدخال عدد الدقائق مع محاذاة لليمين
st.markdown('<div class="right-align">أدخل عدد دقائق استخدام جهازك في اليوم</div>', unsafe_allow_html=True)
app_usage = st.number_input("", min_value=0)

# زر التقييم في الوسط
st.markdown('<div class="center-button"><button type="button">تقييم</button></div>', unsafe_allow_html=True)

# تنفيذ المنطق عند النقر على الزر
if st.button("تقييم"):
    user_data = [[
