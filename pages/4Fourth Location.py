import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

password = 123

test = st.text_input("Who's Reeses captain??")

if test == password:

    st.success("Congrats, you made it! Now, answer the following question to reveal the next location..")

    answer_4_a = 'Morgan'
    answer_4_b = 'morgan'
    answer_4_c = 'morgans'


    bar = st.text_input('Which ear does Reese have pierced, left or right?')
    if st.button('Reveal first location'):
        if bar == answer_4_a or bar == answer_4_b or bar == answer_4_c:
            st.success("Meadowbank Park, coords 51.235214, -0.331248")
            st.success("Apple Maps link: https://maps.apple.com/place?q=Marked%20Location&ll=51.234566%2C-0.33217&address=Meadowbank%2C%20Mill%20Lane%2C%20Dorking%2C%20RH4%201DX%2C%20England")
            coords = [51.235214, -0.331248]
            loc_3 = folium.Map(location=coords, zoom_start=17)
            folium.Marker(location=coords, popup="Dorking RH4 1").add_to(loc_3)
            folium_static(loc_3)
        else:
            st.warning("Wrong! Try again.")