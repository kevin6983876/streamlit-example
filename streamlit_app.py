import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Chemicals usage tracking app
"""
data = pd.read_csv('data.csv', sep=',')

date = st.text_input('Date(dd/mm/yyyy)')
usage = st.number_input('usage in ml', value = 0.0)
buy = st.number_input('newly added', value = 0.0)
reset = st.number_input('reset', value = 0.0)

st.button('submit')
