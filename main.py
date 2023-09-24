import streamlit as st

# Define a list of valid users and passwords
users = ["user1", "user2"]
passwords = ["password1", "password2"]

# Create a login form
with st.form("login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")

# Validate the login credentials
if submit_button and username in users and password == passwords[users.index(username)]:
    # Login successful
    st.success("Login successful")

else:
    # Login failed
    st.error("Login failed")
