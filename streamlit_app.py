import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Chemicals usage tracking app
"""
data = pd.read_csv('data.csv')
st.text(data)

usage = st.number('usage in ml')
