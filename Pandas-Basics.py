import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Initialize name of target excel file
excel_file_1 = 'movies.xlsx'
# movies = pd.read_excel(excel_file_1)
# print(movies.head())

#Print sheet 1
# movies_sheet1 = pd.read_excel(excel_file_1, sheet_name=0, index_col=0)
# print(movies_sheet1.head())

#Print sheet 2
# movies_sheet2 = pd.read_excel(excel_file_1, sheet_name=1, index_col=0)
# print(movies_sheet2.head())

#Print sheet 3
# movies_sheet3 = pd.read_excel(excel_file_1, sheet_name=2, index_col=0)
# print(movies_sheet3.head())

#Combine all 3 sheets into one dataframe
# movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
# print("Dimensions of combined dataframe is : " + str(movies.shape))

#Read in all sheets from a single excel file
combined_sheets_excel_file_1 = pd.ExcelFile(excel_file_1)
movies_sheet_all = []
for sheet in combined_sheets_excel_file_1.sheet_names:
    movies_sheet_all.append(combined_sheets_excel_file_1.parse(sheet))
movies = pd.concat(movies_sheet_all)

movies_subset = movies[['Country', 'Language', 'Gross Earnings']]
print(movies_subset.head())






