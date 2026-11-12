import streamlit as st
from pages.Login import show_login_page
from pages.Dashboard import show_dashboard
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="SociBuddy",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
section[data-testid="stSidebar"] { display: none; }
.block-container, div[data-testid="stMainBlockContainer"] {
    width: 100%; max-width: 1420px; box-sizing: border-box;
    padding: 1rem clamp(.75rem, 3vw, 2.5rem) 2rem;
}
.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #edf5ff 48%, #fff 100%);
}
div.stButton > button {
    border-radius: 999px !important;
    height: 44px !important;
    min-height: 44px !important;
    padding: 0 1rem !important;
    font-weight: 700;
    border: none !important;
    transition: transform .2s, box-shadow .2s, background-color .2s;
    background: #fff;
    color: #233b76;
    box-shadow: 0 4px 14px rgba(34,68,130,.08);
    white-space: nowrap;
}
div.stButton > button p { font-size: clamp(.78rem, 1vw, 1rem) !important; }
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 7px 18px rgba(34,68,130,.16);
}
.st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
    display: grid;
    grid-template-columns: minmax(205px, 1.7fr) repeat(7, minmax(78px, 1fr));
    gap: .55rem;
    align-items: center;
}
.st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    width: 100% !important; min-width: 0 !important; flex: none !important;
    box-sizing: border-box;
}
.brand {
    color: #276cf4; font-size: clamp(1.6rem, 2.2vw, 2.1rem);
    font-weight: 900; letter-spacing: -1px; line-height: 1;
}
.brand-tagline {
    margin-top: .35rem; color: #526487; font-size: .72rem;
    font-weight: 700; letter-spacing: .01em;
}
.st-key-nav_home button { background: #eaf2ff !important; color: #2868f5 !important; }
.st-key-nav_login button {
    background: #fff !important; color: #2868f5 !important;
    border: 1px solid #cbd9ff !important;
}
.st-key-nav_get_started button,
.st-key-hero_get_started button {
    background: linear-gradient(100deg, #6558f5, #874cf1) !important;
    color: #fff !important;
    box-shadow: 0 8px 18px rgba(103,83,238,.25);
}
.st-key-hero_get_started button { min-width: 10rem; }
.st-key-landing_hero > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
    display: grid;
    grid-template-columns: minmax(0, 1.03fr) minmax(0, 1fr);
    align-items: center;
    gap: clamp(1rem, 3vw, 2.5rem);
}
.st-key-landing_hero > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    width: 100% !important; min-width: 0 !important; flex: none !important;
    box-sizing: border-box;
}
.hero-copy { padding: clamp(.25rem, 2vw, 1.5rem) 0; }
.badge {
    display: inline-block; max-width: 100%; padding: .65rem 1rem;
    border-radius: 999px; background: #e6f2ff; color: #365b9d;
    font-size: clamp(.78rem, 1.1vw, .95rem); font-weight: 700;
}
.hero-title {
    margin: .9rem 0 .7rem; color: #102457;
    font-size: clamp(2.55rem, 5vw, 4.5rem); font-weight: 900;
    line-height: 1.04; letter-spacing: -.045em;
}
.hero-highlight {
    background: linear-gradient(90deg, #3483ff, #9454ef, #ed62ad);
    -webkit-background-clip: text; color: transparent;
}
.hero-description {
    max-width: 36rem; color: #5b6b8d;
    font-size: clamp(1rem, 1.65vw, 1.35rem); line-height: 1.55;
}
.st-key-landing_hero img {
    border-radius: 24px;
    filter: drop-shadow(0 18px 30px rgba(42,94,161,.12));
}
.st-key-landing_features > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
.st-key-landing_values > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
    display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: .85rem;
}
.st-key-landing_features > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"],
.st-key-landing_values > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    width: 100% !important; min-width: 0 !important; flex: none !important;
    box-sizing: border-box;
}
.feature-card {
    height: 100%; min-height: 112px; padding: 1rem .7rem;
    border: 1px solid rgba(255,255,255,.9); border-radius: 20px;
    background: rgba(255,255,255,.82); text-align: center;
    box-shadow: 0 8px 24px rgba(36,68,130,.08);
}
.feature-icon {
    display: inline-grid; width: 54px; height: 54px; place-items: center;
    margin-bottom: .35rem; border-radius: 50%; font-size: 1.8rem;
}
.feature-card h4 {
    margin: .2rem 0 0; color: #172d63;
    font-size: clamp(.82rem, 1.2vw, 1rem); line-height: 1.25;
}
.st-key-landing_values {
    margin-top: 1.25rem; padding: .75rem; border-radius: 20px;
    background: rgba(235,243,255,.78);
}
.value-item {
    display: flex; min-height: 46px; align-items: center; justify-content: center;
    gap: .5rem; color: #203568; font-size: clamp(.8rem, 1.15vw, .98rem);
    font-weight: 800; text-align: center;
}
.value-item span { font-size: 1.5rem; }
.st-key-contact_button button { background: #eaf2ff !important; color: #2868f5 !important; }
@media (max-width: 1100px) {
    .st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
        grid-template-columns: repeat(4, minmax(0, 1fr));
    }
    .st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
        grid-column: 1 / -1;
    }
}
@media (max-width: 820px) {
    .st-key-landing_hero > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
        grid-template-columns: minmax(0, 1fr);
    }
    .st-key-landing_hero [data-testid="stImage"] { max-width: 680px; margin-inline: auto; }
}
@media (max-width: 620px) {
    .st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    .st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
        grid-column: 1 / -1;
    }
    .st-key-landing_features > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
    .st-key-landing_values > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    .hero-copy, .hero-description { text-align: center; margin-inline: auto; }
}
@media (max-width: 380px) {
    .st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
        grid-template-columns: minmax(0, 1fr);
    }
    .st-key-landing_nav > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
        grid-column: 1;
    }
    .st-key-landing_features > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"],
    .st-key-landing_values > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
        grid-template-columns: minmax(0, 1fr);
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE FUNCTIONS
# ---------------------------------------------------

