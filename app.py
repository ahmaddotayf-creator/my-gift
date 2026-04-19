import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الصفحة
st.set_page_config(page_title="HBD", page_icon="🎂", layout="centered")

# دالة الاحتفال الكاملة (بالونات + ألعاب نارية + ثلج)
def trigger_full_celebration():
    st.balloons()
    st.snow()
    # كود الألعاب النارية
    st.markdown(
        """
        <style>
        @keyframes fireworks {
          0% { transform: scale(0); opacity: 0; }
          50% { opacity: 1; }
          100% { transform: scale(2); opacity: 0; }
        }
        .firework {
          position: fixed;
          width: 10px;
          height: 10px;
          border-radius: 50%;
          animation: fireworks 1.5s ease-out infinite;
          z-index: 999;
        }
        .f1 { background: #FF4B4B; top: 20%; left: 20%; animation-delay: 0s; }
        .f2 { background: #FFD700; top: 50%; left: 80%; animation-delay: 0.3s; }
        .f3 { background: #00BCD4; top: 80%; left: 40%; animation-delay: 0.6s; }
        .f4 { background: #FF00FF; top: 30%; left: 60%; animation-delay: 0.9s; }
        </style>
        <div class="firework f1"></div>
        <div class="firework f2"></div>
        <div class="firework f3"></div>
        <div class="firework f4"></div>
        """,
        unsafe_allow_html=True
    )

# --- نظام التأمين بكلمة المرور ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center;'>🔒 الموقع مقفل ! الرمز يجيك في يوم ميلادس</h2>", unsafe_allow_html=True)
    password = st.text_input("الرمز السريييييييي :", type="password")
    
    if st.button("دخول"):
        if password == "0551099008rahaf_gift": 
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("الرمز خطأ، ")
else:
    # 2. واجهة الموقع
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎊 كل عام وانتي بخير ياروحي وكلعام وانتي لي 🎊</h1>", unsafe_allow_html=True)

    # --- قسم العداد الزمني (Countup) ---
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

    if 'gift_opened' not in st.session_state:
        st.session_state.gift_opened = False

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if not st.session_state.gift_opened:
            if st.button('اضغطي هنا '):
                st.session_state.gift_opened = True
                trigger_full_celebration()
                st.rerun()
        else:
            trigger_full_celebration() # لتستمر الألعاب النارية بالظهور
            st.success(" امسكي لبى قلبس")

            # 1. الرسالة الخاصة
            st.markdown("""
            ### ل اغلى شخص بحياتي من ونا صغير في يوم ميلادك هذي هديتي البسيطة لك واتمنى دايم يوم ميلادك انك معي دهر هيوفتي ولا بنفترق احبك مره يااعز شخص بحياتي
            """)

            # 2. قسم الموسيقى
            st.write("---")
            st.write("🎵 **هذي اغنية لس امووووووووواح :**")
            youtube_url = "https://youtu.be/WflC7u8pDfU?si=Xhlo6H6kjRVUX_qx"
            st.video(youtube_url)

            if st.button('باي باي اضغطي عشان تتقفل لس وحده ثانية يوم ميلادك الجاي'):
                st.session_state.gift_opened = False
                st.rerun()

    # --- تذييل الصفحة ---
    st.divider()
    st.caption("صنع بكل حب لهيوفتي من احمد ") 
    
    # زر للخروج وقفل الموقع مرة ثانية
    if st.sidebar.button("قفل الموقع 🔒"):
        st.session_state.authenticated = False
        st.rerun()
    # زر للخروج وقفل الموقع مرة ثانية
    if st.sidebar.button("قفل الموقع 🔒"):
        st.session_state.authenticated = False
        st.rerun()
