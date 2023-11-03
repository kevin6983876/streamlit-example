import numpy as np
import pandas as pd
import streamlit as st
import datetime

"""
# Chemicals usage tracking app
"""
operation = st.selectbox('Operation',('Experiment', 'Purchase', 'Check stock'))
st.write('---')
if operation == 'Experiment':
    sample = st.number_input('Sample/Detector Diluent (ml)', 0)                                      
    bead = st.number_input('Bead diluent (ml)', 0)
    SBG_diluent = st.number_input('SBG diluent (ml)',0)
    SBG_concentrate = st.number_input(r'SBG concentrate ($\mu$l)',0)
    disc = st.number_input('Disc',0)
    plate = st.number_input('Plate',0)
    RGP = st.number_input('RGP (bottle)', 0)
    wash_buffer_A = st.number_input('Wash buffer A (pack)',0)
    wash_buffer_B = st.number_input('Wash buffer B (pack)',0)
if operation == 'Purchase':
    sample = st.number_input('Sample/Detector Diluent (ml)', 0.0)                                      
    bead = st.number_input('Bead diluent (ml)', 0.0)
    SBG_diluent = st.number_input('SBG diluent (ml)',0.0)
    SBG_concentrate = st.number_input(r'SBG concentrate ($\mu$l)',0.0)
    disc = st.number_input('Disc',0)
    plate = st.number_input('Plate',0)
    RGP = st.number_input('RGP (bottle)', 0)
    wash_buffer_A = st.number_input('Wash buffer A (pack)',0)
    wash_buffer_B = st.number_input('Wash buffer B (pack)',0)
if operation == 'Check stock':
    sample = st.number_input('Sample/Detector Diluent (ml)', 0.0)                                      
    bead = st.number_input('Bead diluent (ml)', 0.0)
    SBG_diluent = st.number_input('SBG diluent (ml)',0.0)
    SBG_concentrate = st.number_input(r'SBG concentrate ($\mu$l)',0.0)
    disc = st.number_input('Disc',0)
    plate = st.number_input('Plate',0)
    RGP = st.number_input('RGP (bottle)', 0)
    wash_buffer_A = st.number_input('Wash buffer A (pack)',0)
    wash_buffer_B = st.number_input('Wash buffer B (pack)',0)
submit = st.button('submit')
if submit:
    pass

data = pd.read_csv('data.csv', sep=',')
current_datetime = datetime.datetime.now()
current_date = current_datetime.date()
current_time = current_datetime.time()

st.dataframe(data)