from fastf1.ergast import Ergast
import pandas as pd

ergast = Ergast()


from fastf1.ergast import Ergast

ergast = Ergast()


def get_race_winners(year):
    schedule = ergast.get_race_schedule(season=year)
    
    df = pd.DataFrame(columns=['Circuit', 'Winner'])

    for i, round_number in enumerate(schedule['round'], start=1):
        winner_code = ergast.get_driver_info(season=year, round=round_number, results_position=1)['driverCode'].iloc[0]
        circuit = schedule[schedule['round'] == round_number]['circuitId'].iloc[0]

        df = pd.concat([df, pd.DataFrame([{'Circuit': circuit, 'Winner': winner_code}])], ignore_index=True)
    
    return df

the_winners = get_race_winners(2022)

def count_wins(racer):
    total_wins = the_winners['Winner'].value_counts()[racer]
    return total_wins

print(f'Verstappen: {count_wins('VER')}')
print(f'Leclerc: {count_wins('LEC')}')
print(f'Checo: {count_wins('PER')}')
print(f'Sainz: {count_wins('SAI')}')
print(f'Russell: {count_wins('RUS')}')

