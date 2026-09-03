import sqlite3
from pathlib import Path

import pandas as pd

CSV_PATH = Path("data/processed/dados_gelo_artico_sql.csv")
DB_PATH = Path("gelo_artico.db")
TABLE_NAME = "ice_concentration"


def load_csv(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} rows from {csv_path}")
    print(df.head())
    return df


def save_to_sqlite(df: pd.DataFrame, db_path: Path, table_name: str) -> None:
    with sqlite3.connect(db_path) as connection:
        df.to_sql(table_name, connection, if_exists="replace", index=False)

        # Read a few rows back as a sanity check that the write worked
        preview = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", connection)
        print(f"\nPreview of '{table_name}' in {db_path}:")
        print(preview)


def main():
    df = load_csv(CSV_PATH)
    save_to_sqlite(df, DB_PATH, TABLE_NAME)
    print(f"\nDatabase created successfully: {DB_PATH}")


if __name__ == "__main__":
    main()
