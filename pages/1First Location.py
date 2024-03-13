
import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

answer_1_a = 'paris'
answer_1_b = 'Paris'

bar = st.text_input('What is the capital of France?')
if st.button('Reveal first location'):
    if bar == answer_1_a or bar == answer_1_b:
        st.success("Meadowbank Park, coords 51.235214, -0.331248")
        st.success("Apple Maps link: https://maps.apple.com/?ll=51.235197,-0.331297&q=Marked%20Location&_ext=EiYp3bpRC3adSUAx1LMKte2v1b85W5B3Z5yeSUBBEr3szt3E1L9QBA%3D%3D&t=m ")
        coords = [51.235214, -0.331248]
        m = folium.Map(location=coords, zoom_start=17)
        folium.Marker(location=coords, popup="Dorking RH4 1JE").add_to(m)
        folium_static(m)
    else:
        st.warning("Wrong! Try again.")