import sqlite3
import pandas as pd

# Connect to the SQLite database
path_to_sqlite_db = "S30 ETL Assignment.db"
conn = sqlite3.connect(path_to_sqlite_db)

# Load the data into pandas DataFrames
customers = pd.read_sql_query("SELECT * FROM customers", conn)
sales = pd.read_sql_query("SELECT * FROM sales", conn)
orders = pd.read_sql_query("SELECT * FROM orders", conn)
items = pd.read_sql_query("SELECT * FROM items", conn)

# Close the connection
conn.close()

# Merge the DataFrames
merged_df = customers.merge(sales, on='customer_id') \
                     .merge(orders, on='sales_id') \
                     .merge(items, on='item_id')

# Filter the data based on the age condition
filtered_df = merged_df[(merged_df['age'] >= 18) & (merged_df['age'] <= 35)]

# Group by the necessary columns and aggregate the data
grouped_df = filtered_df.groupby(['customer_id', 'age', 'item_name'], as_index=False) \
                        .agg(quantity=('quantity', lambda x: x.fillna(0).sum().astype(int)))

# Filter the groups based on the HAVING condition
result_df = grouped_df[grouped_df['quantity'] > 0]

# Sort the results
result_df = result_df.sort_values(by=['customer_id', 'age', 'item_name'])

# Renaming columns based on the mapping
column_mapping = {
    "customer_id": "customer",
    "item_name": "item",
}
result_df = result_df.rename(columns=column_mapping)

# Save the result to a CSV file with ";" as the delimiter
output_path = "report.csv"
result_df.to_csv(output_path, sep=';', index=False)
