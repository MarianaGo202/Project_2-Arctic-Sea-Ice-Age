# Import libraries
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Load the processed Arctic sea ice dataset
arquivo = "dados_processados/gelo_artico_maio_2026.nc"

dados = xr.open_dataset(arquivo)

# Inspect the dataset structure
print("Dataset:")
print(dados)

# List the available data variables
print("\nData variables:")
print(list(dados.data_vars))

# List the available coordinates
print("\nCoordinates:")
print(list(dados.coords))

# Display the dataset dimensions
print("\nDimensions:")
print(dados.dims)

# Display the attributes of each variable
print("\nVariable attributes:")

for variable in dados.data_vars:

    print(f"\n--- {variable} ---")

    print(dados[variable].attrs)

# Check the number of missing values in each variable
print("\nMissing values:")

for variable in dados.data_vars:

    missing = dados[variable].isnull().sum().item()

    print(f"{variable}: {missing}")

# Select the sea ice age variable
siage = dados["siage"]

# Calculate basic statistics for sea ice age
print("\nSea ice age statistics:")

# Calculate the minimum sea ice age
print("Minimum:")
print(siage.min().item())

# Calculate the maximum sea ice age
print("Maximum:")
print(siage.max().item())

# Calculate the mean sea ice age
print("Mean:")
print(siage.mean().item())

# Calculate the median sea ice age
print("Median:")
print(siage.median().item())

# Calculate the spatial mean for each time step
daily_mean_age = dados["siage"].mean(
    dim=["y", "x"]
)

# Display the daily mean values
print("\nDaily mean sea ice age:")
print(daily_mean_age)

# Convert the time series to a Pandas DataFrame
df_time = daily_mean_age.to_dataframe(
    name="mean_ice_age"
).reset_index()

# Inspect the resulting DataFrame
print("\nTime series DataFrame:")
print(df_time.head())

# Display descriptive statistics for the time series
print("\nTime series statistics:")

print(
    df_time["mean_ice_age"].describe()
)

# Create the daily mean sea ice age plot
plt.figure(figsize=(10, 6))

# Plot the daily mean sea ice age
plt.plot(
    df_time["time"],
    df_time["mean_ice_age"]
)

# Add labels and title
plt.xlabel("Date")

plt.ylabel("Mean Sea Ice Age")

plt.title(
    "Daily Mean Arctic Sea Ice Age - May 2026"
)

# Format the x-axis labels
plt.xticks(rotation=45)

# Add a grid to the plot
plt.grid(True)

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig(
    "daily_mean_ice_age.png",
    dpi=300
)

# Display the figure
plt.show()

# Define the sea ice concentration variables by age category
concentration_variables = [
    "conc_1yi",
    "conc_2yi",
    "conc_3yi",
    "conc_4yi",
    "conc_5yi",
    "conc_6yi"
]

# Calculate the mean concentration for each category
print("\nMean concentration:")

for variable in concentration_variables:

    mean_value = dados[variable].mean().item()

    print(
        f"{variable}: {mean_value}"
    )

# Calculate the spatial mean concentration for each time step
daily_concentration = dados[
    concentration_variables
].mean(
    dim=["y", "x"]
)

# Display the daily concentration values
print("\nDaily concentration:")

print(daily_concentration)

# Convert the concentration data to a Pandas DataFrame
df_concentration = (
    daily_concentration
    .to_dataframe()
    .reset_index()
)

# Inspect the concentration DataFrame
print("\nConcentration DataFrame:")

print(df_concentration.head())

# Create a copy for the SQL stage
sql_df = df_concentration.copy()

# Inspect the DataFrame before exporting
print("\nSQL DataFrame:")

print(sql_df.head())

# Check the DataFrame dimensions
print("\nSQL DataFrame shape:")

print(sql_df.shape)

# Export the processed data as a CSV file for SQL
sql_df.to_csv(
    "dados_processados/dados_gelo_artico_sql.csv",
    index=False
)

# Confirm that the CSV was exported successfully
print("\nCSV exported successfully!")

print(
    "File: dados_processados/dados_gelo_artico_sql.csv"
)

# Create a copy of the processed concentration data for Power BI
powerbi_df = df_concentration.copy()

# Export the data for Power BI
powerbi_df.to_csv(
    "powerbi_gelo_artico.csv",
    index=False
)

# Confirm that the Power BI file was exported successfully
print("\nPower BI CSV exported successfully!")

# Display the Power BI dataset shape
print("\nPower BI dataset shape:")

print(
    powerbi_df.shape
)