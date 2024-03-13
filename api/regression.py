import pandas as pd
from extract_data import extract_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import json


def apply_regression(from_date, to_date, material_code, sales_office_id):
    data = pd.read_excel("data.xlsx", sheet_name='Sheet1')


    columns_to_convert = ['SalesOfficeID', 'MaterialCode']
    for column in columns_to_convert:
        data[column] = data[column].astype(str)


    filtered_data = data[(data['MaterialCode'] == material_code) & (data['SalesOfficeID'] == sales_office_id)]
    try:
        x = filtered_data[['DayType', 'Holiday', 'LongWeekend', 'Marriages', 'temp', 'feelslike', 'humidity', 'precip', 'precipprob', 'preciptype', 'cloudcover']]
        y = filtered_data['SalesQuantity']


        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


        # Random Forest Regression
        rf_regressor = RandomForestRegressor(n_estimators=100, random_state=0)  # You can adjust n_estimators as needed
        rf_regressor.fit(x_train, y_train)


        # Predict future sales quantities
        future_sales = []
        # i=0
        for date in pd.date_range(from_date, to_date):
            future_data = extract_data(date.strftime('%Y-%m-%d'))
            future_df = pd.DataFrame([future_data])
            future_x = future_df[['DayType', 'Holiday', 'LongWeekend', 'Marriages', 'temp', 'feelslike', 'humidity', 'precip', 'precipprob', 'preciptype', 'cloudcover']]
            # future_sales[date.strftime('%Y-%m-%d')] = rf_regressor.predict(future_x)[0]
            future_sales.append({'date':date.strftime('%Y-%m-%d'), 'sales_quantity': (str(rf_regressor.predict(future_x)[0])+' KG')})
            # future_sales[i]['date'] = date.strftime('%Y-%m-%d')
            # future_sales[i]['sales_quantity'] = rf_regressor.predict(future_x)[0]
            # i+=1


        # Convert future sales to JSON format
        future_sales_json = json.dumps(future_sales, indent=4)
        return (future_sales_json)
       
    except Exception as e:
        print(f"Some Error Occurred: {e}")