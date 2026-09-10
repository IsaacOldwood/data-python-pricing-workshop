import numpy as np
import pandas as pd

# ----------------------------
# Metadata
# ----------------------------
VEHICLE_COUNT = 1000
COLOURS = ["Red", "Blue", "Black", "White"]

rng = np.random.default_rng(42)

# ----------------------------
# Vehicle Value
# ----------------------------
VALUE_DISTRIBUTION = {
    "low": 0.35,
    "medium": 0.55,
    "high": 0.10,
}

LOW_VALUE_MIN = 1000
LOW_VALUE_MAX = 10000

MED_VALUE_MIN = 10001
MED_VALUE_MAX = 30000

HIGH_VALUE_MIN = 30001
HIGH_VALUE_MAX = 100000

value_band = rng.choice(
    ["low", "medium", "high"],
    size=VEHICLE_COUNT,
    p=list(VALUE_DISTRIBUTION.values()),
)

vehicle_value = np.zeros(VEHICLE_COUNT)

vehicle_value[value_band == "low"] = rng.integers(
    LOW_VALUE_MIN,
    LOW_VALUE_MAX + 1,
    size=(value_band == "low").sum(),
)

vehicle_value[value_band == "medium"] = rng.integers(
    MED_VALUE_MIN,
    MED_VALUE_MAX + 1,
    size=(value_band == "medium").sum(),
)

vehicle_value[value_band == "high"] = rng.integers(
    HIGH_VALUE_MIN,
    HIGH_VALUE_MAX + 1,
    size=(value_band == "high").sum(),
)

# ----------------------------
# Vehicle Age
# ----------------------------
AGE_DISTRIBUTION = {
    "new": 0.60,
    "medium": 0.30,
    "old": 0.10,
}

NEW_AGE_MIN = 0
NEW_AGE_MAX = 3

MED_AGE_MIN = 4
MED_AGE_MAX = 8

OLD_AGE_MIN = 9
OLD_AGE_MAX = 15

age_band = rng.choice(
    ["new", "medium", "old"],
    size=VEHICLE_COUNT,
    p=list(AGE_DISTRIBUTION.values()),
)

vehicle_age = np.zeros(VEHICLE_COUNT)

vehicle_age[age_band == "new"] = rng.integers(
    NEW_AGE_MIN,
    NEW_AGE_MAX + 1,
    size=(age_band == "new").sum(),
)

vehicle_age[age_band == "medium"] = rng.integers(
    MED_AGE_MIN,
    MED_AGE_MAX + 1,
    size=(age_band == "medium").sum(),
)

vehicle_age[age_band == "old"] = rng.integers(
    OLD_AGE_MIN,
    OLD_AGE_MAX + 1,
    size=(age_band == "old").sum(),
)

# ----------------------------
# Annual Mileage
# ----------------------------
ANNUAL_MILEAGE_MU = np.log(7000)
ANNUAL_MILEAGE_SIGMA = 0.5

annual_mileage = rng.lognormal(
    mean=ANNUAL_MILEAGE_MU,
    sigma=ANNUAL_MILEAGE_SIGMA,
    size=VEHICLE_COUNT,
).round().astype(int)

# ----------------------------
# Previous Claims
# ----------------------------
PREVIOUS_CLAIMS_DISTRIBUTION = {
    "low": 0.70,
    "medium": 0.25,
    "high": 0.05,
}

previous_claims = rng.choice(
    [0, 1, 2],
    size=VEHICLE_COUNT,
    p=list(PREVIOUS_CLAIMS_DISTRIBUTION.values()),
)

# ----------------------------
# Colour
# ----------------------------
colour = rng.choice(
    COLOURS,
    size=VEHICLE_COUNT,
)

# ----------------------------
# Create DataFrame
# ----------------------------
df = pd.DataFrame(
    {
        "vehicle_id": range(1, VEHICLE_COUNT + 1),
        "colour": colour,
        "vehicle_value_at_new": vehicle_value.astype(int),
        "vehicle_age": vehicle_age.astype(int),
        "annual_mileage": annual_mileage,
        "previous_claims": previous_claims,
    }
)

df.to_csv("vehicles.csv", index=False)

print(df.head())