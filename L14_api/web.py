"""
Streamlit example

To run: python -m streamlit run web.py
"""

import streamlit as st

import nasaapi

##############################

info: nasaapi.NasaPic = nasaapi.get_pic_info(True)

st.title(info.title)
st.subheader(info.date)

st.image(info.url)

st.text(info.explanation)
