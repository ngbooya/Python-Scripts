import pandas as pd 

excel_file_1 = 'treatments.xlsx'
tidy_excel_file_1 = 'tidy_treatments.xlsx'

df = pd.read_excel(excel_file_1, sheet_name=0, index_col=None)

# Columns to rows
tidy_df = df.melt(id_vars=['NAME'], value_vars=['TREATMENT A', 'TREATMENT B'], var_name='TREATMENT', value_name='RESULT')
print(tidy_df)

#Take out 'TREATMENT' in treatment type
temp_df = tidy_df['TREATMENT'].str.split(" ", n=1, expand=True)
tidy_df['TREATMENT TYPE'] = temp_df[1]

# Drop old treament columns
tidy_df.drop(columns=['TREATMENT'], inplace=True)

# Shift columns to desired order
cols_shift = ['NAME','TREATMENT TYPE', 'RESULT'] 

# Print final df waiting to write
print(tidy_df[cols_shift])

writer = pd.ExcelWriter(tidy_excel_file_1)

try:
    tidy_df.to_excel(writer)
    writer.save()
    print("Dataframe is written successfully to new excel file ", tidy_excel_file_1)
except:
    print("There was a problem writing to new excel ", tidy_excel_file_1)





