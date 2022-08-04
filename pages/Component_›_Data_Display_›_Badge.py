import streamlit as st
from utils import ui

def main():
    ui.display_header(subheader='Badge')

    ui.display_mui_elements(name='Basic Badge', code='''
with mui.Badge(badgeContent=120, max=99, color='primary'):
    mui.icon.Mail()

with mui.Badge(badgeContent=3, overlap='circular', color='success', anchorOrigin={"vertical": "bottom", "horizontal": "right"}):
    mui.Avatar(src='https://material-ui.com/static/images/avatar/1.jpg', alt='Avatar', color='inherit')
''')

    ui.display_mui_elements(name='Dot Badge', code='''
with mui.Badge(color='primary', variant='dot'):
    mui.icon.Mail()
''')

    

if __name__ == '__main__':
    main()