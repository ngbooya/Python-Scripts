import pandas as pd 

excel_file_1 = 'initial-june.xlsx'
excel_file_2 = 'fixed-june.xlsx'

df_1 = pd.read_excel(excel_file_1, sheet_name=0, index_col=None)
df_2 = pd.read_excel(excel_file_2, sheet_name=0, index_col=None)

# print(df_1.columns)
df_1_data = df_1[['GscSku','PoNbr','Qty_Size_Order']]
df_2_data = df_2[['GscSku','PoNbr','Qty_Size_Order']]


# Combine the two dataframes based on keys SKU and PO number
result_df = pd.merge(df_1_data, df_2_data, on=['GscSku','PoNbr'])
print(result_df)

# Display rows with difference quantities
diff_df = result_df.loc[result_df['Qty_Size_Order_x'] != result_df['Qty_Size_Order_y']]
print(diff_df)

diff_df.to_excel('result.xlsx', index=False)

# diff_df.to_excel('result.xlsx', index=False)






