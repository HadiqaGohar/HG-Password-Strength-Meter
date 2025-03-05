# import streamlit as st
# import re
# import random
# import time

# # ---- PAGE CONFIG ----
# st.set_page_config(page_title="HG Password Strength Meter", page_icon="🔐", layout="wide")

# # ---- SESSION STATE FOR LOGIN ----
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False

# # ---- LOGIN SYSTEM ----
# def login():
#     st.title("🔑 Login to Access Password Strength Meter")
#     username = st.text_input("👤 Username")
#     password = st.text_input("🔒 Password", type="password")

#     if st.button("Login"):
#         if username == "hg" and password == "hg12":  # Change to your credentials
#             st.session_state['logged_in'] = True
#             st.success("✅ Login successful! Redirecting...")
#             time.sleep(1)
#             st.rerun()

#         else:
#             st.error("❌ Incorrect username or password. Try again.")

# # ---- LOGOUT FUNCTION ----
# def logout():
#     st.session_state['logged_in'] = False
#     st.rerun()


# # ---- SHOW LOGIN SCREEN IF NOT LOGGED IN ----
# if not st.session_state['logged_in']:
#     login()
#     st.stop()

# # ---- PASSWORD HISTORY ----
# if 'password_history' not in st.session_state:
#     st.session_state['password_history'] = []

# # ---- CUSTOM CSS ----
# st.markdown("""
#     <style>
#         .stApp { background-color: var(--background-color); color: var(--text-color); }
#         .title { color: #6f42c1; text-align: center; font-size: 28px; }
#         .password-box { border-radius: 10px; padding: 10px; background-color: #ffffff; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
#         .strong { color: green; font-weight: bold; }
#         .moderate { color: orange; font-weight: bold; }
#         .weak { color: red; font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)

# st.toast("💖 **Welcome** to **HG** password generator website!")

# # ---- SIDEBAR ----
# st.sidebar.title("🔐 **HG Password History!** ")
# if st.sidebar.button("Logout"):
#     logout()

# # ---- FUNCTION TO CHECK PASSWORD ----
# def check_password_strength(password):
#     score = 0
#     feedback = []
#     checks = {
#         "✔️ At least 8 characters": len(password) >= 8,
#         "✔️ Contains uppercase & lowercase": re.search(r"[A-Z]", password) and re.search(r"[a-z]", password),
#         "✔️ Includes numbers (0-9)": re.search(r"\d", password),
#         "✔️ Has special characters (!@#$%^&*)": re.search(r"[!@#$%^&*]", password)
#     }

#     for key, passed in checks.items():
#         if passed:
#             score += 1
#         else:
#             feedback.append(f"❌ {key.replace('✔️', '')}")

#     return score, feedback, checks

# # ---- STRONG PASSWORD GENERATOR ----
# def generate_password():
#     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
#     return "".join(random.choice(chars) for _ in range(12))

# st.header("🔐 HG Password Strength Meter ")

# # ---- USER INPUT ----
# password = st.text_input("🔑 **Enter your password:**", type="password")

# if password:
#     with st.spinner("Checking password strength..."):
#         time.sleep(1.5)  # Simulate processing time
    
#     # Avoid duplicate passwords in history
#     if not st.session_state['password_history'] or st.session_state['password_history'][-1] != password:
#         st.session_state['password_history'].append(password)

#     # Show progress bar
#     strength, suggestions, criteria = check_password_strength(password)
#     st.progress(strength / 4)

#     # Display Strength Rating
#     if strength == 4:
#         st.success("✅ **Strong Password!** 🎉")
#         st.markdown("<p class='strong'>Your password is secure.</p>", unsafe_allow_html=True)
#         st.balloons()
#     elif strength == 3:
#         st.warning("⚠️ **Moderate Password - Consider adding more security features.**")
#         st.markdown("<p class='moderate'>Try making your password stronger.</p>", unsafe_allow_html=True)
#     else:
#         st.error("❌ **Weak Password - Improve it using the suggestions below.**")
#         st.markdown("<p class='weak'>Your password is weak.</p>", unsafe_allow_html=True)

#     # Show real-time feedback
#     for criteria_text, passed in criteria.items():
#         if passed:
#             st.success(criteria_text)
#         else:
#             st.error(criteria_text)

#     # Suggest a Strong Password
#     if strength < 4:
#         if st.button("🔄 Generate Strong Password"):
#             strong_password = generate_password()
#             st.info(f"🔐 **Suggested Password:** `{strong_password}`")

