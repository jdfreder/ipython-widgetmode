
from IPython.display import display, Javascript

def widgetmode():
    with open('./static/widgetmode.js', 'r') as f:
        display(Javascript(data=f.read()))