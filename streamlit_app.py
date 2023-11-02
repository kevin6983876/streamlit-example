import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Chemicals usage tracking app
"""
data = pd.read_csv('data.csv', sep=',')

usage = st.number_input('usage in ml', value = 0.0)
buy = st.number_input('newly added', value = 0.0)