def home_page():
    def navigate(page):
        st.session_state.page = page
        st.rerun()

    with st.container(key="landing_nav"):
        columns = st.columns([2.3, .7, .7, .9, 1.1, .8, .75, 1.15], gap="small")

    with columns[0]:
        st.markdown(
            """
            <div class="brand">🧡 SociBuddy</div>
            <div class="brand-tagline">Small Steps. Brighter Tomorrows.</div>
            """,
            unsafe_allow_html=True,
        )

    labels = ("Home", "About", "Features", "For Parents", "Contact", "Login", "Get Started")
    pages = ("Home", "About", "Features", "Parents", "Contact", "Login", "Login")
    keys = (
        "nav_home",
        "nav_about",
        "nav_features",
        "nav_parents",
        "contact_button",
        "nav_login",
        "nav_get_started",
    )
    for column, label, page, key in zip(columns[1:], labels, pages, keys):
        with column:
            if st.button(label, key=key, width="stretch"):
                navigate(page)

    with st.container(key="landing_hero"):
        left, right = st.columns([1.03, 1], gap="large")
        with left:
            st.markdown(
                '<div class="hero-copy"><div class="badge">'
                "✨ An AI-Powered Social Skills Assistant for Children with ASD"
                "</div></div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="hero-title">Building Brighter<br>'
                '<span class="hero-highlight">Connections</span> Together</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="hero-description">Fun. Interactive. Personalized. '
                "Because every child deserves to feel understood and included.</div>",
                unsafe_allow_html=True,
            )
            with st.container(key="landing_features"):
                features = st.columns(4, gap="small")
                feature_data = (
                    ("👥", "Learn Social Skills", "#ffe4ed", "#ed5d87"),
                    ("🎮", "Play & Practice", "#dcf8ef", "#12ad8a"),
                    ("📊", "Track Progress", "#fff1cb", "#e7a400"),
                    ("💜", "Build Confidence", "#e9e3ff", "#7d5bea"),
                )
                for feature_column, (icon, label, background, color) in zip(features, feature_data):
                    with feature_column:
                        st.markdown(
                            f"""
                            <div class="feature-card">
                              <div class="feature-icon" style="background:{background};color:{color}">{icon}</div>
                              <h4>{label}</h4>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
            st.write("")
            if st.button("Get Started  →", key="hero_get_started", width="content"):
                navigate("Login")
        with right:
            st.image("assets/hero.png", width="stretch")

    with st.container(key="landing_values"):
        values = st.columns(4, gap="small")
        value_data = (
            ("👨‍👩‍👧", "For a More Inclusive World"),
            ("💗", "Every Child Matters"),
            ("🌱", "Grow Through Practice"),
            ("⭐", "Small Steps, Big Progress"),
        )
        for column, (icon, text) in zip(values, value_data):
            with column:
                st.markdown(
                    f'<div class="value-item"><span>{icon}</span>{text}</div>',
                    unsafe_allow_html=True,
                )

def about_page():
    st.title("📖 About SociBuddy")
    st.write("SociBuddy helps children build confidence through guided, encouraging social-skills practice.")
    if st.button("← Back to Home", key="about_home"):
        st.session_state.page = "Home"
        st.rerun()

def features_page():
    st.title("✨ Features")
    st.write("Practice greetings, recognizing emotions, smiling, eye contact, and everyday conversations.")
    if st.button("🚀 Get Started", key="features_start"):
        st.session_state.page = "Login"
        st.rerun()
    if st.button("← Back to Home", key="features_home"):
        st.session_state.page = "Home"
        st.rerun()

def parent_page():
    st.title("👨‍👩‍👧 Parent Portal")
    st.write("Support your child by practicing at their pace and celebrating each small step.")
    if st.button("← Back to Home", key="parents_home"):
        st.session_state.page = "Home"
        st.rerun()

def contact_page():
    st.title("💬 Contact")
    st.write("For help with an account or a practice session, please contact the parent or caregiver managing it.")
    if st.button("← Back to Home", key="contact_home"):
        st.session_state.page = "Home"
        st.rerun()

def login_page():
    st.switch_page("pages/Login.py")

def training_page():
    st.title("🎯 Training Modules")
    st.write("Module cards will be shown here.")

# ---------------------------------------------------
# ROUTER
# ---------------------------------------------------

page = st.session_state.page

if page == "Home":
    home_page()

elif page == "About":
    about_page()

elif page == "Features":
    features_page()

elif page == "Parents":
    parent_page()

elif page == "Contact":
    contact_page()

elif page == "Login":
    show_login_page()

elif page == "Training":
    training_page()
elif page == "Dashboard":
    show_dashboard()