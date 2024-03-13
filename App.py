
import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json


st.set_page_config(page_title="Home", initial_sidebar_state="expanded")

st.title('Reese hunt')


st.sidebar.write('Link to location pages')

st.subheader('Answer correctly to reveal the location')

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


