import pandas as pd
from project_utils import load_tables, REPORT_DIR, make_folders


def check_data(tables):

    quality_rows = []

    for name, table in tables.items():

        quality_rows.append({
            "table": name,
            "rows": len(table),
            "columns": len(table.columns),
            "missing_cells": int(table.isna().sum().sum()),
            "duplicate_rows": int(table.duplicated().sum())
        })

    quality = pd.DataFrame(quality_rows)

    annual = tables["annual"]
    severity = tables["severity"]
    road = tables["road"]
    weather = tables["weather"]
    time = tables["time"]
    monthly = tables["monthly"]
    rural_urban = tables["rural_urban"]

    checks = []

    def add_check(name, observed, expected):

        checks.append({
            "check": name,
            "observed": int(observed),
            "expected": int(expected),
            "passed": int(observed) == int(expected)
        })

    # Check time interval totals

    for year in [2019, 2020, 2021, 2022, 2023]:

        expected = annual.loc[
            annual.year == year, "total_accidents"
        ].iloc[0]

        observed = time.loc[
            time.year == year, "accidents"
        ].sum()

        add_check(
            f"Time totals - {year}",
            observed,
            expected
        )

    # Check weather, road and severity totals

    for year in [2022, 2023]:

        expected = annual.loc[
            annual.year == year, "total_accidents"
        ].iloc[0]

        for name, table in [
            ("Weather", weather),
            ("Road", road),
            ("Severity", severity)
        ]:

            observed = table.loc[
                table.year == year, "accidents"
            ].sum()

            add_check(
                f"{name} totals - {year}",
                observed,
                expected
            )

    # Check monthly totals for 2023

    expected_accidents = annual.loc[
        annual.year == 2023, "total_accidents"
    ].iloc[0]

    observed_accidents = monthly["accidents"].sum()

    add_check(
        "Monthly accident totals - 2023",
        observed_accidents,
        expected_accidents
    )

    # Check monthly deaths for 2023

    expected_killed = annual.loc[
        annual.year == 2023, "persons_killed"
    ].iloc[0]

    observed_killed = monthly["persons_killed"].sum()

    add_check(
        "Monthly killed totals - 2023",
        observed_killed,
        expected_killed
    )

    # Check rural and urban totals

    for metric in [
        "accidents",
        "persons_killed",
        "persons_injured"
    ]:

        observed = rural_urban.loc[
            rural_urban.year == 2023, metric
        ].sum()

        expected = annual.loc[
            annual.year == 2023, metric
        ].iloc[0]

        add_check(
            f"Rural and urban {metric} - 2023",
            observed,
            expected
        )

    reconciliation = pd.DataFrame(checks)

    return quality, reconciliation


def save_quality_reports(quality, reconciliation):

    make_folders()

    quality.to_csv(
        REPORT_DIR / "data_quality_summary.csv",
        index=False
    )

    reconciliation.to_csv(
        REPORT_DIR / "reconciliation_checks.csv",
        index=False
    )

    print("Data quality reports saved successfully.")


if _name_ == "_main_":

    data = load_tables()

    quality, reconciliation = check_data(data)

    save_quality_reports(quality, reconciliation)

    print("\nDATA QUALITY SUMMARY")
    print(quality.to_string(index=False))

    print("\nRECONCILIATION CHECKS")
    print(reconciliation.to_string(index=False))

    passed = reconciliation["passed"].sum()

    total = len(reconciliation)

    print(f"\nPassed checks: {passed}/{total}")

    if reconciliation["passed"].all():

        print("All reconciliation checks passed.")

    else:

        print("Some checks need review.")
