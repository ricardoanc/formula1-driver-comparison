import streamlit as st
import fastf1 as ff1
import functions

year = st.selectbox(
    'Select the racing season:',
    ('2025','2024','2023','2022','2021','2020'),
)

st.write(f'SEASON {year}')

driver1 = st.selectbox(
    'Select Driver 1:',
    ('VER','PER','SAI','LEC','RUS','ALO'),
)

driver2 = st.selectbox(
    'Select Driver 2:',
    ('VER','PER','SAI','LEC','RUS','ALO'),
)

df = functions.get_race_winners(year)

driver1_wins = functions.count_wins(racer=driver1)
driver2_wins = functions.count_wins(racer=driver2)

st.write(f'{driver1} wins in {year}: {driver1_wins}')
st.write(f'{driver2} wins in {year}: {driver2_wins}')