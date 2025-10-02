import streamlit as st

# --- Simple user credentials ---
USERS = {
    "alice": "password123",
    "bob": "qwerty",
}

# --- Initialize session state ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False


# --- Login screen ---
def login():
    st.title("🔑 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")


# --- Quiz screen ---
def quiz():
    st.title("📝 Simple Quiz")

    question = "What is the capital of France?"
    options = ["Berlin", "Madrid", "Paris", "Rome"]

    st.write("**Question:**", question)

    answer = st.radio("Choose your answer:", options, index=None)

    if st.button("Submit Answer") and not st.session_state.answered:
        if answer == "Paris":
            st.success("Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error("Wrong answer ❌")
        st.session_state.answered = True

    st.write(f"Your Score: {st.session_state.score}")


# --- Main app flow ---
if not st.session_state.logged_in:
    login()
else:
    quiz()

