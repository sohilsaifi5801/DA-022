
from project_utils import load_tables, make_folders

from data_loader import inspect_tables

from data_checks import (
    check_data,
    save_quality_reports
)

from time_severity_weather import (
    analyse_time_severity_weather
)

from road_monthly_area import (
    analyse_road_monthly_area
)

from charts_aryan import make_aryan_charts

from charts_friend import make_friend_charts


def main():

    print("=" * 55)
    print("ROAD ACCIDENT PATTERN ANALYSIS - INDIA")
    print("=" * 55)

    # Step 1: Create project folders

    make_folders()

    # Step 2: Load all datasets

    tables = load_tables()

    # Step 3: Inspect datasets

    print("\n1. DATA LOADING AND INSPECTION")

    inspect_tables(tables)

    # Step 4: Check data quality

    print("\n2. DATA QUALITY CHECKS")

    quality, reconciliation = check_data(tables)

    print(quality.to_string(index=False))
    print(reconciliation.to_string(index=False))

    save_quality_reports(quality, reconciliation)

    if not reconciliation["passed"].all():

        raise ValueError(
            "Some data checks failed. "
            "Please review the source tables."
        )

    print("All reconciliation checks passed.")

    # Step 5: Time, severity and weather analysis

    print("\n3. TIME, SEVERITY AND WEATHER ANALYSIS")

    analyse_time_severity_weather(tables)

    # Step 6: Road, monthly and area analysis

    print("\n4. ROAD, MONTHLY AND AREA ANALYSIS")

    analyse_road_monthly_area(tables)

    # Step 7: Create charts

    print("\n5. CREATING VISUALIZATIONS")

    make_aryan_charts(tables)

    make_friend_charts(tables)

    print("\n" + "=" * 55)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("Check the reports and visualizations folders.")
    print("=" * 55)


if __name__ == "__main__":

    main()
