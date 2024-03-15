import streamlit as st
import pandas as pd
import folium
import streamlit_folium
from streamlit_folium import folium_static
import os
import requests
import json

password1 = 'DRZ'
password2 = 'drz'
password3 = 'Drz'

bb = st.text_input("Complete the number plate: KS62 '____'")

if bb == password1 or bb == password2 or bb == 'Drz':

  st.write("### WELL DONE! MESSAGE REESE THE WORD 'DOOMSDAY' FOR FURTHER INSTRUCTION")

  st.markdown("![GIF](https://media.giphy.com/media/rIdj5s9Ead7osqcuih/giphy.gif)")
