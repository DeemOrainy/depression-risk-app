import streamlit as st
import joblib

# تحميل النموذج
model = joblib.load("depression_risk_modelf.pkl")

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
st.markdown('<div class="centered-title">تقييم خطر الاكتئاب بناءً على وقت استخدام برامج التواصل الاجتماعي اليومي</div>', unsafe_allow_html=True)

# إدخال عدد الساعات مع محاذاة لليمين
st.markdown('<div class="right-align">أدخل ساعات استخدامك لبرامج التواصل الاجتماعي في اليوم</div>', unsafe_allow_html=True)
app_usage_hours = st.number_input("عدد الساعات", min_value=0.0, step=0.1)  # إدخال عدد الساعات كرقم عشري

# تحويل الساعات إلى دقائق
app_usage_minutes = app_usage_hours * 60

# زر التقييم
if st.button("تقييم"):
    user_data = [[app_usage_minutes]]
    prediction = model.predict(user_data)
    if prediction[0] == 1:
        st.markdown('<div class="right-align">⚠️ هناك احتمال لإصابتك بالاكتئاب</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="right-align">✅ لا يوجد خطر للإصابة بالاكتئاب</div>', unsafe_allow_html=True)

# تعليمات الاستخدام
st.markdown('<div class="right-align">:تعليمات الإستخدام للحصول على عدد الساعات</div>', unsafe_allow_html=True)
st.markdown('<div class="right-align">الدخول على إعدادات الجهاز -> مدة استخدام الجهاز -> إظهار جميع التطبيقات -> الضغط على إظهار الفئات -> الضغط على التواصل الإجتماعي لإظهار تفاصيل المعدل اليومي</div>', unsafe_allow_html=True)
