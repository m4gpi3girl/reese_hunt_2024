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

bb = st.text_input("Complete the number plate: KS62 '____'")

if bb == password1 or bb == password2:

  st.write("### WELL DONE! MESSAGE REESE THE WORD 'DOOMSDAY' FOR FURTHER INSTRUCTION")
