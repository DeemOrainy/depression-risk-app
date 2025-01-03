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
    .right-align {
        text-align: center;
        font-size: 18px;
        margin-bottom: 10px;
    }
    div.stButton > button {
        display: block;
        margin: 20px auto;
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


# زر التقييم
if st.button("تقييم"):
    user_data = [[app_usage]]
    prediction = model.predict(user_data)
    if prediction[0] == 1:
        st.markdown('<div class="right-align">⚠️ هناك احتمال لإصابتك بالاكتئاب</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="right-align">✅ لا يوجد خطر للإصابة بالاكتئاب</div>', unsafe_allow_html=True)
