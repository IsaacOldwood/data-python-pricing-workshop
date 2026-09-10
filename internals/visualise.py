import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv("policies.csv")

# Style
sns.set_theme(style="whitegrid")

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Vehicle age distribution
sns.histplot(data=df, x="vehicle_age", bins=15, ax=axes[0, 0])
axes[0, 0].set_title("Vehicle Age Distribution")

# 2. Mileage distribution
sns.histplot(data=df, x="annual_mileage", bins=20, ax=axes[0, 1])
axes[0, 1].set_title("Annual Mileage Distribution")

# 3A. Vehicle value distribution
sns.histplot(data=df, x="vehicle_value_at_new", bins=20, ax=axes[1, 0])
axes[1, 0].set_title("Vehicle Value Distribution")

# 3B. Vehicle value distribution (KDE)
sns.kdeplot(data=df, x="vehicle_value_at_new", bw_adjust=0.5, fill=True, ax=axes[1, 1])
axes[1, 1].set_title("Vehicle Value Distribution (KDE)")


plt.tight_layout()
plt.show()
