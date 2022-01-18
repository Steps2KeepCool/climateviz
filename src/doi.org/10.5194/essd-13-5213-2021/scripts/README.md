# Scripts used to process data from paper https://doi.org/10.5194/essd-13-5213-2021

These scripts were used as follows:  
  - Download data file essd_ghg_data_gwp100.xlsx from https://doi.org/10.5281/zenodo.5566761
  - Convert .xlsx to a .csv by running:  
    python convert_xlsx_to_csv.py
  - Reshape data columns slightly to make compatible with PivotTable.js:  
    python reshape_gwp_data.py
