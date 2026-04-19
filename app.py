import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الصفحة (تظهر في تبويب المتصفح)
st.set_page_config(page_title="HBD", page_icon="🎂", layout="centered")


# --- دالة الاحتفال (بالونات وثلج) ---
def celebrate():
    st.balloons()
    st.snow()


# 2. واجهة الموقع
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎊 كل عام وانتي بخير ياروحي وكلعام وانتي لي 🎊</h1>", unsafe_allow_html=True)

# --- قسم العداد الزمني (Countup) ---
# ملاحظة: استبدل التاريخ أدناه بتاريخ ميلاد الشخص الحقيقي (سنة، شهر، يوم)
birth_date = datetime(2007 , 4 , 28 , 12 , 0)
now = datetime.now()
diff = now - birth_date
days = diff.days

st.markdown(
    f"<p style='text-align: center; font-size: 20px;'>احتفل فيك اليوم بمرور<b>{days}</b> يوم من الجمال والراحة وكل شي حلو بالعالم هيوفتي ✨</p>",
    unsafe_allow_html=True)
st.divider()

# --- قسم صندوق الهدايا التفاعلي ---
st.subheader("عندس هدية تبينها اضغطي تحت يالبى")

# إدارة حالة الصندوق (مفتوح أو مغلق)
if 'gift_opened' not in st.session_state:
    st.session_state.gift_opened = False

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if not st.session_state.gift_opened:
        # شكل الزر قبل الفتح
        if st.button('اضغطي هنا '):
            st.session_state.gift_opened = True
            celebrate()
            st.rerun()
    else:
        # ما يظهر "فقط" بعد فتح الهدية
        st.success(" امسكي لبى قلبس")

        # 1. الرسالة الخاصة
        st.markdown("""
        ### ل اغلى شخص بحياتي من ونا صغير في يوم ميلادك هذي هديتي البسيطة لك واتمنى دايم يوم ميلادك انك معي دهر هيوفتي ولا بنفترق احبك مره يااعز شخص بحياتي
        """)

        # 2. قسم الموسيقى (يظهر فقط هنا)
        st.write("---")
        st.write("🎵 **هذي اغنية لس امووووووووواح :**")
        # استبدل هذا الرابط برابط أغنية عيد الميلاد المفضلة لديك من يوتيوب
        youtube_url = "https://youtu.be/mFo7S8Cu4EA?si=3YhsTUnqlf6hWFtX"
        st.video(youtube_url)

        # زر لإعادة إغلاق الصندوق إذا رغب
        if st.button('باي باي اضغطي عشان تتقفل لس وحده ثانية يوم ميلادك الجاي'):
            st.session_state.gift_opened = False
            st.rerun()

# --- تذييل الصفحة ---
st.divider()
st.caption("صنع بكل حب لهيوفتي من احمد ")