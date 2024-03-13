import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

password = '123'

test = st.text_input("What is the answer to x?")

if test == password:

    st.success("Congrats, you made it! Now, answer the following question to reveal the next location..")

    answer_2_a = 'left'
    answer_2_b = 'Left'

    bar = st.text_input('Which ear does Reese have pierced, left or right?')
    if st.button('Reveal first location'):
        if bar == answer_2_a or bar == answer_2_b:
            st.success("Meadowbank Park, coords 51.235214, -0.331248")
            st.success("Apple Maps link: https://maps.apple.com/place?address=Dorking,%20RH4%201,%20England&auid=9711118407415029721&ll=51.241128,-0.307572&lsp=7618&q=RH4%201&t=m")
            coords = [51.235214, -0.331248]
            loc_2 = folium.Map(location=coords, zoom_start=17)
            folium.Marker(location=coords, popup="Dorking RH4 1").add_to(loc_2)
            folium_static(loc_2)
        else:
            st.warning("Wrong! Try again.")