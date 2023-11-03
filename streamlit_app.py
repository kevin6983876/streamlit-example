import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Chemicals usage tracking app
"""
operation = st.selectbox('Operation',('Experiment, Purchase, Check stock))
if operation == 'Experiment':
    sample = st.number_input('Sample/Detector Diluent (ml)', 0.0)                                      
    bead = st.number_input('Bead diluent (ml)', 0.0)
data = pd.read_csv('data.csv', sep=',')
st.write('### Current deposit')
st.dataframe(data)

date = st.text_input('Date(dd/mm/yyyy)')
usage = st.number_input('usage in ml', value = 0.0)
buy = st.number_input('newly added', value = 0.0)
reset = st.number_input('reset', value = 0.0)

option = st.button('submit')
