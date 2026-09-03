import os

FOLDERS = [
    "data/raw",
    "data/processed",
    "database",
    "power bi",
    "python",
    "sql",
    "visualisations",
]

def create_folders(folders: list[str]) -> None:
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Ready: {folder}")

def main():
    create_folders(FOLDERS)
    print("\nProject folder structure created successfully!")

if __name__ == "__main__":
    main()
