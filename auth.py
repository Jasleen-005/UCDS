import streamlit as st # type: ignore

def login_page():
    st.title("Login")
    st.subheader("Unified Citizen Document System")

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown("### Login with OTP")
            email = st.text_input("Email")
            otp = st.text_input("Enter OTP")

            if st.button("Send OTP", use_container_width=True):
                if email:
                    st.success("OTP sent successfully")
                else:
                    st.error("Please enter your email")

            if st.button("Login", use_container_width=True):
                if email and otp:
                    st.success("Login Successful")
                else:
                    st.error("Please enter email and OTP")

            st.markdown("---")

            if st.button("Create New Account"):
                st.session_state.page = "signup"
                st.rerun()

def signup_page():
    st.title("Signup")
    st.subheader("Create Your Account")

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            full_name = st.text_input("Full Name")
            email = st.text_input("Email")
            otp = st.text_input("Enter OTP")

            if st.button("Send OTP", use_container_width=True):
                if full_name and email:
                    st.success("OTP sent successfully")
                else:
                    st.error("Please fill name and email first")

            if st.button("Signup", use_container_width=True):
                if not full_name or not email or not otp:
                    st.error("Please complete all fields")
                else:
                    st.success("Account Created Successfully")

            st.markdown("---")

            if st.button("Back to Login"):
                st.session_state.page = "login"
                st.rerun()