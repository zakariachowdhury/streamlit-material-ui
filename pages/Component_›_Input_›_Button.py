import streamlit as st
from utils import ui

def main():
    ui.display_header(subheader='Button')

    ui.display_mui_elements('Basic Button', '''mui.Button('Text', variant='text')
mui.Button('Contained', variant='contained')
mui.Button('Outlined', variant='outlined')
''')

    ui.display_mui_elements('Text Button', '''mui.Button('Primary')
mui.Button('Disabled', disabled=True)
mui.Button('Link', href='https://www.streamlit.io', target='_blank')
''')

    ui.display_mui_elements('Contained Button', '''mui.Button('Contained', variant='contained')
mui.Button('Disabled', variant='contained', disabled=True)
mui.Button('Link', variant='contained', href='https://www.streamlit.io', target='_blank')
mui.Button('Disabled Elevation', variant='contained', disableElevation=True)
''')

    ui.display_mui_elements('Outlined Button', '''mui.Button('Primary', variant='outlined')
mui.Button('Disabled', variant='outlined', disabled=True)
mui.Button('Link', variant='outlined', href='https://www.streamlit.io', target='_blank')    
''')

    ui.display_mui_elements('Handling Clicks', '''def onClick():
    print('Clicked')

mui.Button('Click me', variant='contained', onClick=onClick)
''')

    ui.display_mui_elements('Color', '''mui.Button('Primary', color='primary')
mui.Button('Success', color='success', variant='contained')
mui.Button('Error', color='error', variant='outlined')
''')


    ui.display_mui_elements('Icon & Label', '''mui.Button('Delete', startIcon=mui.icon.Delete, variant='outlined')
mui.Button('Send', endIcon=mui.icon.Send, variant='contained')
''')

    ui.display_mui_elements('Icon Button', '''mui.IconButton(mui.icon.Delete, color="inherit", label="delete")
mui.IconButton(mui.icon.Delete, color="primary", label="delete", disabled=True)
mui.IconButton(mui.icon.Alarm, label="alarm")
mui.IconButton(mui.icon.AddShoppingCart, color="primary", label="add to shopping cart")
''')
    

if __name__ == '__main__':
    main()