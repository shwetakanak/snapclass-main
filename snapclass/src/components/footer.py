import streamlit as st

def footer_home():
    logo_url="https://github.com/shwetakanak/project_aiml/blob/3aa0a1116c69108d36756853f8a36cf44938632d/images/Gemini_Generated_Image_8axdxx8axdxx8axd.png?raw=true"
    st.markdown(f"""
                <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center;items-align:center;">
                <p style="font-weight:bold;color:white;">Created with ❤️ by </p>
                <img src='{logo_url}' style='max-height:25px'/>
                </div>
                """,unsafe_allow_html=True)
def footer_dashboard():
    logo_url="https://github.com/shwetakanak/project_aiml/blob/3aa0a1116c69108d36756853f8a36cf44938632d/images/Gemini_Generated_Image_8axdxx8axdxx8axd.png?raw=true"
    st.markdown(f"""
                <div style="margin-top:2rem;display:flex;gap:6px;justify-content:center;items-align:center;">
                <p style="font-weight:bold;color:black;">Created with ❤️ by </p>
                <img src='{logo_url}' style='max-height:25px'/>
                </div>
                """,unsafe_allow_html=True)