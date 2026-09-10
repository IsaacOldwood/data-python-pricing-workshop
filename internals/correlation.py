import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# -----------------------------------------------------------------------------
# Load data
# -----------------------------------------------------------------------------

policies = pd.read_csv("policies.csv")
claims = pd.read_csv("claims.csv")

# -----------------------------------------------------------------------------
# Aggregate claims to policy level
# -----------------------------------------------------------------------------

claims_summary = (
    claims.groupby("policy_number")
    .agg(
        claim_count=("claim_number", "count"),
        average_claim_cost=("claim_amount", "mean"),
    )
    .reset_index()
)

# -----------------------------------------------------------------------------
# Merge policy and claims data
# -----------------------------------------------------------------------------

df = policies.merge(claims_summary, on="policy_number", how="left")

# Policies with no claims
df["claim_count"] = df["claim_count"].fillna(0)
df["average_claim_cost"] = df["average_claim_cost"].fillna(0)

# -----------------------------------------------------------------------------
# Correlation Matrix
# -----------------------------------------------------------------------------

correlation_columns = [
    "vehicle_value_at_new",
    "vehicle_age",
    "annual_mileage",
    "claim_count",
    "average_claim_cost",
]

corr = df[correlation_columns].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    center=0,
    vmin=-1,
    vmax=1,
)

plt.title("Policy Feature Correlations")
plt.tight_layout()
plt.show()
