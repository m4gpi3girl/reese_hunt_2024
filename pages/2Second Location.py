import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

password = 'tbc'

test = st.text_input("What is the answer to x?")

if test == password:

    st.success("Congrats you made it. Now answer the following to reveal the next location..")

    answer_1_a = 'paris'
    answer_1_b = 'Paris'

    bar = st.text_input('What is the capital of France?')
    if st.button('Reveal first location'):
        if bar == answer_1_a or bar == answer_1_b:
            st.success("Meadowbank Park, coords 51.235214, -0.331248")
            coords = [51.235214, -0.331248]
            m = folium.Map(location=coords, zoom_start=17)
            folium.Marker(location=coords, popup="Location 1").add_to(m)
            folium_static(m)
        else:
            st.warning("Wrong! Try again.")