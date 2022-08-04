import streamlit as st
from utils import ui

def main():
    ui.display_header(subheader='Card')

    st.write('Cards contain content and actions about a single subject.')
    st.caption('Cards are surfaces that display content and actions on a single topic. They should be easy to scan for relevant and actionable information. Elements, like text and images, should be placed on them in a way that clearly indicates hierarchy.')

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

    ui.display_mui_elements('Complex Interaction', '''
with mui.Card(sx={"maxWidth": "345px"}):
    mui.CardHeader(
        title="Shrimp and Chorizo Paella",
        subheader="September 14, 2016",
        avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
        action=mui.IconButton(mui.icon.MoreVert)
    )
    mui.CardMedia(
        component="img",
        height=194,
        image="https://mui.com/static/images/cards/paella.jpg",
        alt="Paella dish",
    )
    with mui.CardContent(sx={"flex": 1}):
        mui.Typography("This impressive paella is a perfect party dish and a fun meal to cook together with your guests. Add 1 cup of frozen peas along with the mussels, if you like.", variant="body2", color="text.secondary")
    with mui.CardActions(disableSpacing=True):
        mui.IconButton(mui.icon.Favorite)
        mui.IconButton(mui.icon.Share)
''')

    ui.display_mui_elements('Media', '''
with mui.Card(sx={"maxWidth": "345px"}):
    mui.CardMedia(
        component="img",
        height=140,
        image="https://mui.com/static/images/cards/contemplative-reptile.jpg",
        alt="Green Iguana",
    )
    with mui.CardContent(sx={"flex": 1}):
        mui.Typography("Lizard", variant="h5", component="div", gutterBottom=True)
        mui.Typography("Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica", variant="body2", color="text.secondary")
    with mui.CardActions(disableSpacing=True):
        mui.Button("Share", size="small")
        mui.Button("Learn More", size="small")
''')

    ui.display_mui_elements('Primary Action', '''
with mui.Card(sx={"maxWidth": "345px"}):
    with mui.CardActionArea(onClick=lambda: print('You clicked the card.')):
        mui.CardMedia(
            component="img",
            height=140,
            image="https://mui.com/static/images/cards/contemplative-reptile.jpg",
            alt="Green Iguana",
        )
        with mui.CardContent(sx={"flex": 1}):
            mui.Typography("Lizard", variant="h5", component="div", gutterBottom=True)
            mui.Typography("Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica", variant="body2", color="text.secondary")
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