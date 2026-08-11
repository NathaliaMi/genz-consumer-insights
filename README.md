#  Gen Z Consumer Insights

An end-to-end Python data analysis project exploring a 5,000-respondent Gen Z consumer
survey — screen time, spending, platform habits, trust in ads vs. influencers, and shopping
values — cross-checked against **~50 real, cited industry statistics** (Bank of America Institute,
PwC, Circana/WSJ, Experian, NRF/ICSC).



## Key findings

1. **The ad-trust / influencer-trust gap is the sharpest signal in the data.** Traditional ads
   average **2.33/5** trust vs. **3.39/5** for influencers — and that ~1-point gap holds steady
   across every region, gender, income level, and platform.
2. **Discretionary spending is a near-fixed ~22% of income**, regardless of employment status —
   income predicts spend almost perfectly (r ≈ 0.88); *how* someone earns it barely matters.
3. **BNPL (Buy Now, Pay Later) adoption (~42%) is flat across income quartiles** — it reads as a
   generational payment preference here, not narrowly a low-income workaround.
4. **Social media is the #1 brand-discovery channel (40.8%)** — ahead of search, word-of-mouth,
   influencer content, and traditional ads combined.
5. **Screen time barely varies by primary platform** (a tight 5.9–6.2 hr/day band across TikTok,
   Instagram, YouTube, Reddit, Snapchat, and X).

##  Anomalies worth flagging

- **Attitudinal variables are almost uncorrelated with demographics or each other** (mostly
  |r| < 0.05, aside from income↔spend). The analysis treats it as the honest finding it is:
  good for practicing EDA, not a basis for causal "segment X thinks Y" claims.
- **9 respondents (0.18%) report 3+ σ above mean screen time** (up to 16 hrs/day) — plausible,
  but flagged for a sanity check before high-stakes use.
- **"Non-binary" (n=92) and "Prefer not to say" (n=45)** gender groups are small enough that any
  differences involving them should be read as directional, not statistically robust.

Full write-up, including *why* the flat correlation matrix matters, is in Section 6–8 of the
notebook and the "Findings & Anomalies" tab of the dashboard.

##  What this could mean in a broader context

The survey's clearest signals — low trust in traditional ads, and spending that tracks income
tightly rather than identity — line up with independent, real-world research on Gen Z as a cohort:

- Gen Z's **global spending power is projected to roughly quadruple, from ~$2.7 trillion in 2024
  to $12.6 trillion by 2030**, per the Bank of America Institute's *"Gen Z: A new economic force"*
  report — even as many individuals report real budget pressure.
  ([Bank of America Institute, 2025](https://institute.bankofamerica.com/economic-insights/genz-new-economic-force.html))
- Yet **U.S. Gen Z spending fell ~13% between January and April 2025**, concentrated in apparel,
  accessories, and electronics — per PwC's analysis of ~1 million consumer transactions, read as
  a shift toward value-consciousness rather than simple frugality.
  ([PwC, "Gen Z Consumer Trends," 2025](https://www.pwc.com/us/en/industries/consumer-markets/library/gen-z-consumer-trends.html))
- Gaming — often assumed recession-proof for a young, online-first generation — saw an even
  sharper pullback: **weekly video-game spending among 18–24-year-olds fell ~25% year-over-year**,
  per Circana data reported by the *Wall Street Journal*, versus under 5% for older generations.
  ([reported via PC Gamer, 2025](https://www.pcgamer.com/gaming-industry/new-study-shows-that-gen-z-is-spending-way-less-money-on-videogames-than-older-gamers/))
- Credit behavior stays comparatively conservative: Experian puts **Gen Z's average credit card
  balance at ~$3,493** as of mid-2025 — lowest of any adult generation, though growing faster
  year-over-year than older cohorts.
  ([Experian, 2025](https://www.experian.com/blogs/ask-experian/research/credit-card-debt-by-age/))
- And **85% of Gen Z say social media influences their purchasing decisions**, per a 2025 ICSC
  report — directly consistent with this survey's trust gap and social-led discovery findings.
  ([Retail Dive, 2025](https://www.retaildive.com/news/generation-z-social-media-influence-shopping-behavior-purchases-tiktok-instagram/652576/))

**Takeaway:** both the survey and the cited research point to a generation with large *aggregate*
long-run spending power and a structurally low baseline of trust in traditional marketing, but one
currently spending more cautiously than that long-run power would suggest — an argument for
earning attention through credible, peer- and creator-level channels rather than traditional ads,
without assuming today's caution is permanent.

*(Every stat quoted above is paraphrased from, and linked to, its original source — see
`data/industry_benchmarks.csv` for the full list of ~50 benchmarks with sources, years, and notes,
including places where different 2025 reports disagree.)*

---

##  Sample visuals

<table>
<tr>
<td><img src="assets/trust_gap.png" width="400"/></td>
<td><img src="assets/correlation_heatmap.png" width="400"/></td>
</tr>
<tr>
<td><img src="assets/income_vs_discretionary.png" width="400"/></td>
<td><img src="assets/bnpl_by_income.png" width="400"/></td>
</tr>
</table>

The Streamlit dashboard (`app.py`) covers the same ground interactively, with live filters for
region, gender, employment, age, and platform.

---

## Project structure

```
genz-consumer-insights/
├── app.py                        # Interactive Streamlit dashboard
├── requirements.txt
├── LICENSE
├── data/
│   ├── survey_responses.csv      # 5,000-row  Gen Z survey (18 columns)
│   └── industry_benchmarks.csv   # ~50 real, cited external stats (source/year/notes)
├── notebooks/
│   └── analysis.ipynb            # Full written EDA, pre-executed
├── src/
│   └── data_utils.py             # Shared loading/cleaning functions 
└── assets/                       # Chart images exported from the notebook (used in this README)
```

## Quickstart

```bash
# 1. Clone and enter the repo
git clone https://github.com/<your-username>/genz-consumer-insights.git
cd genz-consumer-insights

# 2. Install dependencies (a virtual environment is recommended)
pip install -r requirements.txt

# 3a. Run the interactive dashboard
streamlit run app.py


## Data dictionary

**`survey_responses.csv`** (5,000 rows, synthetic):

| Column | Description |
|---|---|
| `respondent_id` | Unique ID |
| `age`, `gender`, `region`, `ethnicity`, `education`, `employment` | Demographics |
| `annual_income_usd`, `monthly_discretionary_usd` | Financials |
| `primary_platform`, `daily_screen_hours` | Media habits |
| `val_sustainability_1to5`, `val_brand_authenticity_1to5` | Stated values (Likert 1–5) |
| `trust_traditional_ads_1to5`, `trust_influencers_1to5` | Trust (Likert 1–5) |
| `preferred_shopping_channel`, `uses_buy_now_pay_later`, `brand_discovery_channel` | Shopping behavior |

**`industry_benchmarks.csv`** (~50 rows, real, cited): `category`, `metric`, `value`, `unit`,
`population`, `source`, `year`, `notes` — five categories: `social_media`, `gaming`,
`income_spending`, `dining`, `shopping_values`.


MIT —  Survey data is synthetic and free to reuse; benchmark statistics
remain the property of their original publishers  and should be cited back to them
if reused elsewhere.

