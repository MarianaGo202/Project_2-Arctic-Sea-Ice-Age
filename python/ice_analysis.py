import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Paths 
NC_PATH = "data/processed/arctic_sea_ice_may_2026.nc"
PLOT_PATH = "visualisations/daily_mean_ice_age.png"
SQL_CSV_PATH = "data/processed/arctic_sea_ice_sql.csv"
POWERBI_CSV_PATH = "data/processed/powerbi_arctic_sea_ice.csv"

# Variables
CONCENTRATION_VARIABLES = [
    "conc_1yi",
    "conc_2yi",
    "conc_3yi",
    "conc_4yi",
    "conc_5yi",
    "conc_6yi",
]

def inspect_dataset(dados: xr.Dataset) -> None:
    print("Dataset:")
    print(dados)

    print("\nData variables:")
    print(list(dados.data_vars))

    print("\nCoordinates:")
    print(list(dados.coords))

    print("\nDimensions:")
    print(dados.dims)

    print("\nVariable attributes:")
    for variable in dados.data_vars:
        print(f"\n--- {variable} ---")
        print(dados[variable].attrs)

    print("\nMissing values:")
    for variable in dados.data_vars:
        missing = dados[variable].isnull().sum().item()
        print(f"{variable}: {missing}")

def analyze_sea_ice_age(dados: xr.Dataset) -> pd.DataFrame:
    siage = dados["siage"]

    print("\nSea ice age statistics:")
    print("Minimum:", siage.min().item())
    print("Maximum:", siage.max().item())
    print("Mean:", siage.mean().item())
    print("Median:", siage.median().item())

    daily_mean_age = siage.mean(dim=["y", "x"])
    print("\nDaily mean sea ice age:")
    print(daily_mean_age)

    df_time = daily_mean_age.to_dataframe(name="mean_ice_age").reset_index()

    print("\nTime series DataFrame:")
    print(df_time.head())
    print("\nTime series statistics:")
    print(df_time["mean_ice_age"].describe())

    return df_time

def plot_daily_mean_age(df_time: pd.DataFrame) -> None:
    import os
    os.makedirs("visualisations", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df_time["time"], df_time["mean_ice_age"])
    plt.xlabel("Date")
    plt.ylabel("Mean Sea Ice Age")
    plt.title("Daily Mean Arctic Sea Ice Age - May 2026")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=300)
    plt.show()

def analyze_concentration_by_age(dados: xr.Dataset) -> pd.DataFrame:
    print("\nMean concentration:")
    for variable in CONCENTRATION_VARIABLES:
        mean_value = dados[variable].mean().item()
        print(f"{variable}: {mean_value}")

    daily_concentration = dados[CONCENTRATION_VARIABLES].mean(dim=["y", "x"])
    print("\nDaily concentration:")
    print(daily_concentration)

    df_concentration = daily_concentration.to_dataframe().reset_index()

    print("\nConcentration DataFrame:")
    print(df_concentration.head())

    return df_concentration

def export_data(df_concentration: pd.DataFrame) -> None:
    import os
    os.makedirs("data/processed", exist_ok=True)

    print("\nSQL DataFrame:")
    print(df_concentration.head())
    print("\nSQL DataFrame shape:")
    print(df_concentration.shape)

    df_concentration.to_csv(SQL_CSV_PATH, index=False)
    print("\nCSV exported successfully!")
    print(f"File: {SQL_CSV_PATH}")

    df_concentration.to_csv(POWERBI_CSV_PATH, index=False)
    print("\nPower BI CSV exported successfully!")
    print(f"File: {POWERBI_CSV_PATH}")
    print("Power BI dataset shape:", df_concentration.shape)

def main():
    dados = xr.open_dataset(NC_PATH)

    inspect_dataset(dados)
    df_time = analyze_sea_ice_age(dados)
    plot_daily_mean_age(df_time)
    df_concentration = analyze_concentration_by_age(dados)
    export_data(df_concentration)

    dados.close()

if __name__ == "__main__":
    main()
