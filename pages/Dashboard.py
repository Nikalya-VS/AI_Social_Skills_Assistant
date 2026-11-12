import html
import re

import streamlit as st


ACTIVITIES = [
    ("greetings", "Greetings", "assets/dashboard/greetings.png"),
    ("smile", "Smile Detection", "assets/dashboard/smile.png"),
    ("eye_contact", "Eye Contact", "assets/dashboard/eye_contact.png"),
    ("emotion", "Emotion Recognition", "assets/dashboard/emotion.png"),
    ("conversation", "Daily Conversation", "assets/dashboard/conversation.png"),
]


def display_name_from_email(email):
    local_part = str(email or "").split("@", 1)[0]
    words = re.sub(r"[._\-+\d]+", " ", local_part).split()
    return " ".join(word.capitalize() for word in words) or "Friend"


def show_dashboard():
    email = st.session_state.get("user", "")
    name = st.session_state.get("display_name") or display_name_from_email(email)
    safe_name = html.escape(str(name))
    first_name = safe_name.split()[0] if safe_name else "Friend"

    st.markdown(
        """
        <style>
        .block-container, div[data-testid="stMainBlockContainer"] {
            width: 100%; max-width: none; box-sizing: border-box;
            padding: 1rem clamp(.75rem, 2.4vw, 2.25rem) 1.5rem;
        }
        section[data-testid="stSidebar"] { display: none; }
        .stApp {
            background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 55%, #f7f8ff 100%);
            color: #10245f;
        }
        header[data-testid="stHeader"], footer, #MainMenu { visibility: hidden; }
        .sb-topbar {
            display: flex; align-items: center; justify-content: space-between;
            gap: 12px; flex-wrap: wrap; padding: 4px 4px 18px;
        }
        .sb-brand { display: flex; align-items: center; gap: 12px; }
        .sb-logo {
            width: 58px; height: 58px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            background: linear-gradient(145deg, #dbe6ff, #fff);
            box-shadow: 0 5px 16px #6679c526; font-size: 34px;
        }
        .sb-brand-name {
            font-size: 32px; font-weight: 1000; letter-spacing: -1px;
            line-height: 1; background: linear-gradient(90deg, #7b2ff2, #2866f6);
            -webkit-background-clip: text; color: transparent;
        }
        .sb-brand-sub { font-size: 13px; font-weight: 700; color: #1b347b; margin-top: 5px; }
        .sb-nav {
            display: flex; gap: 8px; flex-wrap: wrap; align-items: center;
        }
        .sb-pill {
            background: #fff; border: 1px solid #e7eaff; border-radius: 28px;
            padding: 10px 16px; box-shadow: 0 5px 14px #6679c51c;
            font-weight: 800; color: #152b78; white-space: nowrap;
        }
        .sb-pill.active { background: linear-gradient(100deg, #4f70ff, #5c7cf4); color: white; }
        .sb-hero {
            min-height: 240px; border-radius: 25px; padding: 28px 42px;
            overflow: hidden; position: relative; display: flex; align-items: center;
            background: radial-gradient(circle at 78% 45%, #83c8ff 0, #9dd5ff 24%, transparent 46%),
                linear-gradient(105deg, #d9e8ff 0%, #f2f5ff 43%, #8ecbff 100%);
            box-shadow: 0 10px 24px #5b76ce20;
        }
        .sb-hero-copy { position: relative; z-index: 1; max-width: 65%; }
        .sb-hero h1 {
            font-size: clamp(38px, 4.2vw, 64px); line-height: .98;
            letter-spacing: -2px; color: #081b79; font-weight: 1000; margin: 0 0 12px;
        }
        .sb-hero h1 span { color: #803df0; }
        .sb-lead { font-size: 21px; font-weight: 900; color: #071d76; margin-bottom: 4px; }
        .sb-sublead { font-size: 17px; color: #254078; font-weight: 600; }
        .sb-hero-art {
            position: absolute; right: 8%; bottom: -12px;
            font-size: clamp(90px, 13vw, 165px);
            filter: drop-shadow(0 12px 8px #3957a333);
        }
        .sb-stat {
            min-height: 104px; border: 2px solid #fff; border-radius: 22px;
            padding: 15px 18px; display: flex; align-items: center; gap: 14px;
            box-shadow: 0 8px 18px #6879c51c;
        }
        .sb-stat-icon { font-size: 42px; line-height: 1; }
        .sb-stat-title { font-size: 25px; font-weight: 1000; line-height: 1.1; }
        .sb-stat-caption { font-size: 15px; color: #273c7b; font-weight: 700; margin-top: 4px; }
        .sb-mission {
            min-height: 104px; border-radius: 22px;
            background: linear-gradient(100deg, #d6f9e7, #c9f5e4);
            padding: 16px 20px; display: flex; gap: 14px; align-items: center;
            box-shadow: 0 8px 18px #55b58b24;
        }
        .sb-mission-icon { font-size: 40px; }
        .sb-mission-title { font-size: 19px; font-weight: 1000; color: #06465a; }
        .sb-mission-copy { font-size: 15px; color: #164f61; line-height: 1.35; }
        .sb-section-title { color: #071b78; font-size: 28px; font-weight: 1000; margin: 12px 0 2px; }
        .sb-section-hint { color: #4d6097; font-weight: 700; margin-bottom: 10px; }
        .sb-panel {
            background: #ffffffc9; border: 1px solid #e4e9ff; border-radius: 22px;
            padding: 18px; box-shadow: 0 8px 18px #6679c51b; height: 100%;
        }
        .sb-panel-title { color: #071b78; font-size: 20px; font-weight: 1000; margin-bottom: 12px; }
        .sb-achievements { display: flex; justify-content: space-around; gap: 8px; text-align: center; }
        .sb-achievement { color: #263b78; font-size: 13px; }
        .sb-medal {
            width: 54px; height: 54px; border-radius: 50%; display: grid;
            place-items: center; margin: 0 auto 6px; font-size: 30px;
            background: linear-gradient(145deg, #fff2b2, #ffdc75);
        }
        .sb-achievement strong { display: block; color: #071b78; }
        .sb-say {
            min-height: 150px; border-radius: 22px; padding: 20px 24px;
            color: white; background: linear-gradient(110deg, #9b8cf6, #6289ff);
            display: flex; align-items: center; gap: 16px;
            box-shadow: 0 8px 18px #6679c51b;
        }
        .sb-say-bot { font-size: 58px; }
        .sb-say-label { font-size: 18px; font-weight: 1000; }
        .sb-say-text { font-size: 16px; font-weight: 800; line-height: 1.45; margin-top: 8px; }
        .st-key-dashboard_stats [data-testid="stHorizontalBlock"],
        .st-key-dashboard_activity_grid [data-testid="stHorizontalBlock"],
        .st-key-dashboard_bottom [data-testid="stHorizontalBlock"] {
            display: grid;
            gap: .75rem;
        }
        .st-key-dashboard_stats [data-testid="stHorizontalBlock"] {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }
        .st-key-dashboard_activity_grid [data-testid="stHorizontalBlock"] {
            grid-template-columns: repeat(5, minmax(0, 1fr));
        }
        .st-key-dashboard_bottom [data-testid="stHorizontalBlock"] {
            grid-template-columns: minmax(0, .9fr) minmax(0, 1.1fr);
        }
        .st-key-dashboard_stats [data-testid="column"],
        .st-key-dashboard_activity_grid [data-testid="column"],
        .st-key-dashboard_bottom [data-testid="column"] {
            width: auto !important; min-width: 0 !important; flex: none !important;
        }
        div.stButton > button {
            border-radius: 24px; font-weight: 800; border: 0;
            background: linear-gradient(100deg, #4f70ff, #7136ed); color: white;
        }
        @media (max-width: 1100px) {
            .st-key-dashboard_stats [data-testid="stHorizontalBlock"] {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
            .st-key-dashboard_activity_grid [data-testid="stHorizontalBlock"] {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }
        }
        @media (max-width: 760px) {
            .st-key-dashboard_activity_grid [data-testid="stHorizontalBlock"] {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
            .st-key-dashboard_bottom [data-testid="stHorizontalBlock"] {
                grid-template-columns: minmax(0, 1fr);
            }
            .sb-hero { padding: 24px; }
            .sb-hero-copy { max-width: 85%; }
            .sb-hero-art { right: 0; opacity: .65; }
            .sb-brand-name { font-size: 26px; }
        }
        @media (max-width: 520px) {
            .st-key-dashboard_stats [data-testid="stHorizontalBlock"],
            .st-key-dashboard_activity_grid [data-testid="stHorizontalBlock"] {
                grid-template-columns: minmax(0, 1fr);
            }
            .sb-topbar { align-items: flex-start; }
            .sb-nav { justify-content: flex-start; gap: 6px; }
            .sb-pill { padding: 8px 11px; font-size: 13px; }
            .sb-hero { min-height: 220px; padding: 22px 18px; }
            .sb-hero-copy { max-width: 100%; }
            .sb-hero h1 { font-size: clamp(34px, 10vw, 48px); }
            .sb-hero-art { display: none; }
            .sb-stat { min-height: 84px; }
            .sb-achievements { flex-wrap: wrap; row-gap: 14px; }
            .sb-achievement { flex: 1 1 38%; }
            .sb-say { padding: 18px; gap: 10px; }
            .sb-say-bot { font-size: 42px; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="sb-topbar">
          <div class="sb-brand">
            <div class="sb-logo">🤖</div>
            <div>
              <div class="sb-brand-name">SociBuddy</div>
              <div class="sb-brand-sub">Learn · Practice · Grow · Shine</div>
            </div>
          </div>
          <div class="sb-nav">
            <div class="sb-pill active">⌂ &nbsp; Home</div>
            <div class="sb-pill">🏆 &nbsp; Rewards</div>
            <div class="sb-pill">⭐ &nbsp; Badges</div>
            <div class="sb-pill">⚙️ &nbsp; Settings</div>
            <div class="sb-pill">🧒 &nbsp; Hi, {first_name}!</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("⇥ Logout", width="content", key="dashboard_logout"):
        for key in ("logged_in", "user", "display_name", "selected_activity"):
            st.session_state.pop(key, None)
        st.session_state.page = "Home"
        st.rerun()

    st.markdown(
        f"""
        <div class="sb-hero">
          <div class="sb-hero-copy">
            <h1>Welcome Back,<br><span>{first_name}!</span> 👋</h1>
            <div class="sb-lead">Ready for another amazing learning adventure?</div>
            <div class="sb-sublead">Let's practice, learn and grow together!</div>
          </div>
          <div class="sb-hero-art">🧒🏻🤖</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    with st.container(key="dashboard_stats"):
        stats = st.columns([1, 1, 1, 1.65], gap="small")
        stat_data = [
            ("⭐", "Explorer", "Current Level", "#fff4d8", "#4d25d9"),
            ("🔥", "5 Days", "Learning Streak", "#ffe3ed", "#d01882"),
            ("🪙", "350", "Reward Points", "#eee3ff", "#4b22d5"),
        ]
        for column, (icon, title, caption, background, color) in zip(stats[:3], stat_data):
            with column:
                st.markdown(
                    f"""
                    <div class="sb-stat" style="background:{background}">
                      <div class="sb-stat-icon">{icon}</div>
                      <div><div class="sb-stat-title" style="color:{color}">{title}</div>
                      <div class="sb-stat-caption">{caption}</div></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        with stats[3]:
            st.markdown(
                """
                <div class="sb-mission">
                  <div class="sb-mission-icon">🎯</div>
                  <div><div class="sb-mission-title">Today's Mission</div>
                  <div class="sb-mission-copy">Complete any 2 activities today<br>
                  and earn an extra <b style="color:#6025df">20 Reward Points!</b></div></div>
                  <div style="font-size:30px;margin-left:auto">🚩</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="sb-section-title">🎮 Choose an Activity</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sb-section-hint">Pick a module and start your learning adventure!</div>',
        unsafe_allow_html=True,
    )
    with st.container(key="dashboard_activity_grid"):
        activity_columns = st.columns(5, gap="small")
        for column, (key, title, image_path) in zip(activity_columns, ACTIVITIES):
            with column:
                st.image(image_path, width="stretch")
                if st.button("Start Learning ➜", key=f"start_{key}", width="stretch"):
                    st.session_state.selected_activity = title
                if st.session_state.get("selected_activity") == title:
                    st.caption("Selected activity")

    with st.container(key="dashboard_bottom"):
        lower_left, lower_right = st.columns([0.9, 1.1], gap="small")
        with lower_left:
            st.markdown(
                """
                <div class="sb-panel">
                  <div class="sb-panel-title">🏆 Recent Achievements</div>
                  <div class="sb-achievements">
                    <div class="sb-achievement"><div class="sb-medal">⭐</div><strong>First Login</strong>Welcome!</div>
                    <div class="sb-achievement"><div class="sb-medal" style="background:linear-gradient(145deg,#dff8ff,#8edfff)">👋</div><strong>Greetings</strong>Completed</div>
                    <div class="sb-achievement"><div class="sb-medal" style="background:linear-gradient(145deg,#ffe2ec,#ffb6d1)">🔥</div><strong>5 Day</strong>Streak</div>
                    <div class="sb-achievement"><div class="sb-medal" style="background:linear-gradient(145deg,#eee2ff,#c7a8ff)">🏅</div><strong>Earned 50</strong>Points</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with lower_right:
            st.markdown(
                """
                <div class="sb-say">
                  <div class="sb-say-bot">🤖💗</div>
                  <div>
                    <div class="sb-say-label">SociBuddy Says:</div>
                    <div class="sb-say-text">✨ “You're doing amazing!<br>
                    Keep learning and be proud of yourself!” 💗</div>
                  </div>
                  <div style="font-size:34px;margin-left:auto">⭐</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        "<div style='text-align:center;color:#7a87b4;font-size:12px;margin-top:14px'>"
        "SociBuddy · Learn at your own pace · Every small step matters 💙</div>",
        unsafe_allow_html=True,
    )
