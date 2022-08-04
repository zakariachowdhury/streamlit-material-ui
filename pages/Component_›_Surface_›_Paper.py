import streamlit as st
from utils import ui

def main():
    ui.display_header(subheader='Paper')

    st.write('In Material Design, the physical properties of paper are translated to the screen.')
    st.caption("The background of an application resembles the flat, opaque texture of a sheet of paper, and an application's behavior mimics paper's ability to be re-sized, shuffled, and bound together in multiple sheets.")

    ui.display_mui_elements('Basic Paper', '''
with mui.Box(sx={'display': 'flex',
        'flexWrap': 'wrap',
        '& > :not(style)': {
          'm': 1,
          'width': 128,
          'height': 128
        }}):
    mui.Paper(elevation=0)
    mui.Paper()
    mui.Paper(elevation=3)
    mui.Paper(elevation=6)
    mui.Paper(elevation=9)
    mui.Paper(elevation=12)
    mui.Paper(elevation=16)
    mui.Paper(elevation=24)
''')

    ui.display_mui_elements('Variants', '''
with mui.Box(sx={'display': 'flex',
        'flexWrap': 'wrap',
        '& > :not(style)': {
          'm': 1,
          'width': 128,
          'height': 128
        }}):    
    mui.Paper(variant='outlined')
    mui.Paper(variant='outlined', square=True)
''')

if __name__ == '__main__':
    main()