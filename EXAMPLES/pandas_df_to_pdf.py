import pandas as pd
import pdfkit  # needed for conversion to PDF

# data from
# http://www.rita.dot.gov/bts/sites/rita.dot.gov.bts/files/publications/
# national_transportation_statistics/html/table_01_44.html

airports_df = pd.read_csv(  # create dataframe from CSV file
    '../DATA/airport_boardings.csv',
    thousands=',',
    index_col=1
)

print("ENTIRE DATAFRAME")

print(airports_df.head(), "\n")

print("SELECTED COLUMNS WITH FILTERED ROWS")

columns_wanted = ['2001 Total', 'Airport']  # only want these columns
sort_col = '2001 Total'  # column to sort on
min_val = 20000000 # only want rows where '2001 Total' is > min_val
selector = airports_df['2001 Total'] > min_val  # Boolean selector for desired rows

print("COLUMN TOTALS")
selected_rows = airports_df[selector][columns_wanted]  # save selected rows to new dataframe

html = selected_rows.to_html('selected_rows.html')  # export dataframe as HTML

pdfkit.from_file('selected_rows.html', 'selected_rows.pdf') # convert HTML to PDF with pdfkit
