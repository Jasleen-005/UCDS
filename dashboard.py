import streamlit as st
 
 
def dashboard_page():

    st.set_page_config(page_title="Dashboard", page_icon="📄", layout="wide")
 
    st.title("📄 Unified Citizen Document System")

    st.subheader("Citizen Dashboard")
 
    st.markdown("---")
 
    # Top summary cards

    col1, col2, col3 = st.columns(3)
 
    with col1:

        st.info("Total Documents\n\n8")
 
    with col2:

        st.success("Verified Documents\n\n6")
 
    with col3:

        st.warning("Pending Verification\n\n2")
 
    st.markdown("---")
 
    # Document section

    st.markdown("### My Documents")
 
    documents = [

        {"Document Name": "Aadhaar Card", "Status": "Verified"},

        {"Document Name": "PAN Card", "Status": "Verified"},

        {"Document Name": "Passport", "Status": "Pending"},

        {"Document Name": "Driving License", "Status": "Verified"},

    ]
 
    st.table(documents)
 
    st.markdown("---")
 
    # Search documents

    st.markdown("### Search Document")

    search = st.text_input("Enter document name")
 
    if st.button("Search"):

        if search:

            st.success(f"Showing results for: {search}")

        else:

            st.error("Please enter a document name")
 
    st.markdown("---")
 
    # Logout

    if st.button("Logout"):

        st.success("Logged out successfully")
 
 
if __name__ == "__main__":

    dashboard_page()

 
