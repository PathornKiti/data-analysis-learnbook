# Ethics and responsible-analysis checklist

Complete this for your project and keep it with your data card. "N/A" is fine, but **think about each item**.

## Data and consent
- [ ] I am allowed to use this data (licence / terms of use / consent). Source and licence are in the data card.
- [ ] The data were collected ethically. If I collected them (survey, interviews), participants consented and know how data will be used.
- [ ] I removed or avoided **direct identifiers** (names, emails, phone numbers, ID numbers, exact addresses).
- [ ] I considered **indirect identification** (rare combinations such as age + job + neighbourhood). Small groups are suppressed or merged (e.g. counts under 5).
- [ ] Sensitive information (health, finances, location, beliefs, minors' data) is stored and shared appropriately, or not shared at all.
- [ ] No passwords, API keys or private data are committed to the repository (check `.gitignore`).

## Representation and bias
- [ ] I can say **who is in the data and who is missing**, and how that may skew results.
- [ ] I checked results for **different groups** where relevant (e.g. error rates of a model by group) and report differences.
- [ ] My variables are measured in the same way for everyone (no changes in definition over time or place).
- [ ] I avoided proxies for sensitive attributes unless there is a good, stated reason.

## Honest analysis
- [ ] I stated my questions **before** looking, and report **all** comparisons I ran, not just the ones that "worked".
- [ ] I report **uncertainty** (intervals, test-set performance), not only point estimates.
- [ ] I used baselines and held-out data when making predictions; I looked for leakage.
- [ ] I do not claim **causation** from observational data.
- [ ] My charts don't mislead (zero baselines, honest scales, nothing important hidden).

## Impact and communication
- [ ] I considered who could be **helped or harmed** if someone acted on my results, and wrote the conclusions in proportion to the evidence.
- [ ] Limitations are prominent, specific and written in plain language.
- [ ] I credited data sources, libraries, and any help (including AI tools or tutors), following my course's rules.
- [ ] I would be comfortable explaining my method to the people the data are about.

## Notes
(Anything you decided, and why. Future you will be grateful.)
