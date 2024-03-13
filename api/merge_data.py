import pandas as pd

# Step 1: Read all Excel files into pandas dataframes
sales_d1 = pd.read_excel("2021.xlsx", sheet_name=None)
sales_d2 = pd.read_excel("2022.xlsx", sheet_name=None)
sales_d3 = pd.read_excel("2023.xlsx", sheet_name=None)

sales_combined = pd.concat([sales_d1["first_half"], sales_d1["second_half"], 
                            sales_d2["first_half"], sales_d2["second_half"],
                            sales_d3["first_half"], sales_d3["second_half"]], ignore_index=True)

# Step 3: Sum up SalesQuantity for each Date and MaterialCode combination
sales_grouped_by_office = sales_combined.groupby(["BillingDate", "SalesOfficeID", "MaterialCode"]).agg({"SalesQuantity": "sum"}).reset_index()
sales_grouped_by_office.rename(columns={'BillingDate': 'Date'}, inplace=True)

dailydata = pd.read_excel('dailydata.xlsx')
dailydata['DayType'] = dailydata['DayType'].map({'Weekend': 1, 'Weekday': 0})
columns_to_convert = ['Holiday', 'LongWeekend', 'Marriages', 'preciptype']
dailydata[columns_to_convert] = dailydata[columns_to_convert].applymap(lambda x: 1 if pd.notna(x) and x != '' else 0)

sales_grouped_by_office['Date'] = pd.to_datetime(sales_grouped_by_office['Date'])
dailydata['Date'] = pd.to_datetime(dailydata['Date'])
merged_data = pd.merge(sales_grouped_by_office, dailydata, on='Date')

merged_data.to_excel("data.xlsx", index=False)

print("Done")