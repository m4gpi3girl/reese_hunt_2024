
import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(page_title="Home", initial_sidebar_state="expanded")

st.title('Reese hunt')

st.subheader("The hunt is simple: answer a question to reveal the location. answer a question specific to the location to access the next location. repeat x4")

st.write("# Location 1:")
answer_1_a = 5
answer_1_b = 'five'
answer_1_c = 'Five'
answer_1_d = '5'

bar = st.text_input('How many toes does the Dorking cockeral have?')
k = st.button('Reveal first location')

location_2_locked = True

if k:
    if bar == answer_1_a or bar == answer_1_b or bar == answer_1_c or bar == answer_1_d:
        st.success("Meadowbank Park, coords 51.2342591, -0.3317815")
        st.success("Apple Maps link: https://maps.apple.com/?ll=51.235197,-0.331297&q=Marked%20Location&_ext=EiYp3bpRC3adSUAx1LMKte2v1b85W5B3Z5yeSUBBEr3szt3E1L9QBA%3D%3D&t=m ")
        st.warning("To unlock Location 2, find the surname: Barney '____'")
        coords = [51.2342591, -0.3317815]
        loc_1 = folium.Map(location=coords, zoom_start=17)
        folium.Marker(location=coords, popup="Dorking RH4 1JE").add_to(loc_1)
        folium_static(loc_1)