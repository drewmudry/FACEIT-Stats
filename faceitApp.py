import streamlit as st
import requests
import json
import numpy as np
import pandas as pd

# Faceit stats tracker
# Step 1: Program gets a faceit user's name and looks them up by using the faceit api. 
# Step 2: Then we retrieve the last 20 matches of the player. 

st.title("FACEIT STAT TRACKER")
username = st.text_input("Enter your FaceIT profile name.")
api_key = "833d66a2-9853-43a5-9644-1193780aec85"

#request user info from API 
playerRequest = requests.get("https://open.faceit.com/data/v4/players?nickname="+username+"&game=CSGO",headers={"Authorization":"Bearer "+api_key,"Content-Type":"application/json"})
matchRequest = requests.get("https://open.faceit.com/data/v4/players/"+"cuckme_"+"/history?game=csgo&offset=0&limit=20",headers={"Authorization":"Bearer "+api_key,"Content-Type":"application/json"})

st.markdown(matchRequest)



