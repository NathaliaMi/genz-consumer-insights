"""
data_utils.py
--------------
Shared helper functions for loading and lightly enriching the two source
datasets used throughout this project:

1. data/survey_responses.csv     -> 5,000-row synthetic Gen Z consumer survey
2. data/industry_benchmarks.csv  -> ~50 real-world, third-party benchmark
                                     stats (with source/year/notes columns)

Both the Jupyter notebook (notebooks/analysis.ipynb) and the Streamlit app
(app.py) import from this module so the two stay in sync.
"""

from pathlib import Path
import pandas as pd

# Project root is one level up from this file (src/ -> project root)
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

SURVEY_PATH = DATA_DIR / "survey_responses.csv"
BENCHMARK_PATH = DATA_DIR / "industry_benchmarks.csv"


def load_survey(path: Path = SURVEY_PATH) -> pd.DataFrame:
    """Load the 5,000-respondent synthetic Gen Z survey and add a handful
    of convenience columns used across the analysis (age cohort, income
    quartile, monthly income, discretionary spend as % of income).
    """
    df = pd.read_csv(path)

    # --- convenience / derived columns -----------------------------------
    df["age_cohort"] = pd.cut(
        df["age"], bins=[17, 22, 28], labels=["18-22 (younger Gen Z)", "23-28 (older Gen Z)"]
    )
    df["income_quartile"] = pd.qcut(
        df["annual_income_usd"], 4, labels=["Q1 (lowest)", "Q2", "Q3", "Q4 (highest)"]
    )
    df["monthly_income_usd"] = df["annual_income_usd"] / 12
    df["discretionary_pct_of_income"] = (
        df["monthly_discretionary_usd"] / df["monthly_income_usd"] * 100
    )
    return df


def load_benchmarks(path: Path = BENCHMARK_PATH) -> pd.DataFrame:
    """Load the third-party industry benchmark table (already tidy)."""
    df = pd.read_csv(path)
    return df


def trust_gap_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Mean trust in traditional advertising vs. influencers, long-format,
    ready to hand to a bar chart.
    """
    out = pd.DataFrame(
        {
            "channel": ["Traditional ads", "Influencers"],
            "avg_trust_1to5": [
                df["trust_traditional_ads_1to5"].mean(),
                df["trust_influencers_1to5"].mean(),
            ],
        }
    )
    return out


CATEGORICAL_COLUMNS = [
    "gender",
    "region",
    "ethnicity",
    "education",
    "employment",
    "primary_platform",
    "preferred_shopping_channel",
    "uses_buy_now_pay_later",
    "brand_discovery_channel",
]

NUMERIC_COLUMNS = [
    "age",
    "annual_income_usd",
    "daily_screen_hours",
    "val_sustainability_1to5",
    "val_brand_authenticity_1to5",
    "trust_traditional_ads_1to5",
    "trust_influencers_1to5",
    "monthly_discretionary_usd",
]
