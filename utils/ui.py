import streamlit as st
from streamlit_elements import elements, mui

APP_TITLE = 'Streamlit Material UI'

def display_header(subheader=None):
    st.title(APP_TITLE)
    if subheader:
        st.subheader(subheader)

def display_mui_elements(name, code):
    uiTab, codeTab = st.tabs([name, "Code"])
    with uiTab:
        with elements(name):
            with mui.Stack(spacing=2, padding=1, direction='row'):
                exec(code)
    with codeTab:
        st.code(code)