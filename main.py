import streamlit as st
import re
import random
import time
import json
import os

# ---- PAGE CONFIG ----
st.set_page_config(page_title="HG Password Strength Meter", page_icon="🔐", layout="wide")

# ---- SESSION STATE FOR LOGIN ----
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""

# ---- USERS JSON FILE ----
USER_FILE = "users.json"

# ---- FUNCTION TO LOAD USERS ----
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as file:
        return json.load(file)

# ---- FUNCTION TO SAVE USERS ----
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)

# ---- FUNCTION TO HANDLE LOGIN & REGISTRATION ----
def login_or_register():
    st.title("🔑 Login/Register to Access Password Strength Meter")
    st.sidebar.title("👋 **Hello User!**")
    st.sidebar.image("login.png")

    username = st.text_input("👤 Enter your username")  
    password = st.text_input("🔒 Enter your password", type="password")  

    users = load_users()  # Load users from JSON file

    # Check if username exists for login, else register
    if st.button("Submit"):
        if username.strip() and password.strip():
            if username in users:
                if users[username]['password'] == password:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username  
                    st.success(f"✅ Welcome back, {username}! Redirecting...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid password. Try again.")
            else:
                users[username] = {'password': password, 'password_history': []}
                save_users(users)
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success("✅ Registration successful! You are now logged in.")
                time.sleep(1)
                st.rerun()
        else:
            st.error("❌ Please enter both username and password.")

# ---- LOGOUT FUNCTION ----
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""
    st.rerun()

# ---- SHOW LOGIN SCREEN IF NOT LOGGED IN ----
if not st.session_state['logged_in']:
    login_or_register()
    st.stop()

# ---- SIDEBAR ----
st.sidebar.title("🔐 **HG Password History** ")
st.sidebar.subheader(f"👋 *Welcome, {st.session_state['username']}!*")
st.sidebar.image("sidebar.png")

if st.sidebar.button("Logout"):
    logout()

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

# ---- MAIN PAGE ----
st.title("🔐 HG Password Strength Meter")

# ---- USER INPUT ----
password = st.text_input("🔑 **Enter your password:**", type="password")

if password:
    with st.spinner("Checking password strength..."):
        time.sleep(1.5)  # Simulate processing time
    
    # Avoid duplicate passwords in history
    if st.session_state['username']:
        users = load_users()
        username = st.session_state['username']
        if password not in users[username]['password_history']:
            users[username]['password_history'].append(password)
            save_users(users)

    # Show progress bar
    strength, suggestions, criteria = check_password_strength(password)
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
if st.session_state['username']:
    users = load_users()
    username = st.session_state['username']
    st.sidebar.subheader("📝 Password History")

    for i, past_password in enumerate(reversed(users[username]['password_history'][-5:]), 1):
        st.sidebar.text(f"{i}. {past_password}")
        delete_button = st.sidebar.button(f"❌ Delete Password {i}", key=f"delete_{i}")
        if delete_button:
            users[username]['password_history'].remove(past_password)
            save_users(users)
            st.experimental_rerun()

# ---- FAQ ----
st.subheader("💡 FAQ - Toggle Question Answer")

faq = [
    ("What is a strong password?", "A strong password contains at least 8 characters, uppercase & lowercase letters, numbers, and special symbols."),
    ("How do I reset my password?", "You can reset your password by clicking on the 'Forgot Password' link on the login page."),
    ("Why is password security important?", "Password security is crucial to protect your personal and sensitive information from unauthorized access."),
]

for question, answer in faq:
    with st.expander(question):
        st.write(answer)

st.markdown("""
    <p class='footer'>💛🅲🆁🅴🅰🆃🅴🅳 🅱🆈 🅷🅰🅳🅸🆀🅰 🅶🅾🅷🅰🆁💛</p>
""", unsafe_allow_html=True)

time.sleep(2)  
st.toast("⚠️ **Use at least:** 8 characters, Uppercase, Lowercase, Number & Special Symbol!")
