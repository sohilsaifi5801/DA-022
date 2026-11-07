import pandas as pd
from project_utils import load_tables


def analyse_time_severity_weather(tables):
    """Analyse time, severity and weather patterns for 2023."""

    annual = tables["annual"]
    time = tables["time"]
    severity = tables["severity"]
    weather = tables["weather"]

    row_2023 = annual.loc[annual.year == 2023].iloc[0]

    time_2023 = time.loc[
        time.year == 2023
    ].sort_values("accidents", ascending=False)

    severity_2023 = severity.loc[
        severity.year == 2023
    ].sort_values("accidents", ascending=False)

    weather_2023 = weather.loc[
        weather.year == 2023
    ].sort_values("accidents", ascending=False)

    print("INDIA ROAD ACCIDENT SUMMARY - 2023")

    print(f"Total accidents: {row_2023.total_accidents:,.0f}")
    print(f"Fatal accidents: {row_2023.fatal_accidents:,.0f}")
    print(f"Persons killed: {row_2023.persons_killed:,.0f}")
    print(f"Persons injured: {row_2023.persons_injured:,.0f}")

    print("\nTIME INTERVAL ANALYSIS")

    print(
        time_2023[
            ["time_interval", "accidents", "share_pct"]
        ].to_string(index=False)
    )

    print("\nSEVERITY ANALYSIS")

    print(
        severity_2023[
            ["severity_category", "accidents", "share_pct"]
        ].to_string(index=False)
    )

    print("\nWEATHER ANALYSIS")

    print(
        weather_2023[
            ["weather_condition", "accidents", "accident_share_pct"]
        ].to_string(index=False)
    )

    return time_2023, severity_2023, weather_2023


if _name_ == "_main_":

    tables = load_tables()

    analyse_time_severity_weather(tables)
