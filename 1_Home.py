import streamlit as st
from utils import ui

def main():
    st.set_page_config(page_title='Material UI', initial_sidebar_state='expanded')
    ui.display_header()

    code = '''
from streamlit_elements import elements, mui

with elements('new_element'):
    # Add your MUI code here
    mui.Button('Click Me', variant='contained')
'''
    codeTab, uiTab = st.tabs(['How To Use', 'Output'])
    with codeTab:
        st.code('''pip install streamlit --upgrade
pip install streamlit-elements==0.1.*''')
        st.code(code)
    with uiTab:
        exec(code)
    

if __name__ == '__main__':
    main()