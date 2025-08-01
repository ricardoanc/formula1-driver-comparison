import fastf1 as ff1
import pandas as pd
from fastf1.ergast import Ergast

ff1.Cache.enable_cache('./cache')

ergast = Ergast()

# Returns a list of drivers on a given season
def get_drivers(year):
    season_drivers = ergast.get_driver_info(season=year)['driverCode'].drop_duplicates()
    return season_drivers


# Returns a list of the winner of each race given the season
def get_race_winners(year):
    schedule = ergast.get_race_schedule(season=year)
    
    df = pd.DataFrame(columns=['Circuit', 'Winner'])

    for i, round_number in enumerate(schedule['round'], start=1):
        winner_code = ergast.get_driver_info(season=year, round=round_number, results_position=1)['driverCode'].iloc[0]
        circuit = schedule[schedule['round'] == round_number]['circuitId'].iloc[0]

        df = pd.concat([df, pd.DataFrame([{'Circuit': circuit, 'Winner': winner_code}])], ignore_index=True)
    return df


# Returns a list of the winner of each pole position given the season
def get_pole_winners(year):
    schedule = ergast.get_race_schedule(season=year)
    
    df = pd.DataFrame(columns=['Circuit', 'Winner'])

    for i, round_number in enumerate(schedule['round'], start=1):
        pole_winner = ergast.get_driver_info(season=year, round=round_number, grid_position=1)['driverCode'].iloc[0]
        circuit = schedule[schedule['round'] == round_number]['circuitId'].iloc[0]

        df = pd.concat([df, pd.DataFrame([{'Circuit': circuit, 'Winner': pole_winner}])], ignore_index=True)
    return df


# Returns total count of wins per racer
def count_wins(racer, winners):
    total_wins = (winners['Winner'] == racer).sum()
    return total_wins

