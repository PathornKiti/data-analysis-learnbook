# Ethics and responsible-analysis checklist: worked example

## Data and consent
- [x] I am allowed to use this data (synthetic, from the course repository); source and licence are in the data card.
- [x] No data were collected from people.
- [x] There are no direct identifiers. N/A for indirect identification: the table contains daily totals only.
- [x] No sensitive information; nothing private is committed.

## Representation and bias
- [x] Who is in the data / who is missing: the data represent nobody real; the data card says what is absent (holidays, events, other years).
- [x] N/A: no group-level model comparisons (no people involved). If this were real trip data, I would check whether predictions are worse in some neighbourhoods.

## Honest analysis
- [x] Questions were stated first (PROPOSAL.md) and the full list of comparisons is: weekend vs weekday; one regression with three predictors; three models.
- [x] Uncertainty is reported (intervals, cross-validation spread); held-out data and a baseline were used for prediction.
- [x] No causal claims: conclusions use "goes with" language.
- [x] Charts use zero baselines for bars and state the finding in the title.

## Impact and communication
- [x] If a real operator used this to allocate bikes, a poor forecast on unusual days could leave stations empty or full; the limitations section says the model is only trustworthy within the temperature range seen.
- [x] Limitations are prominent and specific.
- [x] Sources and libraries are credited.
