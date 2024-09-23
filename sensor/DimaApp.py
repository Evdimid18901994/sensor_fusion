import streamlit as st
from streamlit_navigation_bar import st_navbar
from Pages import Brosay, Andreich, Gusmanych, Valentinich, Dima
import streamlit_navigation_bar



st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Дима","Андреич", 'Все бросайте', 'Гусманыч', 'Валентиныч']

styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(105, 114, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}
page = st_navbar(pages, styles = styles)

if page == 'Дима':
    Dima.Dima().app()

elif page == "Андреич":
    Andreich.Andreich().app()

elif page == "Все бросайте":
    Brosay.Brosay().app()

elif page == "Гусманыч":
    Gusmanych.Gus().app()

elif page == "Валентиныч":
    Valentinich.Vale().app()

with st.sidebar:
    st.write("Sidebar")





