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

  st.markdown("<iframe src="https://giphy.com/embed/rIdj5s9Ead7osqcuih" width="480" height="412" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/friends-butterfly-bees-rIdj5s9Ead7osqcuih">via GIPHY</a></p>")
