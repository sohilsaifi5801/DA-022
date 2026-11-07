from project_utils import load_tables


def analyse_road_monthly_area(tables):

    road = tables["road"]
    annual = tables["annual"]
    monthly = tables["monthly"]
    rural_urban = tables["rural_urban"]

    # 1. Road category analysis for 2023

    road_2023 = road.loc[
        road["year"] == 2023
    ].sort_values("accidents", ascending=False)

    print("ROAD CATEGORY ANALYSIS - 2023")

    print(
        road_2023[
            ["road_category", "accidents",
             "persons_killed", "persons_injured"]
        ].to_string(index=False)
    )

    # 2. Annual accident trends

    print("\nANNUAL ACCIDENT TRENDS")

    print(
        annual[
            ["year", "total_accidents", "persons_killed"]
        ].to_string(index=False)
    )

    # 3. Monthly accident analysis

    print("\nMONTHLY ACCIDENT ANALYSIS - 2023")

    print(
        monthly[
            ["month", "accidents", "persons_killed"]
        ].to_string(index=False)
    )

    highest_month = monthly.loc[
        monthly["accidents"].idxmax()
    ]

    lowest_month = monthly.loc[
        monthly["accidents"].idxmin()
    ]

    print(
        "\nMonth with highest accidents:",
        highest_month["month"]
    )

    print(
        "Month with lowest accidents:",
        lowest_month["month"]
    )

    # 4. Rural and urban comparison

    area_2023 = rural_urban.loc[
        rural_urban["year"] == 2023
    ]

    print("\nRURAL AND URBAN COMPARISON - 2023")

    print(
        area_2023[
            ["area", "accidents",
             "persons_killed", "persons_injured"]
        ].to_string(index=False)
    )

    return road_2023, highest_month, lowest_month, area_2023


if __name__ == "__main__":

    tables = load_tables()

    analyse_road_monthly_area(tables)
