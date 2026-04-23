import streamlit as st # type: ignore
from auth import login_page, signup_page

st.set_page_config(
    page_title="Unified Citizen Document System",
    page_icon="📄",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "login"

if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "signup":
    signup_page()
