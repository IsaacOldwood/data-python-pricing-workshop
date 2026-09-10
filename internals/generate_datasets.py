import random

import numpy as np
import pandas as pd


def generate_datasets() -> tuple[pd.DataFrame, pd.DataFrame]:
    # ----------------------------
    # Metadata
    # ----------------------------
    VEHICLE_COUNT = 2000 + random.randint(0, int(1000 * 0.1))
    COLOURS = ["Red", "Blue", "Black", "White"]

    rng = np.random.default_rng()

    # ----------------------------
    # Vehicle Value
    # ----------------------------
    VALUE_DISTRIBUTION = {
        "low": 0.225,
        "medium": 0.65,
        "high": 0.125,
    }

    LOW_VALUE_MIN = 1000
    LOW_VALUE_MAX = 9000

    MED_VALUE_MIN = 9_001
    MED_VALUE_MAX = 22_500

    HIGH_VALUE_MIN = 22_501
    HIGH_VALUE_MAX = 50_000

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

    n = (value_band == "high").sum()

    values = HIGH_VALUE_MIN + rng.exponential(
        scale=10000,
        size=n,
    )

    vehicle_value[value_band == "high"] = np.clip(
        values,
        HIGH_VALUE_MIN,
        HIGH_VALUE_MAX,
    ).astype(int)

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

    annual_mileage = (
        rng.lognormal(
            mean=ANNUAL_MILEAGE_MU,
            sigma=ANNUAL_MILEAGE_SIGMA,
            size=VEHICLE_COUNT,
        )
        .round()
        .astype(int)
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
            "policy_number": [f"POL#{i:04d}" for i in range(1, VEHICLE_COUNT + 1)],
            "colour": colour,
            "vehicle_value_at_new": vehicle_value.astype(int),
            "vehicle_age": vehicle_age.astype(int),
            "annual_mileage": annual_mileage,
        }
    )

    df.to_csv("policies.csv", index=False)

    # ----------------------------
    # Generate Claims Dataset
    # ----------------------------

    claims_records = []

    shuffled_df = df.sample(frac=1, random_state=rng).reset_index(drop=True)

    for _, policy in shuffled_df.iterrows():
        # Frequency model
        claim_rate = 0.05

        # Mileage effect
        claim_rate += policy["annual_mileage"] / 100000

        # Vehicle age effect
        claim_rate += policy["vehicle_age"] * 0.01

        # Cap frequency
        claim_rate = min(claim_rate, 1.5)

        # Number of claims this year
        claim_count = rng.poisson(claim_rate)

        for claim_num in range(claim_count):
            # Severity factor by vehicle value
            severity_mean = policy["vehicle_value_at_new"] * 0.08

            claim_amount = rng.lognormal(
                mean=np.log(max(severity_mean, 100)),
                sigma=0.8,
            )

            # Cap very large claims
            claim_amount = min(
                claim_amount,
                policy["vehicle_value_at_new"] * 1.2,
            )

            claims_records.append(
                {
                    "claim_number": f"CLM#{len(claims_records) + 1:04d}",
                    "policy_number": policy["policy_number"],
                    "claim_amount": round(claim_amount, 2),
                }
            )

    claims_df = pd.DataFrame(claims_records)

    claims_df.to_csv("claims.csv", index=False)
    return df, claims_df


if __name__ == "__main__":
    df, claims_df = generate_datasets()
    print(f"Policies: {len(df)}")
    print(f"Claims: {len(claims_df)}")
    print(f"Policies with claims: {claims_df['policy_number'].nunique()}")
