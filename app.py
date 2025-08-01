import streamlit as st
import fastf1 as ff1
import functions
import time

ff1.Cache.enable_cache('./cache')

years = ['Select...'] + [str(y) for y in range(1950, 2025)]

year = st.selectbox(
    'Select the racing season:',
    years
)

st.write(f'SEASON {year}')

if year != 'Select...':
    drivers = functions.get_drivers(year)


driver1 = st.selectbox(
    'Select Driver 1:',
    drivers
)

driver2 = st.selectbox(
    'Select Driver 2:',
    drivers
)

# year, driver1, driver2 = 2024, 'VER', 'ALO'

if year != 'Select...' and driver1 != 'Select...' and driver2 != 'Select...':
    st.write(f"SEASON {year}: Comparing {driver1} vs {driver2}")

    winners = functions.get_race_winners(year)
    time.sleep(0.5)
    pole_winners = functions.get_pole_winners(year)
    time.sleep(0.5)

    driver1_wins = functions.count_wins(driver1, winners)
    driver2_wins = functions.count_wins(driver2, winners)

    driver1_poles = functions.count_wins(driver1, pole_winners)
    driver2_poles = functions.count_wins(driver2, pole_winners)

    # print(f'{driver1} had {driver1_wins} wins in season {year}.\n While {driver2} had {driver2_wins} wins.\n\n')
    # print(f'{driver1} had {driver1_poles} pole positions in season {year}.\n While {driver2} had {driver2_poles} pole positions.')

    st.write(f'{driver1} wins: {driver1_wins}.\n{driver2} wins: {driver2_wins}.\n\n')
    st.write(f'{driver1} pole positions: {driver1_poles}.\n{driver2} pole positions: {driver2_poles}.')

else:
    st.write('Please select all values.')
