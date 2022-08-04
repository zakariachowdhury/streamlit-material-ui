import streamlit as st
from utils import ui

def main():
    ui.display_header(subheader='Avatar')

    ui.display_mui_elements(name='Image Avatar', code='''
mui.Avatar(alt='Remy Sharp', src='https://material-ui.com/static/images/avatar/1.jpg')
mui.Avatar(alt='Travis Howard', src='https://material-ui.com/static/images/avatar/2.jpg')
mui.Avatar(alt='Cindy Baker', src='https://material-ui.com/static/images/avatar/3.jpg')
''')

    ui.display_mui_elements(name='Letter Avatar', code='''
mui.Avatar('H')
mui.Avatar('N', sx={'bgcolor': 'orange'})
mui.Avatar('OP', sx={'bgcolor': 'purple'})
''')

    ui.display_mui_elements(name='Sizes', code='''
mui.Avatar(alt='Remy Sharp', sx={'width': 24, 'height': 24}, src='https://material-ui.com/static/images/avatar/1.jpg')
mui.Avatar(alt='Remy Sharp', src='https://material-ui.com/static/images/avatar/1.jpg')
mui.Avatar(alt='Remy Sharp', sx={'width': 56, 'height': 56}, src='https://material-ui.com/static/images/avatar/1.jpg')
''')

    ui.display_mui_elements(name='Icon Avatar', code='''
mui.Avatar(mui.icon.Folder)
mui.Avatar(mui.icon.Pageview, sx={'bgcolor': 'pink'})
mui.Avatar(mui.icon.Assignment, sx={'bgcolor': 'green'})
''')

    ui.display_mui_elements(name='Variants', code='''
mui.Avatar('N', variant='square', sx={'bgcolor': 'orange'})
mui.Avatar(mui.icon.Assignment, variant='rounded', sx={'bgcolor': 'green'})
''')

    ui.display_mui_elements(name='Grouped', code='''
with mui.AvatarGroup(max=4, total=20):
    mui.Avatar(alt='Remy Sharp', src='https://material-ui.com/static/images/avatar/1.jpg')
    mui.Avatar(alt='Travis Howard', src='https://material-ui.com/static/images/avatar/2.jpg')
    mui.Avatar(alt='Cindy Baker', src='https://material-ui.com/static/images/avatar/3.jpg')
    mui.Avatar(alt='Agnes Walker', src='https://material-ui.com/static/images/avatar/4.jpg')
    mui.Avatar(alt='Trevor Hansen', src='https://material-ui.com/static/images/avatar/5.jpg')
''')
    

if __name__ == '__main__':
    main()