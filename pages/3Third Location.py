import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

apassword = 'Smith'
bpassword = 'SMITH'
cpassword =  'smith'

test = st.text_input("What is surname?")

if test == apassword or test == bpassword or test == cpassword:

    st.success("Congrats, you made it! Now, answer the following question to reveal the next location..")

    answer_3_a = 'meadowbank'
    answer_3_b = 'Meadowbank'
    answer_3_c = 'meadow bank'
    answer_3_d = 'Meadow Bank'
    answer_3_e = 'Meadow bank'
    answer_3_f = 'meadow Bank'

    bar = st.text_input('What field did Reese have his first bong?')
    if st.button('Reveal third location'):
        if bar == answer_3_a or bar == answer_3_b or bar == answer_3_c or bar == answer_3_d or bar == answer_3_e or bar == answer_3_f:
            st.success("Meadowbank Park, coords 51.2356060, -0.3301243")
            st.success("Apple Maps link: https://maps.apple.com/place?q=Marked%20Location&ll=51.234566%2C-0.33217&address=Meadowbank%2C%20Mill%20Lane%2C%20Dorking%2C%20RH4%201DX%2C%20England")
            st.warning("To unlock Location 2, finish the quote: Loved and Missed, '____'")
            coords = [51.2356060, -0.3301243]
            loc_3 = folium.Map(location=coords, zoom_start=17)
            folium.Marker(location=coords, popup="Dorking RH4 1").add_to(loc_3)
            folium_static(loc_3)
        else:
            st.warning("Wrong! Try again.")