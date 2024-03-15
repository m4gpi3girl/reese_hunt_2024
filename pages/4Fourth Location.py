import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

apassword = "Never Forgotten"
bpassword = "never forgotten"
cpassword = "never Forgotten"
dpassword = 'Never forgotten'

test = st.text_input("What is the rest of the quote?")

if test == apassword or test == bpassword or test == cpassword or test == dpassword:

    st.success("Congrats, you made it! Now, answer the following question to reveal the next location..")

    answer_4_a = 'Morgan'
    answer_4_b = 'morgan'
    answer_4_c = 'morgans'


    bar = st.text_input("Who's Reeses captain??")
    if st.button('Reveal fourth location'):
        if bar == answer_4_a or bar == answer_4_b or bar == answer_4_c:
            st.success("Meadowbank Park, coords 51.2336990, -0.3330767")
            st.success("Apple Maps link: https://maps.apple.com/place?q=Marked%20Location&ll=51.234566%2C-0.33217&address=Meadowbank%2C%20Mill%20Lane%2C%20Dorking%2C%20RH4%201DX%2C%20England")
            st.warning("To unlock Location 5, finish the quote: Complete the number plate: KS62 '____'")
            coords = [51.2336990, -0.3330767]
            loc_3 = folium.Map(location=coords, zoom_start=17)
            folium.Marker(location=coords, popup="Dorking RH4 1").add_to(loc_3)
            folium_static(loc_3)

        else:
            st.warning("Wrong! Try again.")