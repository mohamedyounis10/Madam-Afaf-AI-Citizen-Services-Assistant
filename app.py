import requests
import streamlit as st
import base64
import os

# ================================================================
# FUNCTION TO LOAD LOCAL IMAGE AS BASE64
# ================================================================
@st.cache_data(show_spinner=False)
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8").replace("\n", "")
    except FileNotFoundError:
        return ""


# ================================================================
# IMAGE PATH
# ================================================================
img_path = r"C:\Users\moham\Desktop\Tips Hindawei\Final Project\image.jpg"

img_b64 = get_base64_image(img_path)

if img_b64:
    bg_url = f"data:image/jpeg;base64,{img_b64}"
else:
    bg_url = (
        "https://images.unsplash.com/"
        "photo-1539650116574-8efeb43e2b50"
        "?q=80&w=1920&auto=format&fit=crop"
    )


# ================================================================
# PAGE CONFIG
# ================================================================
st.set_page_config(
    page_title="مدام عفاف | Madam Afaf",
    page_icon="👩‍💼",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ================================================================
# GLOBAL CSS
# ================================================================
st.markdown(
    f"""
<style>

* {{
    font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        "Helvetica Neue",
        Arial,
        sans-serif !important;
}}


/* ===================== MAIN APP DIRECTION ===================== */

[data-testid="stAppViewContainer"] {{
    direction: ltr;
}}

[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
.block-container {{
    direction: rtl;
    text-align: right;
}}


/* ===================== SIDEBAR DIRECTION ===================== */

[data-testid="stSidebar"] {{
    direction: rtl;
    text-align: right;
}}

[data-testid="stSidebar"] * {{
    direction: rtl;
    text-align: right;
}}


/* ===================== SIDEBAR SPACING ===================== */

[data-testid="stSidebar"] > div:first-child {{
    padding-top: 2rem !important;
}}

[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}}

[data-testid="stSidebar"] .block-container {{
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
}}


/* ===================== SIDEBAR FONT ===================== */

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] li {{
    font-size: 1.15rem !important;
    line-height: 1.8 !important;
}}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
    font-size: 1.5rem !important;
    font-weight: 700 !important;
}}

[data-testid="stSidebar"] ul {{
    padding-right: 1.4rem !important;
    padding-left: 0 !important;
}}

[data-testid="stSidebar"] hr {{
    margin: 1.2rem 0 !important;
}}


/* ===================== GENERAL TEXT ===================== */

h1, h2, h3, h4, p, li, label, .stMarkdown,
[data-testid="stCaptionContainer"],
[data-testid="stExpander"] summary,
[data-testid="stAlert"] {{
    direction: rtl;
    text-align: right;
}}


/* ===================== CHAT MESSAGE ===================== */

[data-testid="stChatMessageContent"] p,
[data-testid="stChatMessageContent"] li {{
    direction: rtl;
    text-align: right;
    font-size: 1.3rem !important;
    line-height: 1.8 !important;
}}


/* ===================== INPUT ===================== */

textarea, input {{
    direction: rtl;
    text-align: right;
    font-size: 1.25rem !important;
}}

code {{ direction: ltr; }}

header {{ visibility: hidden; }}


/* ============================================================
   BACKGROUND IMAGE
   الصورة بقت على ::before عشان نقدر نعمل لها fade (opacity transition).
   الحالة الافتراضية = ظاهرة (landing)، ووضع الشات بيخلّيها opacity:0
   فترجع الخلفية السودا العادية.
   ============================================================ */

[data-testid="stAppViewContainer"] {{
    isolation: isolate;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    pointer-events: none;

    background-image:
        linear-gradient(rgba(0, 0, 0, 0.70), rgba(0, 0, 0, 0.70)),
        url("{bg_url}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;

    opacity: 1;
    transition: opacity 0.8s ease-in-out;
}}


/* ============================================================
   HERO (العنوان + الجملة + السؤال)
   ============================================================ */

.hero-wrap {{
    overflow: hidden;
}}

.hero-out {{
    animation: heroOut 0.6s ease forwards;
    pointer-events: none;
}}

@keyframes heroOut {{
    from {{ opacity: 1; max-height: 24rem; }}
    to   {{ opacity: 0; max-height: 0; }}
}}


/* ============================================================
   CHAT INPUT ANIMATION
   ============================================================ */

[data-testid="stBottom"] {{
    transition:
        transform 0.6s cubic-bezier(0.25, 0.8, 0.25, 1),
        background-color 0.6s ease-in-out !important;
}}

</style>
""",
    unsafe_allow_html=True,
)


# ================================================================
# API CONFIG & SETTINGS
# ================================================================
HEADERS = {"ngrok-skip-browser-warning": "true"}

RAG_K = 4
MAX_NEW_TOKENS = 300

API_URL = "https://stinging-gruffly-progress.ngrok-free.dev"


# ================================================================
# SESSION STATE
# ================================================================
st.session_state.setdefault("messages", [])
st.session_state.setdefault("pending", False)     # في سؤال لسه مستني إجابة
st.session_state.setdefault("fade_hero", False)   # لمرة واحدة: اعمل fade-out للعنوان


# ================================================================
# SIDEBAR
# ================================================================
with st.sidebar:
    st.header("💡 عن مدام عفاف")

    st.markdown(
        """
        **مساعد خدمات المواطنين** بيساعدك تعرف معلومات
        عن الخدمات الحكومية في مصر.

        - 📄 المستندات المطلوبة
        - 💰 الرسوم
        - 🔗 المصادر الرسمية للمعلومات

        ---

        **نحن نقدم استفسارات حول:**

        - 🏛️ **خدمات الأحوال المدنية**
        - 🍞 **تموين**
        - 🛂 **وزارة الداخلية (هجرة وجوازات)**

        ---

        **💬 اسأل بطريقتك العادية**

        ممكن تسأل باللهجة المصرية عادي.

        """
    )

    st.divider()

    st.caption("👩‍💼 مدام عفاف - مساعدك الذكي للمعلومات الحكومية في مصر")


# ================================================================
# HERO
# (ملاحظة: مفيش سطور فاضية جوه الـ HTML عشان الـ markdown ميكسرهوش)
# ================================================================
def render_hero(fade_out=False):
    cls = "hero-wrap hero-out" if fade_out else "hero-wrap"
    st.markdown(
        f"""
<div class="{cls}">
<h2 style="text-align: center; color: #facc15; font-size: 2.4rem; font-weight: 800; margin-top: 12vh; margin-bottom: 5px; text-shadow: 0px 4px 10px rgba(0,0,0,0.8); position: relative; right: 20px; pointer-events: none;">👩‍💼 مدام عفاف | Madam Afaf</h2>
<p style="text-align: center; color: #e2e8f0; font-size: 1.3rem; font-weight: 600; margin-top: 0; margin-bottom: 15px; text-shadow: 0px 3px 8px rgba(0,0,0,0.8); position: relative; right: 20px; pointer-events: none;">الموظفة اللي مش هتقولك فوت علينا بكرة! 😉</p>
<h1 style="text-align: center; color: white; font-size: 3.2rem; font-weight: 800; margin-top: 0; text-shadow: 0px 5px 15px rgba(0,0,0,1); position: relative; right: 35px; pointer-events: none;">ازاى اقدر اساعدك النهاردة ؟ 🏛️</h1>
</div>
""",
        unsafe_allow_html=True,
    )


# ================================================================
# DYNAMIC LAYOUT
# ================================================================
if not st.session_state.messages:

    # ------------------------- LANDING PAGE -------------------------
    st.markdown(
        """
        <style>
        /* سحب مربع الإدخال لمنتصف الشاشة */
        [data-testid="stBottom"] {
            transform: translateY(-35vh) !important;
        }
        [data-testid="stBottom"] > div {
            background-color: transparent !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    render_hero()

else:

    # -------------------------- CHAT PAGE ---------------------------
    st.markdown(
        """
        <style>
        /* رجوع مربع الكتابة لمكانه الطبيعي */
        [data-testid="stBottom"] {
            transform: translateY(0) !important;
        }
        /* الصورة بتتلاشى والخلفية ترجع سودا عادية */
        [data-testid="stAppViewContainer"]::before {
            opacity: 0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.fade_hero:
        render_hero(fade_out=True)
        st.session_state.fade_hero = False


# ================================================================
# HELPER FUNCTION
# ================================================================
def show_sources(sources):
    if not sources:
        return

    with st.expander("📚 المصادر الرسمية"):
        for source in sources:
            service_name = source.get("service_name", "الخدمة")
            url = source.get("url", "#")
            source_name = source.get("source", "المصدر")
            st.markdown(f"- [{service_name}]({url}) — {source_name}")


# ================================================================
# ASK MODEL
# ================================================================
def ask_model(question):
    if not API_URL:
        answer = "⚠️ النظام مش متصل حاليًا بالموديل."
        st.error(answer)
        return answer, []

    try:
        with st.spinner("بيفكر في الإجابة..."):
            response = requests.post(
                f"{API_URL}/ask",
                json={
                    "question": question,
                    "k": RAG_K,
                    "max_new_tokens": MAX_NEW_TOKENS,
                },
                headers=HEADERS,
                timeout=300,
            )

        if response.status_code != 200:
            raise RuntimeError(
                f"API Error {response.status_code}: {response.text[:300]}"
            )

        data = response.json()
        answer = data.get("answer", "❌ حصلت مشكلة أثناء إنشاء الإجابة.")
        sources = data.get("sources", [])
        return answer, sources

    except requests.exceptions.ConnectionError:
        answer = (
            "❌ مش قادر أوصل للموديل حاليًا.\n\n"
            "اتأكد إن الـ Kaggle Notebook شغال "
            "وإن الـ API متاحة."
        )
        return answer, []

    except requests.exceptions.Timeout:
        answer = (
            "⏳ الموديل أخد وقت طويل في الاستجابة.\n\n"
            "حاول تاني بعد شوية."
        )
        return answer, []

    except Exception as e:
        answer = f"❌ حصل خطأ: {e}"
        return answer, []


# ================================================================
# CHAT INTERFACE
# ================================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            show_sources(message.get("sources", []))


# ================================================================
# RECEIVE NEW QUESTION
# ================================================================
if question := st.chat_input("مثال: إزاي أطلّع بطاقة رقم قومي بدل فاقد؟"):
    if not st.session_state.messages:
        st.session_state.fade_hero = True

    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.pending = True
    st.rerun()


# ================================================================
# ANSWER THE PENDING QUESTION
# ================================================================
if st.session_state.pending:
    last_question = st.session_state.messages[-1]["content"]

    with st.chat_message("assistant"):
        answer, sources = ask_model(last_question)
        st.markdown(answer)
        show_sources(sources)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )
    st.session_state.pending = False