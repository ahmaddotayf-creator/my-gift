import streamlit as st
import time
from datetime import datetime

# 1. إعدادات الصفحة
st.set_page_config(page_title="HBD", page_icon="🎂", layout="centered")

# دالة الاحتفال الكاملة (بالونات + ألعاب نارية + ثلج)
def trigger_full_celebration():
    st.balloons()
    st.snow()
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

# دالة رسم القلب الشفاف (بدون خلفية بيضاء)
def draw_transparent_heart():
    st.markdown(
        """
        <style>
        .heart-overlay {
          position: fixed;
          top: 0;
          left: 0;
          width: 100%;
          height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          background: transparent; /* جعل الخلفية شفافة تماماً */
          z-index: 10000;
          pointer-events: none; /* عشان ما يمنع الضغط على الأزرار */
        }
        .heart-pen {
          position: relative;
          width: 100px;
          height: 90px;
          animation: heartAppear 5s forwards;
        }
        .heart-pen:before, .heart-pen:after {
          position: absolute;
          content: "";
          left: 50px;
          top: 0;
          width: 50px;
          height: 80px;
          background: #FF4B4B;
          border-radius: 50px 50px 0 0;
          transform: rotate(-45deg);
          transform-origin: 0 100%;
        }
        .heart-pen:after {
          left: 0;
          transform: rotate(45deg);
          transform-origin: 100% 100%;
        }
        @keyframes heartAppear {
          0% { transform: scale(0); opacity: 0; }
          20% { transform: scale(1.5); opacity: 0.8; }
          80% { transform: scale(1.5); opacity: 0.8; }
          100% { transform: scale(0); opacity: 0; }
        }
        </style>
        <div class="heart-overlay">
          <div class="heart-pen"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- نظام التأمين بكلمة المرور ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center;'>🔒 الموقع مقفل ! الرمز يجيك في يوم ميلادس</h2>", unsafe_allow_html=True)
    password = st.text_input("الرمز السريييييييي :", type="password")
    
    if st.button("دخول", key="login_btn"): 
        if password == "0551099008rahaf_gift": 
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("الرمز خطأ، ")
else:
    # يظهر القلب الشفاف فوق المحتوى ويختفي بعد 5 ثواني
    draw_transparent_heart()
    
    # 2. واجهة الموقع
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎊 كل عام وانتي بخير ياروحي وكلعام وانتي لي 🎊</h1>", unsafe_allow_html=True)

    # --- قسم العداد الزمني ---
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
            if st.button('اضغطي هنا ', key="open_gift"):
                st.session_state.gift_opened = True
                trigger_full_celebration()
                st.rerun()
        else:
            trigger_full_celebration()
            st.success(" امسكي لبى قلبس")
            st.markdown("""
            ### ل اغلى شخص بحياتي من ونا صغير في يوم ميلادك هذي هديتي البسيطة لك واتمنى دايم يوم ميلادك انك معي دهر هيوفتي ولا بنفترق احبك مره يااعز شخص بحياتي
            """)
            st.write("---")
            st.write("🎵 **هذي اغنية لس امووووووووواح :**")
            st.video("https://youtu.be/WflC7u8pDfU?si=Xhlo6H6kjRVUX_qx")

            if st.button('باي باي اضغطي عشان تتقفل لس وحده ثانية يوم ميلادك الجاي', key="close_gift"):
                st.session_state.gift_opened = False
                st.rerun()

    st.divider()
    st.caption("صنع بكل حب لهيوفتي من احمد ") 
    
    if st.sidebar.button("قفل الموقع 🔒", key="logout_sidebar"):
        st.session_state.authenticated = False
        st.rerun()
