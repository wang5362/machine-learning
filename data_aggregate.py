import pandas as pd
from convert import convert
import glob
from schema import lease_name, loan_name

# Read the date_match file, which contains the dates for each EDGAR file
# date_match = pd.read_csv ("date_match.csv", index_col=1)
# date_match = date_match.loc[:, ~date_match.columns.str.contains ('^Unnamed')]

# Find all the valid date_match file names in the folder
file_in_folder = glob.glob ('**.csv')
# csv_in_list = date_match['File Name']
# valid_names = tuple (set (csv_in_folder) & set (csv_in_list))
# missing_names = tuple (set (csv_in_folder) - set (csv_in_list))

variables = loan_name # all the possible name for autolease contract

dfs = tuple(map(pd.read_csv, file_in_folder))
dfs = tuple(convert(df, variables) for df in dfs)
# for name in valid_names:
#     df = pd.read_csv (name, skiprows=1, header=None)
#     df = convert(df, variables)
#     dfs+=(df,)

database = pd.concat(dfs)

database.to_csv('database.csv')
