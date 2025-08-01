from fastf1.ergast import Ergast
import pandas as pd
import time

ergast = Ergast()

def get_drivers(year):
    season_drivers = ergast.get_driver_info(season=year)['driverId'].drop_duplicates()
    return season_drivers

def jic_full_drivers_list():
    drivers_list = []

    for year in range(1950,2025):
        season_drivers = get_drivers(year)
        time.sleep(0.5)
        for driver in season_drivers:
            drivers_list.append({'Driver Name': driver, 'Season': year})

    all_time_drivers = pd.DataFrame(drivers_list)

    all_time_drivers.to_csv('./drivers_list.csv', index=False, encoding='utf-8')
    
    return