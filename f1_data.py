#<editor-fold desc="Imports">
import fastf1 as ff1
import pandas as pd


#</editor-fold>

#<editor-fold desc="Set Ups">
ff1.Cache.enable_cache('Cache/')
pd.options.mode.chained_assignment = None



def getLapTimes(year, race, session):
    race = ff1.get_session(year, race, session)
    
    laps = race.load_laps(with_telemetry=True)

    colums = ["Stint","LapStartTime","LapStartDate","SpeedI1","SpeedI2","SpeedFL","SpeedST","IsPersonalBest","FreshTyre"]

    laps.drop(colums,inplace=True,axis=1)

    print(laps)
    return laps