# # ---- PASSWORD HISTORY DISPLAY ----
# if st.session_state['password_history']:
#     st.sidebar.subheader("📝 Password History")
#     for i, past_password in enumerate(reversed(st.session_state['password_history'][-5:]), 1):
#         st.sidebar.text(f"{i}. {past_password}")

# st.markdown("""
#     <style>
#         .footer {
#             text-align: center;
#             font-size: 18px;
#             font-weight: bold;
#             color: #433f40;
#             margin-top: 20px;
#         }
#     </style>
#     <p class='footer'>🅲🆁🅴🅰🆃🅴🅳 🅱🆈 🅷🅰🅳🅸🆀🅰 🅶🅾🅷🅰🆁</p>
# """, unsafe_allow_html=True)

# time.sleep(2)  # Delay before showing the toast
# st.toast("⚠️ **Use at least:** 8 characters, Uppercase, Lowercase, Number & Special Symbol!")




import streamlit as st
import re
import random
import time

# ---- PAGE CONFIG ----
st.set_page_config(page_title="HG Password Strength Meter", page_icon="🔐", layout="wide")

# ---- SESSION STATE FOR LOGIN ----
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""

# ---- LOGIN SYSTEM ----
def login():
    st.title("🔑 Login to Access Password Strength Meter")
    st.sidebar.title("👋 **Hello User!**")
    st.sidebar.image("login.png")
    username = st.text_input("👤 Enter your name")  # Store user's name
    password = st.text_input("🔒 Enter any password", type="password")  # Accept any password
    # time.sleep(2)  # Delay before showing the toast
    st.toast("⚠️ **Login to Access HG Password Strength Meter**!")


    if st.button("Login"):
        if username.strip():  # Ensure username is not empty
            st.session_state['logged_in'] = True
            st.session_state['username'] = username  # Store name in session
            st.success(f"✅ Welcome, {username}! Redirecting...")
            time.sleep(1)
            st.rerun()
        else:
            st.error("❌ Please enter a valid username.")

# ---- LOGOUT FUNCTION ----
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""
    st.rerun()

# ---- SHOW LOGIN SCREEN IF NOT LOGGED IN ----
if not st.session_state['logged_in']:
    login()
    st.stop()

# ---- PASSWORD HISTORY ----
if 'password_history' not in st.session_state:
    st.session_state['password_history'] = []

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        .stApp { background-color: var(--background-color); color: var(--text-color); }
        .title { color: #6f42c1; text-align: center; font-size: 28px; }
        .password-box { border-radius: 10px; padding: 10px; background-color: #ffffff; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
        .strong { color: green; font-weight: bold; }
        .moderate { color: orange; font-weight: bold; }
        .weak { color: red; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.toast(f"💖 **Welcome, {st.session_state['username']}!** to HG password generator website!")

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

# st.header("🔐 HG Password Strength Meter ")
st.title("🔐 HG Password Strength Meter")

# ---- USER INPUT ----
password = st.text_input("🔑 **Enter your password:**", type="password")

if password:
    with st.spinner("Checking password strength..."):
        time.sleep(1.5)  # Simulate processing time
    
    # Avoid duplicate passwords in history
    if not st.session_state['password_history'] or st.session_state['password_history'][-1] != password:
        st.session_state['password_history'].append(password)

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
if st.session_state['password_history']:
    st.sidebar.subheader("📝 Password History")
    for i, past_password in enumerate(reversed(st.session_state['password_history'][-5:]), 1):
        st.sidebar.text(f"{i}. {past_password}")

# import streamlit as st
st.title("")

st.subheader("💡 FAQ - Toggle Question Answer")

# List of Questions and Answers
faq = [
    ("What is a strong password?", "A strong password contains at least 8 characters, uppercase & lowercase letters, numbers, and special symbols."),
    ("How do I reset my password?", "You can reset your password by clicking on the 'Forgot Password' link on the login page."),
    ("Why is password security important?", "Password security is crucial to protect your personal and sensitive information from unauthorized access."),
]

# Display each question inside an expander (toggle)
for question, answer in faq:
    with st.expander(question):
        st.write(answer)

# st.sidebar.image("sidebar.png")
st.markdown("""
    <style>
        .footer {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #433f40;
            margin-top: 20px;
        }
    </style>
    <p class='footer'>💛🅲🆁🅴🅰🆃🅴🅳 🅱🆈 🅷🅰🅳🅸🆀🅰 🅶🅾🅷🅰🆁💛</p>
""", unsafe_allow_html=True)

time.sleep(2)  # Delay before showing the toast
st.toast("⚠️ **Use at least:** 8 characters, Uppercase, Lowercase, Number & Special Symbol!")
