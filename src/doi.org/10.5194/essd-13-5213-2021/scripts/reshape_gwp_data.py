import pandas as pd

print( "Reshaping GWP data..." )

df = pd.read_csv( "essd_ghg_data_gwp100.csv" )

print( "Initial read:" )
print( df )

# Drop GHG total column as pivot table will calculate this, and we do not want it in the rehsaped datat
df_adjusted = df.drop( columns=["GHG"] )
print( "Adjusted:" )
print( df_adjusted )

# Select only records which are not for 2020, as gases other than CO2 do not have 2020 data
df_filtered = df_adjusted[ df_adjusted.year < 2020 ]
print( "Filtered:" )
print( df_filtered )

# Reshape the data to be more compatible with PivotTable.js
df_reshaped = df_filtered.melt( id_vars=["ISO","country","region_ar6_6","region_ar6_10","region_ar6_22","region_ar6_dev","year","sector_title","subsector_title"], var_name="gas", value_name="emissions_tCO2eq" )

print( "Melted data table:" )
print( df_reshaped )

# Output CSV of reshaped dataframe

df_reshaped.to_csv( "out-ghg-data-gwp100-reshaped.csv", index=False )

