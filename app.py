import streamlit as st
from pages.Login import show_login_page
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

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background: linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 45%,
        #ffffff 100%
    );
}

/* Navbar Buttons */
div.stButton > button {
    border-radius: 30px !important;
    height: 72px;
    font-weight:600;
    border:none !important;
    transition:0.3s;
}

div.stButton > button p{
    font-size:22px !important;
}

div.stButton > button:hover{
    transform:translateY(-3px);
}

/* Hero Section */

.badge{
    background:#eaf3ff;
    padding:10px 18px;
    border-radius:25px;
    display:inline-block;
    color:#3b5ccc;
    font-weight:600;
}

.hero-title{
    font-size:70px;
    font-weight:800;
    line-height:1.1;
    color:#122a72;
}

.hero-highlight{
    color:#4d83ff;
}

.hero-description{
    font-size:23px;
    color:#60708f;
}

.st-key-hero_get_started div.stButton > button{
    font-size:48px !important;
    height:auto;
    min-height:72px;
    padding:10px 24px;
}

.st-key-hero_get_started div.stButton > button p{
    font-size:48px !important;
}

/* Cards */

.feature-card{
    background:white;
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 10px 30px rgba(0,0,0,0.08);
}

.feature-icon{
    font-size:42px;
}

.footer-card{
    background:white;
    border-radius:20px;
    padding:15px;
    text-align:center;
    box-shadow:0 10px 20px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE FUNCTIONS
# ---------------------------------------------------

def home_page():

    # Navbar
    c1,c2,c3,c4,c5,c6 = st.columns([2.4,1.1,1.1,1.25,1.35,1.1])

    with c1:
        st.markdown(
            "<h1 style='color:#5A4FF3;'>🤖 SociBuddy</h1>",
            unsafe_allow_html=True
        )

    with c2:
        if st.button("Home", use_container_width=True, key="nav_home"):
            st.session_state.page="Home"
            st.rerun()

    with c3:
        if st.button("About", use_container_width=True, key="nav_about"):
            st.session_state.page="About"
            st.rerun()

    with c4:
        if st.button("Features", use_container_width=True, key="nav_features"):
            st.session_state.page="Features"
            st.rerun()

    with c5:
        if st.button("Parents", use_container_width=True, key="nav_parents"):
            st.session_state.page="Parents"
            st.rerun()

    with c6:
        if st.button("Login", use_container_width=True, key="nav_login"):
            st.session_state.page="Login"
            st.rerun()


    st.write("")

    # Hero

    left,right = st.columns([1.15,1])

    with left:

        st.markdown("""
        <div class='badge'>
        ✨ AI-Powered Social Skills Assistant for Children with ASD
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='hero-title'>
        Building Brighter<br>
        <span class='hero-highlight'>
        Connections
        </span>
        Together
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='hero-description'>
        Fun. Interactive. Personalized.
        Because every child deserves
        to feel understood and included.
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.write("")

        if st.button("🚀 GET STARTED", key="hero_get_started"):
            st.session_state.page="Login"
            st.rerun()

    with right:
        st.image("assets/hero.png", use_container_width=True)

    st.write("")
    st.write("")

    # Features

    a,b,c,d = st.columns(4)

    with a:
        st.markdown("""
        <div class='feature-card'>
        <div class='feature-icon'>👥</div>
        <h4>Learn Social Skills</h4>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class='feature-card'>
        <div class='feature-icon'>🎮</div>
        <h4>Play & Practice</h4>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class='feature-card'>
        <div class='feature-icon'>📊</div>
        <h4>Track Progress</h4>
        </div>
        """, unsafe_allow_html=True)

    with d:
        st.markdown("""
        <div class='feature-card'>
        <div class='feature-icon'>💜</div>
        <h4>Build Confidence</h4>
        </div>
        """, unsafe_allow_html=True)

def about_page():
    st.title("📖 About SociBuddy")
    st.write("About the project goes here.")

def features_page():
    st.title("✨ Features")
    st.write("Feature list goes here.")

def parent_page():
    st.title("👨‍👩‍👧 Parent Portal")
    st.write("Parent dashboard preview.")

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

elif page == "Login":
    show_login_page()

elif page == "Training":
    training_page()