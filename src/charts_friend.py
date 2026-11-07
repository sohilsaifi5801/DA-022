import matplotlib.pyplot as plt
import seaborn as sns

from project_utils import load_tables, CHART_DIR, make_folders


def make_friend_charts(tables):
    """Create four charts for road, annual, monthly and area data."""

    make_folders()
    sns.set_theme(style="whitegrid")

    road = tables["road"]
    annual = tables["annual"]
    monthly = tables["monthly"]
    rural_urban = tables["rural_urban"]

    # Chart 4: Road category comparison

    road_data = road.loc[road.year == 2023].copy()

    road_long = road_data.melt(
        id_vars="road_category",
        value_vars=[
            "accidents",
            "persons_killed",
            "persons_injured"
        ],
        var_name="measure",
        value_name="count"
    )

    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=road_long,
        x="road_category",
        y="count",
        hue="measure"
    )

    ax.set_title(
        "Road Accidents by Road Category - 2023"
    )
    ax.set_xlabel("Road Category")
    ax.set_ylabel("Number of Cases")

    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "04_road_category_2023.png",
        dpi=180,
        bbox_inches="tight"
    )
    plt.close()

    # Chart 5: Annual accident trends

    annual_long = annual.melt(
        id_vars="year",
        value_vars=[
            "total_accidents",
            "persons_killed"
        ],
        var_name="measure",
        value_name="count"
    )

    plt.figure(figsize=(9, 5.5))

    ax = sns.lineplot(
        data=annual_long,
        x="year",
        y="count",
        hue="measure",
        marker="o"
    )

    ax.set_title(
        "Road Accident Trends - 2019 to 2023"
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cases")
    ax.set_xticks(annual.year)

    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "05_annual_trends_2019_2023.png",
        dpi=180,
        bbox_inches="tight"
    )
    plt.close()

    # Chart 6: Monthly accident trends

    monthly_long = monthly.melt(
        id_vars="month",
        value_vars=[
            "accidents",
            "persons_killed"
        ],
        var_name="measure",
        value_name="count"
    )

    plt.figure(figsize=(11, 5.5))

    ax = sns.lineplot(
        data=monthly_long,
        x="month",
        y="count",
        hue="measure",
        marker="o"
    )

    ax.set_title(
        "Monthly Road Accident Trends - 2023"
    )
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Cases")

    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "06_monthly_trends_2023.png",
        dpi=180,
        bbox_inches="tight"
    )
    plt.close()

    # Chart 7: Rural and urban comparison

    area_data = rural_urban.loc[
        rural_urban.year == 2023
    ].copy()

    area_long = area_data.melt(
        id_vars="area",
        value_vars=[
            "accidents",
            "persons_killed"
        ],
        var_name="measure",
        value_name="count"
    )

    plt.figure(figsize=(8, 5))

    ax = sns.barplot(
        data=area_long,
        x="area",
        y="count",
        hue="measure"
    )

    ax.set_title(
        "Rural vs Urban Road Accidents - 2023"
    )
    ax.set_xlabel("Area")
    ax.set_ylabel("Number of Cases")

    plt.tight_layout()

    plt.savefig(
        CHART_DIR / "07_rural_urban_2023.png",
        dpi=180,
        bbox_inches="tight"
    )
    plt.close()

    print("Four charts created successfully.")


if _name_ == "_main_":

    data = load_tables()

    make_friend_charts(data)
