import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def print_regression_formula(data):
    # Influencing factors
    X = data[['DayType', 'Holiday', 'LongWeekend', 'Marriages', 'temp', 'feelslike', 'humidity', 'precip', 'precipprob', 'preciptype', 'cloudcover']]
    
    # Add constant term
    X = sm.add_constant(X)
    
    # Define dependent variable
    y = data['SalesQuantity']
    
    # Fit regression model
    model = sm.OLS(y, X).fit()

    # Predict
    ypred = model.predict(X)
    
    # Compute accuracy metrics
    r2 = r2_score(y, ypred)
    mse = mean_squared_error(y, ypred)
    mae = mean_absolute_error(y, ypred)
    
    # Print accuracy metrics
    print("R-squared:", r2)
    print("Mean Squared Error:", mse)
    print("Mean Absolute Error:", mae)

# Read data
data = pd.read_excel("data.xlsx", sheet_name='Sheet1')

# Convert columns to string
columns_to_convert = ['SalesOfficeID','MaterialCode']
for column in columns_to_convert:
    data[column] = data[column].astype(str)

# Filter data
material_code = '10102'
sales_office_id = '1942'
filtered_data = data[(data['MaterialCode'] == material_code) & (data['SalesOfficeID'] == sales_office_id)]

print_regression_formula(filtered_data)
