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

    st.markdown(
        """
        <style>
        .block-container, div[data-testid="stMainBlockContainer"] {
            width: 100%; max-width: 1180px; box-sizing: border-box;
            padding: clamp(1rem, 3vw, 2.5rem);
        }
        section[data-testid="stSidebar"] { display: none; }
        .st-key-login_layout > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
            display: grid;
            grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
            align-items: center;
            gap: clamp(1rem, 3vw, 3rem);
        }
        .st-key-login_layout > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
            width: 100% !important; min-width: 0 !important; flex: none !important;
            box-sizing: border-box;
        }
        .st-key-login_form_card {
            box-sizing: border-box;
            width: 100%;
            padding: clamp(1rem, 3vw, 2rem);
            background: rgba(255,255,255,.55);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255,255,255,.8);
            border-radius: 24px;
            box-shadow: 0 8px 32px rgba(31,38,135,.14);
        }
        .login-title {
            color: #1f2a44; font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 800; text-align: center; line-height: 1.1;
        }
        .login-subtitle {
            color: #555; font-size: clamp(1rem, 2vw, 1.4rem);
            font-weight: 500; text-align: center; margin-bottom: 1.5rem;
        }
        .login-hero-title {
            color: #1f2a44; font-size: clamp(2rem, 4vw, 3.25rem);
            font-weight: 800; line-height: 1.1;
        }
        .login-hero-copy {
            color: #555; font-size: clamp(1rem, 2vw, 1.5rem);
            line-height: 1.5;
        }
        div[data-testid="stTextInput"] [data-testid="stWidgetLabel"] p,
        div[data-testid="stCheckbox"] [data-testid="stWidgetLabel"] p {
            font-size: clamp(1rem, 2vw, 1.3rem) !important;
            font-weight: 500 !important;
            color: #1f2a44 !important;
        }
        div[data-testid="stTextInput"] input {
            box-sizing: border-box;
            width: 100% !important;
            min-height: 3rem;
            font-size: clamp(1rem, 1.8vw, 1.25rem) !important;
            border-radius: 12px !important;
        }
        div[data-testid="stTextInput"] { width: 100% !important; }
        div[data-testid="stCheckbox"] label {
            display: flex !important; align-items: center !important; gap: 10px;
        }
        div[data-testid="stCheckbox"] label p {
            margin: 0 !important; font-size: 1rem !important; font-weight: 500 !important;
        }
        div.stButton > button {
            width: 100%;
            height: 3.25rem !important;
            min-height: 3.25rem;
            padding: .5rem 1rem;
            border-radius: 16px !important;
            background: linear-gradient(90deg, #5A4FF3, #8266FF) !important;
            color: white !important;
            font-size: clamp(1rem, 1.8vw, 1.2rem) !important;
            font-weight: 700 !important;
            border: none !important;
        }
        div.stButton > button p { font-size: inherit !important; }
        div.stButton > button:hover { transform: translateY(-2px); }
        @media (max-width: 900px) {
            .st-key-login_layout > [data-testid="stLayoutWrapper"] > [data-testid="stHorizontalBlock"] {
                grid-template-columns: minmax(0, 1fr);
            }
            .st-key-login_layout [data-testid="stImage"] {
                max-width: 420px; margin-inline: auto;
            }
        }
        @media (max-width: 520px) {
            .st-key-login_layout [data-testid="stImage"] { max-width: 220px; }
            .login-hero-title { text-align: center; }
            .login-hero-copy { text-align: center; }
            .login-subtitle { margin-bottom: 1rem; }
            .st-key-login_form_card { border-radius: 18px; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="login_layout"):
        left, right = st.columns([1.05, 1], gap="large")

        with left:
            st.image("assets/hero.png", width="stretch")
            st.markdown(
                '<div class="login-hero-title">Welcome to SociBuddy 🤖</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="login-hero-copy">Helping children build confidence '
                "through AI-powered social interaction training.</div>",
                unsafe_allow_html=True,
            )

        with right:
            with st.container(key="login_form_card"):
                st.markdown('<div class="login-title">Welcome Back</div>', unsafe_allow_html=True)
                st.markdown(
                    '<div class="login-subtitle">Sign in to continue</div>',
                    unsafe_allow_html=True,
                )

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Login", width="stretch", key="login_mode_button"):
                        st.session_state.auth_mode = "Login"

                with col2:
                    if st.button("Sign Up", width="stretch", key="signup_mode_button"):
                        st.session_state.auth_mode = "Signup"

                st.write("")

                if st.session_state.auth_mode == "Login":
                    email = st.text_input("Email")
                    password = st.text_input("Password", type="password")
                    st.checkbox("Remember Me")

                    if st.button("Login Account", width="stretch"):
                        response = requests.post(
                            "http://127.0.0.1:8000/login",
                            json={"email": email, "password": password},
                        )

                        if response.status_code == 200:
                            st.success("✅ Login Successful")
                            st.session_state.logged_in = True
                            st.session_state.user = email
                            st.session_state.page = "Dashboard"
                            st.rerun()
                        else:
                            st.error(response.json()["detail"])
                else:
                    email = st.text_input("Email", key="signup_email")
                    password = st.text_input("Password", type="password", key="signup_pass")
                    confirm = st.text_input(
                        "Confirm Password",
                        type="password",
                        key="signup_confirm",
                    )

                    if st.button("Create Account", width="stretch"):
                        if password != confirm:
                            st.error("❌ Passwords do not match")
                        elif len(password) < 6:
                            st.error("❌ Password must contain at least 6 characters")
                        else:
                            response = requests.post(
                                "http://127.0.0.1:8000/signup",
                                json={"email": email, "password": password},
                            )

                            if response.status_code == 200:
                                st.success("✅ Account Created Successfully")
                                st.session_state.auth_mode = "Login"
                            else:
                                st.error(response.json()["detail"])