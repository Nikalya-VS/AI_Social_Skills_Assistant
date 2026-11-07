import streamlit as st
import sqlite3
import bcrypt
import requests

# =====================================================
# DATABASE
# =====================================================

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password_hash TEXT
)
""")

conn.commit()

# =====================================================
# FUNCTIONS
# =====================================================

def create_user(email, password):

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    if cursor.fetchone():
        return False, "Account already exists"

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    cursor.execute(
        """
        INSERT INTO users
        (email,password_hash)
        VALUES(?,?)
        """,
        (
            email,
            hashed.decode()
        )
    )

    conn.commit()

    return True, "Account created successfully"


def login_user(email, password):

    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    user = cursor.fetchone()

    if not user:
        return False, "Account not found"

    if bcrypt.checkpw(
        password.encode(),
        user[2].encode()
    ):
        return True, "Login successful"

    return False, "Incorrect password"

# =====================================================
# LOGIN PAGE
# =====================================================

def show_login_page():

    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "Login"

    st.markdown("""
    <style>

    .block-container{
        padding-top:2rem;
    }

    .glass-card{

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);

    border: 1px solid rgba(255,255,255,0.25);

    border-radius: 30px;

    padding: 25px 30px;

    max-width: 650px;

    margin: auto;

    box-shadow:
    0 8px 32px rgba(31,38,135,0.18);
    }

    .main-title{
        font-size:50px;
        font-weight:800;
        color:#1f2a44;
        text-align:center;
    }

    .sub-title{

    text-align:center;

    color:#555;

    font-size:26px;

    font-weight:500;

    margin-bottom:30px;

    }
    div[data-testid="stTextInput"] [data-testid="stWidgetLabel"] p,
    div[data-testid="stCheckbox"] [data-testid="stWidgetLabel"] p {
        font-size:26px !important;
        font-weight:400 !important;
        color:#1f2a44 !important;
    }

    div[data-testid="stTextInput"] input {

    width:100% !important;

    font-size:22px !important;

    height:65px !important;

    border-radius:15px !important;

    }
    div[data-testid="stTextInput"]{
    width:100% !important;
    }

    div[data-testid="stCheckbox"] label {

    display:flex !important;

    align-items:center !important;

    gap:10px !important;

    }
    div[data-testid="stCheckbox"] label p {

    margin:0 !important;

    font-size:18px !important;

    font-weight:500 !important;

    }


    div.stButton > button{
        border-radius:18px !important;

        background:
        linear-gradient(
        90deg,
        #5A4FF3,
        #8266FF
        ) !important;

        color:white !important;

        font-size:20px !important;

        font-weight:700 !important;

        border:none !important;

        height:52px !important;
    }

    div.stButton > button p {
        font-size:20px !important;
    }

    div.stButton > button:hover{
        transform:translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.15, 1])

    # =================================================
    # LEFT SIDE HERO
    # =================================================

    with left:

        st.image(
            "assets/hero.png",
            use_container_width=True
        )

        st.markdown(
        """
        <h1 style="
        color:#1F2A44;
        font-size:52px;
        font-weight:800;
        ">
        Welcome to SociBuddy 🤖
        </h1>
        """,
        unsafe_allow_html=True
        )

        st.markdown(
        """
        <p style="
        font-size:24px;
        color:#555;">
        Helping children build
        confidence through AI-powered
        social interaction training.
        </p>
        """,
        unsafe_allow_html=True
        )

    # =================================================
    # RIGHT SIDE LOGIN CARD
    # =================================================

    with right:

        st.markdown("""
        <div class='glass-card'>
        """,
        unsafe_allow_html=True)

        st.markdown("""
        <div class='main-title'>
        Welcome Back
        </div>
        """,
        unsafe_allow_html=True)

        st.markdown("""
        <div class='sub-title'>
        Sign in to continue
        </div>
        """,
        unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:
            if st.button(
                "Login",
                use_container_width=True
            ):
                st.session_state.auth_mode="Login"

        with col2:
            if st.button(
                "Sign Up",
                use_container_width=True
            ):
                st.session_state.auth_mode="Signup"

        st.write("")

        # =============================================
        # LOGIN
        # =============================================

        if st.session_state.auth_mode=="Login":

            email = st.text_input(
                "Email",
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            remember = st.checkbox(
                "Remember Me"
            )

            if st.button(
                "Login Account",
                use_container_width=True
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/login",
                    json={
                        "email": email,
                        "password": password
                    }
                )

                if response.status_code == 200:

                    st.success(
                        "✅ Login Successful"
                    )

                    st.session_state.logged_in = True

                    st.session_state.user = email

                    st.session_state.page = "Dashboard"

                    st.rerun()

                else:

                    st.error(
                        response.json()["detail"]
                    )

        # =============================================
        # SIGNUP
        # =============================================

        else:

            email = st.text_input(
                "Email",
                key="signup_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="signup_pass"
            )

            confirm = st.text_input(
                "Confirm Password",
                type="password",
                key="signup_confirm"
            )

            if st.button(
                "Create Account",
                use_container_width=True
            ):

                if password != confirm:

                    st.error(
                        "❌ Passwords do not match"
                    )

                elif len(password) < 6:

                    st.error(
                        "❌ Password must contain at least 6 characters"
                    )

                else:

                    response = requests.post(
                        "http://127.0.0.1:8000/signup",
                        json={
                            "email": email,
                            "password": password
                        }
                    )

                    if response.status_code == 200:

                        st.success(
                            "✅ Account Created Successfully"
                        )

                        st.session_state.auth_mode = "Login"

                    else:

                        st.error(
                            response.json()["detail"]
                        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )