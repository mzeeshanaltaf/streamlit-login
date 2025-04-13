import streamlit as st
from util import *

# Page title of the application
page_title = "Streamlit Login"
page_icon = "🔒"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Application Title and description
st.title(f'{page_title}{page_icon}')
st.write('***:blue[🔐 Secure Google Login → 🚀 One-Click Access → 🏃 Quick Logout]***')
st.write("""
*This app lets users log in instantly with their Google account—no passwords needed! Enjoy a frictionless, 
secure authentication experience with just a click. Log out anytime with ease. Perfect for apps prioritizing 
speed & simplicity! 🎯✨*
""")

# Display footer in the sidebar
display_footer()

if not st.experimental_user.is_logged_in:
    login = st.button("Login", icon=":material/login:")
    if login:
        st.login("google")

if st.experimental_user.is_logged_in:
    st.header(f"Hello {st.experimental_user.name}")
    st.image(st.experimental_user.picture)
    logout = st.button("Logout", icon=":material/logout:")
    if logout:
        st.logout()



