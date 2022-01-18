import pandas as pd

print( "Converting .xlsx to .csv ..." )

df = pd.read_excel( "essd_ghg_data_gwp100.xlsx", sheet_name="data" )

print( "Read xlsx into DataFrame:" )
print( df )

print( "Writing .csv ..." )
df.to_csv( "essd_ghg_data_gwp100.csv", index=False )

print( "... done." )

