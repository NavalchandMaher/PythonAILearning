
#Reading files using pandas

#CSV file
import pandas as pd
df = pd.read_csv('data.csv')

#Excel file
df = pd.read_excel('data.xlsx')

#JSON file
df = pd.read_json('data.json')

#HTML file
df = pd.read_html('data.html')

#Save to CSV
df.to_csv('data.csv', index=False)

#Save to Excel
df.to_excel('data.xlsx', index=False)

#Save to JSON
df.to_json('data.json', orient='records')

#Save to HTML
df.to_html('data.html', index=False)

#SQL database
import sqlite3
conn = sqlite3.connect('data.db')

#SQL query
df = pd.read_sql_query('SELECT * FROM table_name', conn)

#Parquet file
df = pd.read_parquet('data.parquet')

#HDF5 file
df = pd.read_hdf('data.h5', 'table_name')

#Feather file
df = pd.read_feather('data.feather')

#Stata file
df = pd.read_stata('data.dta')

#SAS file
df = pd.read_sas('data.sas7bdat')

#SPSS file
df = pd.read_spss('data.sav')

#Pickle file
df = pd.read_pickle('data.pkl')
