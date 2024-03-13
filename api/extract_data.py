import pandas as pd
from datetime import datetime

def extract_data(date):
    df = pd.read_excel('2024-weather.xlsx')
    df.rename(columns={'datetime': 'Date'}, inplace=True)

    condition = df['Date'] == date

    desired_row = df[condition]

    desired_row_dict = desired_row.iloc[0].to_dict()
    if desired_row_dict['preciptype'] == 'rain':
        desired_row_dict['preciptype'] = 1
    else:
        desired_row_dict['preciptype'] = 0

    df = pd.read_excel('ts-holidays-2024.xlsx', sheet_name='holidays')
    if pd.to_datetime(date) in df['Date'].values:
        desired_row_dict['Holiday'] = 1
    else:
        desired_row_dict['Holiday'] = 0

    df = pd.read_excel('ts-holidays-2024.xlsx', sheet_name='long_weekends')
    if pd.to_datetime(date) in df['Date'].values:
        desired_row_dict['LongWeekend'] = 1
    else:
        desired_row_dict['LongWeekend'] = 0

    df = pd.read_excel('ts-holidays-2024.xlsx', sheet_name='wedding_dates')
    if pd.to_datetime(date) in df['Date'].values:
        desired_row_dict['Marriages'] = 1
    else:
        desired_row_dict['Marriages'] = 0

    date_object = datetime.strptime(date, '%Y-%m-%d')
    day_of_week = date_object.weekday()
    if day_of_week >= 5:
        desired_row_dict['DayType'] = 1
    else:
        desired_row_dict['DayType'] = 0
    
    return(desired_row_dict)