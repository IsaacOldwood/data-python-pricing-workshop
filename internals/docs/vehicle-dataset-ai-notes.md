# Insurance Pricing Workshop Dataset Design

To keep the workshop focused on data analytics rather than regulatory or ethical discussions around protected characteristics, avoid using variables such as driver age. Instead, use characteristics related to the vehicle and its usage that have a clear and intuitive relationship to insurance risk.

## Potential Variables

### Vehicle Value

A simple and easy-to-understand factor.

- £5,000 vehicle → lower repair costs
- £50,000 vehicle → higher repair costs

Useful for teaching:

- Segmentation
- Grouping
- Visualisation

---

### Vehicle Age

Example bands:

- 0 to 3 years
- 4 to 8 years
- 9+ years

Potential relationships:

- Newer vehicles may be more expensive to repair.
- Older vehicles may have lower values but higher maintenance-related risks.

---

### Annual Mileage

Examples:

- 5,000 miles
- 10,000 miles
- 20,000 miles

A very intuitive relationship:

> More time on the road means more opportunity for accidents.

Useful for:

- Scatter plots
- Trend analysis
- Risk segmentation

---

### Previous Claims

One of the strongest and most intuitive predictors.

Example bands:

- 0 previous claims
- 1 previous claim
- 2+ previous claims

Participants can easily understand why previous claims history may indicate future risk.

---

## Recommended Dataset

For a beginner-friendly workshop, use only five core variables:

| Variable | Purpose |
|-----------|----------|
| Vehicle Value | Severity driver |
| Vehicle Age | Feature engineering |
| Annual Mileage | Frequency driver |
| Previous Claims | Strong predictor |
| Claim Cost | Target variable |

This provides a simple workflow:

1. Explore vehicle values.
2. Explore annual mileage.
3. Explore previous claims.
4. Create risk bands and factors.
5. Calculate expected claim costs.
6. Generate insurance premiums.

## Example Narrative

Participants discover patterns such as:

- High-mileage vehicles have more claims.
- High-value vehicles have more expensive claims.
- Vehicles with previous claims are riskier.

They then build a simple pricing model:

```text
Premium
=
Base Cost
× Mileage Factor
× Vehicle Value Factor
× Previous Claims Factor
```

This approach feels realistic, avoids protected characteristics, and creates opportunities to teach:

- Data cleaning
- Grouping and aggregation
- Data visualisation
- Feature engineering
- Basic modelling

The strongest combination of variables is likely:

- Previous Claims
- Annual Mileage
- Vehicle Value

These are easy to understand, clearly related to risk, and require no prior insurance knowledge from attendees.