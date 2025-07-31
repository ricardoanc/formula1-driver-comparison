import streamlit as st
import fastf1 as ff1
import pandas as pd

year = st.selectbox(
    'Select the racing season:',
    ('2025','2024','2023','2022','2021','2020'),
)

st.write(f'SEASON {year}')

driver1 = st.selectbox(
    'Select the driver to compare:',
    ('1','2','3','4','5','6'),
)

driver2 = st.selectbox(
    'Select the driver to compare:',
    ('1','2','3','4','5','6'),
)