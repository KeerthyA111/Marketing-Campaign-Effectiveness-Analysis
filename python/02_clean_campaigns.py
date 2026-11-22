"""Clean campaign names and channel categories using Pandas.
Adapted from original capstone code shared by project author.
Changes: relative paths and null-safe text conversion.
Requires data/Campaigns_raw_data.xlsx; see ../data/README.md.
"""
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "Campaigns_raw_data.xlsx"
OUTPUT_DIR = PROJECT_ROOT / "results"
OUTPUT_DIR.mkdir(exist_ok=True)

campaigns = pd.read_excel(INPUT_FILE)
pd.set_option("display.max_columns", None)

# Original project cleaning operations: whitespace trimming and typo corrections.
for column in ["CampaignID", "CampaignName", "Channel"]:
    campaigns[column] = campaigns[column].astype("string").str.strip()

correction_dict = {
    "e-mail": "Email",
    "E-mail": "Email",
    "Search Engine.": "Search Engine",
    "Social  Media": "Social Media",
    "Emal": "Email",
}
campaigns["Channel"] = campaigns["Channel"].replace(correction_dict)

valid_channels = {"Email", "Social Media", "Search Engine"}


def extract_channel(campaign_name):
    """Infer a known channel from campaign name; leave unknowns missing."""
    if pd.isna(campaign_name):
        return pd.NA
    lower_name = str(campaign_name).strip().lower()
    if "email" in lower_name:
        return "Email"
    if "search engine" in lower_name:
        return "Search Engine"
    if "social media" in lower_name:
        return "Social Media"
    return pd.NA


def standardize_channel(row):
    value = row["Channel"]
    if pd.notna(value):
        candidate = " ".join(str(value).split()).title()
        if candidate in valid_channels:
            return candidate
    return extract_channel(row["CampaignName"])

campaigns["Channel"] = campaigns.apply(standardize_channel, axis=1).astype("string")

print(campaigns.head(20))
print("Missing Channel values after cleaning:", campaigns["Channel"].isna().sum())

output_file = OUTPUT_DIR / "Campaigns_cleaned.xlsx"
campaigns.to_excel(output_file, index=False)
print(f"Cleaned campaigns saved to {output_file}")
