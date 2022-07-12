import streamlit as st

with st.form("Test"):


    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("col1")
        st.form_submit_button("Button 1")
    with col2:
        st.write("col2")
        st.form_submit_button("Button 2")
    with col3:
        st.write("col3")
        st.form_submit_button("Button 3")        