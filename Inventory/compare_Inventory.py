import pandas as pd

try:
    sheet_1_df = pd.read_excel('Inventory.xlsx', sheet_name=0, index_col=None)
    # print(sheet_1_df)
except:
    print("Error reading in Sheet 1")

try:
    sheet_2_df = pd.read_excel('Inventory.xlsx', sheet_name=1, index_col=None)
    # print(sheet_2_df)
except:
    print("Error reading in Sheet 2")

SKU_df_1 = sheet_1_df[['SKU', 'Available']]
# Change column name
SKU_df_1.rename(columns={"Available":"Qty"}, inplace=True)

# SKU_df_1['File'] = "Latona Inventory"
# SKU_df_1 = SKU_df_1[['File','SKU','Qty']]
SKU_df_1 = SKU_df_1.pivot_table(index='SKU', aggfunc=sum)


print(SKU_df_1)

# SKU_df_2 = sheet_2_df[['SKU','Garment Q\'ty']]
# Change column name
# SKU_df_2.rename(columns={"Garment Q\'ty":"Qty"}, inplace=True)
# SKU_df_2['File'] = 'Madagascar Inventory'
# print(SKU_df_2)

# append_df = SKU_df_1.append(SKU_df_2)
# print(append_df)

SKU_df_1.to_excel('result.xlsx', index=False)