# Import libraries
import sqlite3
import pandas as pd


# ============================================================
# 1. LOAD THE PROCESSED CSV FILE
# ============================================================

# Load the CSV file generated during the Python analysis
arquivo_csv = "dados_processados/dados_gelo_artico_sql.csv"

df = pd.read_csv(arquivo_csv)


# Display the first rows
print("CSV data:")

print(df.head())


# ============================================================
# 2. CONNECT TO THE SQLITE DATABASE
# ============================================================

# Create or connect to the SQLite database
connection = sqlite3.connect(
    "gelo_artico.db"
)


# ============================================================
# 3. CREATE THE DATABASE TABLE
# ============================================================

# Save the DataFrame as a SQL table
df.to_sql(
    "ice_concentration",
    connection,
    if_exists="replace",
    index=False
)


# ============================================================
# 4. CHECK THE DATABASE TABLE
# ============================================================

# Read the table back from SQLite
table = pd.read_sql_query(
    "SELECT * FROM ice_concentration LIMIT 5",
    connection
)


# Display the first records
print("\nDatabase table:")

print(table)


# ============================================================
# 5. CLOSE THE DATABASE CONNECTION


# Close the database connection
connection.close()


# Confirm successful database creation
print("\nDatabase created successfully!")

print("File: gelo_artico.db")