# Descale math

The citric acid dose for the kettle, the descaling calendar hard water demands, and what homemade costs against the branded sachets. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/descalemath/

## The three tools

- **Dose plan** - `dosePlan(volumeMl, strengthGPerL)`: grams of citric acid and heaped tablespoons.
- **Schedule plan** - `schedulePlan(intervalDays, minutesPerCycle)`: cycles per year, minutes and hours of maintenance.
- **Cost plan** - `costPlan(gramsPerCycle, cyclesPerYear, kgPriceDollars, sachetsPerCycle, sachetPriceDollars)`: homemade versus sachet cost and the savings.

## Labeled norms (illustrative references, not rules)

- Strength: 20 g per liter; a heaped tablespoon is about 15 g. Interval: 45 days in hard-water areas, 90 in soft. Prices: $8 a kilo loose against $3 a sachet, 2 sachets a cycle. The appliance manual's instructions win, and never mix descalers or acids with bleach.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (12 cases, 57 checks)

Regenerate the oracle expectations: `python3 oracle.py`
