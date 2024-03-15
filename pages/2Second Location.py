import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

apassword = 'Harwood'
bpassword = 'HARWOOD'
cpassword = 'harwood'

test = st.text_input("What is the surname?")

if test == apassword or test == bpassword or test == cpassword:

    st.success("Congrats, you made it! Now, answer the following question to reveal the next location..")

    answer_2_a = 'left'
    answer_2_b = 'Left'

    bar = st.text_input('Which ear does Reese have pierced, left or right?')
    if st.button('Reveal second location'):
        if bar == answer_2_a or bar == answer_2_b:
            st.success("Meadowbank Park, coords 51.2356060, -0.3323398")
            st.success("Apple Maps link: https://maps.apple.com/?ll=51.235197,-0.331297&q=Marked%20Location&_ext=EiYp3bpRC3adSUAx1LMKte2v1b85W5B3Z5yeSUBBEr3szt3E1L9QBA%3D%3D&t=m ")
            st.warning("To unlock Location 3, find the surname: Brian and Betty '____'")
            coords = [51.2356060, -0.3323398]
            loc_2 = folium.Map(location=coords, zoom_start=17)
            folium.Marker(location=coords, popup="Dorking RH4 1").add_to(loc_2)
            folium_static(loc_2)
        else:
            st.warning("Wrong! Try again.")