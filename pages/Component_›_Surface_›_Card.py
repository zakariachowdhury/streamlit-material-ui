import streamlit as st
from utils import ui

def main():
    ui.display_header(subheader='Card')

    ui.display_mui_elements('Basic Card', '''
with mui.Card(sx={"minWidth": "275px"}):
    with mui.CardContent():
        mui.Typography('Word of the Day', sx={'fontSize': 14}, color="text.secondary", gutterBottom=True)
        mui.Typography('be•nev•o•lent', variant='h5', component='div')
        mui.Typography('adjective', sx={ 'mb': 1.5 }, color="text.secondary")
        mui.Typography('well meaning and kindly. "a benevolent smile"', variant='body2')
    with mui.CardActions():
        mui.Button('Learn More', size='small')
''')

    ui.display_mui_elements('Outlined Card', '''
with mui.Card(sx={"minWidth": "275px"}, variant='outlined'):
    with mui.CardContent():
        mui.Typography('Word of the Day', sx={'fontSize': 14}, color="text.secondary", gutterBottom=True)
        mui.Typography('be•nev•o•lent', variant='h5', component='div')
        mui.Typography('adjective', sx={ 'mb': 1.5 }, color="text.secondary")
        mui.Typography('well meaning and kindly. "a benevolent smile"', variant='body2')
    with mui.CardActions():
        mui.Button('Learn More', size='small')
''')

    ui.display_mui_elements('UI Controls', '''
with mui.Card(sx={"display": "flex"}):
    with mui.Box(sx={"display": "flex", "flexDirection": "column"}):
        with mui.CardContent(sx={"flex": "1 0 auto"}):
            mui.Typography('Live From Space', component='div', variant='h5')
            mui.Typography('Mac Miller', component='div', variant='subtitle1', color="text.secondary")
        with mui.Box(sx={"display": "flex", "alignItems": "center", "pl": 1, "pb": 1}):
            with mui.IconButton(label="Previous"):
                mui.icon.SkipPrevious()
            with mui.IconButton(label="Play/Pause"):
                mui.icon.PlayArrow(sx={"height": "38px", "width": "38px"})
            with mui.IconButton(label="Next"):
                mui.icon.SkipNext()
    mui.CardMedia(component="img", sx={"width": 151}, image="https://material-ui.com/static/images/cards/live-from-space.jpg", title="Live from space album cover")
''')
if __name__ == '__main__':
    main()