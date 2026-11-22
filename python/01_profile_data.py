"""Profile the four Marketing Campaign Effectiveness source tables.
Adapted from the original Pandas EDA script shared by the project author.
Changes: portable paths, correct conversion table printout, clearer output handling.
Requires input Excel files; see ../data/README.md.
"""
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_DIR.mkdir(exist_ok=True)

pd.set_option("display.max_columns", None)

customers = pd.read_excel(DATA_DIR / "Customer.xlsx", sheet_name="Customers")
conversions = pd.read_excel(DATA_DIR / "Customer.xlsx", sheet_name="Customer Conversions")
campaigns = pd.read_excel(DATA_DIR / "Campaigns.xlsx")
impressions_clicks = pd.read_excel(DATA_DIR / "Impressions, Clicks.xlsx")

sources = {
    "Customers": customers,
    "Customer Conversions": conversions,
    "Campaigns": campaigns,
    "Impressions and Clicks": impressions_clicks,
}

for name, table in sources.items():
    print(f"\n{name}: {table.shape[0]} rows, {table.shape[1]} columns")
    print(table.describe(include="all"))
    print(f"\nData types and non-null counts for {name}:")
    table.info()

summary_file = OUTPUT_DIR / "Description_statistics.xlsx"
with pd.ExcelWriter(summary_file, engine="xlsxwriter") as writer:
    customers.describe(include="all").to_excel(writer, sheet_name="Customers_Desc")
    conversions.describe(include="all").to_excel(writer, sheet_name="Conversions_Desc")
    campaigns.describe(include="all").to_excel(writer, sheet_name="Campaigns_Desc")
    impressions_clicks.describe(include="all").to_excel(writer, sheet_name="Impressions_Clicks_Desc")

print(f"\nDescriptive statistics saved to {summary_file}")
