import streamlit as st
import fastf1 as ff1
import functions

ff1.Cache.enable_cache('./cache')

year = st.selectbox(
    'Select the racing season:',
    ('2024',
     '2023',
     '2022',
     '2021',
     '2020',
     '2019',
     '2018',
     '2017')
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

# year, driver1, driver2 = 2022, 'VER', 'ALO'

winners = functions.get_race_winners(year)
pole_winners = functions.get_pole_winners(year)

driver1_wins = functions.count_wins(driver1, winners)
driver2_wins = functions.count_wins(driver2, winners)

driver1_poles = functions.count_wins(driver1, pole_winners)
driver2_poles = functions.count_wins(driver2, pole_winners)

# print(f'{driver1} wins in {year}: {driver1_wins}')
# print(f'{driver2} wins in {year}: {driver2_wins}')

st.write(f'{driver1} had {driver1_wins} wins in season {year}.\n While {driver2} had {driver2_wins} wins.\n\n')
st.write(f'{driver1} had {driver1_poles} pole positions in season {year}.\n While {driver2} had {driver2_poles} pole positions.')

