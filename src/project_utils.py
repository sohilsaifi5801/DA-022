from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_DIR / "data"

CHART_DIR = PROJECT_DIR / "visualizations"

REPORT_DIR = PROJECT_DIR / "reports"

DATA_FILES = {
    "annual": "national_trends_2019_2023.csv",
    "severity": "severity_2019_2023.csv",
    "road": "road_category_2022_2023.csv",
    "weather": "weather_2022_2023.csv",
    "time": "time_interval_2019_2023.csv",
    "monthly": "monthly_2023.csv",
    "rural_urban": "rural_urban_2019_2023.csv"
}


def make_folders():

    CHART_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def load_tables():

    tables = {}

    for name, filename in DATA_FILES.items():

        path = DATA_DIR / filename

        if not path.exists():

            raise FileNotFoundError(
                f"Missing data file: {path}"
            )

        tables[name] = pd.read_csv(path)

    return tables
