
from project_utils import load_tables


def inspect_tables(tables):
    """Show the size, columns and sample rows of each table."""

    print("DATA TABLE OVERVIEW")

    for name, table in tables.items():

        print(f"\n{name}: {table.shape[0]} rows, {table.shape[1]} columns")

        print("Columns:", ", ".join(table.columns))

        print(table.head(3).to_string(index=False))


if __name__ == "__main__":

    data = load_tables()

    inspect_tables(data)
