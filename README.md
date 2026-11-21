# Hands-On Data Lab Implementation

**Task 2 — Data Analyst Internship (YuvaIntern)**

A complete, reproducible data-analysis lab built on a realistic Indian retail
orders dataset. The project covers environment setup, data manipulation with
pandas and NumPy, visualisation with Matplotlib and Seaborn, and a structured
exploratory analysis with business findings.

## 1. Project overview

This project demonstrates an end-to-end analytics workflow: setting up an isolated
Python environment, building and cleaning a deliberately imperfect dataset, deriving
business metrics, aggregating and reshaping the data, producing publication-ready
visualisations, and communicating findings with supporting evidence.

## 2. Business problem and objectives

A fictional Indian multi-city retailer, **Kiran Retail**, needs to understand the
performance of its first half of 2025. The raw order export is messy — duplicates,
missing values, inconsistent casing, stray spaces and mixed date formats. The
objectives are to clean the data, quantify category, regional, segment and monthly
performance, and surface actionable findings.

## 3. Tools and technologies

Python 3.13 · pandas · NumPy · Matplotlib · Seaborn · SciPy · JupyterLab · Git

## 4. Project features

* Isolated virtual environment with pinned dependencies (`requirements.txt`).
* Programmatic environment verification with PASS/FAIL checks and assertions.
* Reproducible data generation using `np.random.default_rng(42)`.
* A 30-row raw dataset with five realistic data-quality problems.
* A complete cleaning pipeline with documented imputation decisions.
* Derived business metrics: gross revenue, discount amount, net revenue, total cost,
  profit, profit margin, order month, order quarter and value classification.
* Grouped aggregations, a pivot table and a regional-target merge.
* Four publication-ready charts saved at 150 DPI.
* A KPI summary, a findings table, quality checks and limitations.

## 5. Directory structure

```
Hands_On_Data_Lab/
├── README.md
├── requirements.txt
├── verify_environment.py
├── Hands_On_Data_Lab.ipynb
├── Hands_On_Data_Lab_Report.docx
├── data/
│   ├── raw_retail_orders.csv
│   └── cleaned_retail_orders.csv
└── outputs/
    ├── 01_category_revenue_profit.png
    ├── 02_monthly_trend.png
    ├── 03_segment_order_value.png
    ├── 04_discount_margin.png
    ├── category_summary.csv
    └── monthly_summary.csv
```

## 6. Dataset description

`data/raw_retail_orders.csv` holds 30 order records (28 unique) across 12 Indian
cities and 5 product categories, with 13 columns: `order_id`, `order_date`,
`customer_id`, `city`, `region`, `product_category`, `product_name`, `units_sold`,
`unit_price`, `unit_cost`, `discount_percentage`, `customer_segment` and
`payment_mode`. All monetary values are in INR.

## 7. Environment setup

```bash
# Windows PowerShell
python -m venv .venv
.\\\.venv\\Scripts\\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

## 8. Installation

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 9. Running the notebook

```bash
jupyter lab
# then open Hands_On_Data_Lab.ipynb and run all cells top to bottom
```

To reproduce the executed notebook from scratch:

```bash
jupyter nbconvert --execute --to notebook --inplace Hands_On_Data_Lab.ipynb
```

## 10. Verification

```bash
python verify_environment.py
```

The script checks the Python version, every required library, the project folders
and key files, and a seeded reproducibility draw.

## 11. Exercises covered

| Section | Exercises |
|---|---|
| 1 | Virtual environment, dependency freeze, JupyterLab launch, kernel selection, environment verification |
| 2 | Inspection, cleaning, imputation, dedupe, text standardisation, date parsing, filtering, slicing, sorting, calculated metrics, grouping, pivot tables, merging |
| 3 | Grouped bar chart, monthly line chart, box plot, scatter with regression line and Pearson correlation |
| 4 | KPI analysis, findings table, quality checks, limitations, conclusion |

## 12. Key findings

* Electronics leads revenue (₹1,26,548.46) but earns only a 2.9% margin.
* Beauty is the margin leader at 36.0% with ₹20,120 profit.
* Discount percentage and profit margin correlate strongly and negatively (r = −0.87).
* Premium customers average ₹19,101 per order, ahead of New customers at ₹12,725.
* One 60-unit bulk order accounts for 18.2% of net revenue — a concentration risk.

## 13. Visualisation previews

| Chart 1 — Revenue and profit by category | Chart 2 — Monthly revenue trend |
|---|---|
| ![Chart 1](outputs/01_category_revenue_profit.png) | ![Chart 2](outputs/02_monthly_trend.png) |

| Chart 3 — Order value by segment | Chart 4 — Discount vs profit margin |
|---|---|
| ![Chart 3](outputs/03_segment_order_value.png) | ![Chart 4](outputs/04_discount_margin.png) |

All four charts are saved at 150 DPI and embedded in
`Hands_On_Data_Lab_Report.docx`.

## 14. Limitations

* Small sample of 28 unique orders from a single retailer.
* Synthetic data: patterns are illustrative, not market evidence.
* Missing values were imputed with median or mode values.
* A small number of unusual orders (bulk, clearance, premium) are retained and flagged.
* Correlations are observational and do not establish causation.

## 15. Future improvements

* Connect to a live order database or API instead of a CSV export.
* Add customer-level cohort and repeat-purchase analysis.
* Automate the quality checks in a CI job.
* Extend the dashboard with Plotly or a BI tool.

## 16. Author

Prepared as Task 2 of the Data Analyst Internship portfolio. Environment and
dependency versions are recorded in `requirements.txt`.
