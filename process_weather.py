import pandas as pd

excel_file_1 = 'weather.xlsx'
tidy_excel_file_1 = 'tidy_weather.xlsx'

df = pd.read_excel(excel_file_1, sheet_name=0, index_col=None)

print(df)

tidy_df = df.melt(id_vars=['location','Temperature'], var_name='Date', value_name='Value')
formatted_date = tidy_df['Date'].dt.strftime('%m-%Y')
tidy_df['Date'] = formatted_date
print(tidy_df)



# print(transposed_df)




