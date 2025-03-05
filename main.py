import streamlit as st
import re
import random
import time

# ---- PAGE CONFIG ----
st.set_page_config(page_title="HG Password Strength Meter", page_icon="🔐", layout="wide")

# ---- INITIALIZE PASSWORD HISTORY ----
if 'password_history' not in st.session_state:
    st.session_state['password_history'] = []

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        .stApp {
            background-color: var(--background-color);
            color: var(--text-color);
        }
        .title {
            color: #6f42c1;
            text-align: center;
            font-size: 28px;
        }
        .password-box {
            border-radius: 10px;
            padding: 10px;
            background-color: #ffffff;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .strong { color: green; font-weight: bold; }
        .moderate { color: orange; font-weight: bold; }
        .weak { color: red; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR TITLE ----
st.sidebar.title("🔐 HG Password History")

# ---- FUNCTION TO CHECK PASSWORD ----
def check_password_strength(password):
    score = 0
    feedback = []
    checks = {
        "✔️ At least 8 characters": len(password) >= 8,
        "✔️ Contains uppercase & lowercase": re.search(r"[A-Z]", password) and re.search(r"[a-z]", password),
        "✔️ Includes numbers (0-9)": re.search(r"\d", password),
        "✔️ Has special characters (!@#$%^&*)": re.search(r"[!@#$%^&*]", password)
    }

    for key, passed in checks.items():
        if passed:
            score += 1
        else:
            feedback.append(f"❌ {key.replace('✔️', '')}")

    return score, feedback, checks

# ---- STRONG PASSWORD GENERATOR ----
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(12))

st.header("🔐 HG Password Strength Meter")
# ---- USER INPUT ----
password = st.text_input("🔑 Enter your password:", type="password")

if password:
    with st.spinner("Checking password strength..."):
        time.sleep(1.5)  # Simulate processing time

    strength, suggestions, criteria = check_password_strength(password)
    st.session_state['password_history'].append(password)

    # Show progress bar
    st.progress(strength / 4)

    # Display Strength Rating
    if strength == 4:
        st.success("✅ **Strong Password!** 🎉")
        st.markdown("<p class='strong'>Your password is secure.</p>", unsafe_allow_html=True)
        st.balloons()
    elif strength == 3:
        st.warning("⚠️ **Moderate Password - Consider adding more security features.**")
        st.markdown("<p class='moderate'>Try making your password stronger.</p>", unsafe_allow_html=True)
    else:
        st.error("❌ **Weak Password - Improve it using the suggestions below.**")
        st.markdown("<p class='weak'>Your password is weak.</p>", unsafe_allow_html=True)

    # Show real-time feedback
    for criteria_text, passed in criteria.items():
        if passed:
            st.success(criteria_text)
        else:
            st.error(criteria_text)

    # Suggest a Strong Password
    if strength < 4:
        if st.button("🔄 Generate Strong Password"):
            strong_password = generate_password()
            st.info(f"🔐 **Suggested Password:** `{strong_password}`")

# ---- PASSWORD HISTORY DISPLAY ----
if st.session_state['password_history']:
    st.sidebar.subheader("📜 Password History")
    for i, past_password in enumerate(reversed(st.session_state['password_history'][-5:]), 1):
        st.sidebar.text(f"{i}. {past_password}")


st.text("Created by Hadiqa Gohar")