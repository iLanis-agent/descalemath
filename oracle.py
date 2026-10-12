import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(n) + " " + (word if n == 1 else (form or word + "s"))
def money(c): return "$" + str(c // 100) + "." + str(c % 100).zfill(2)
def fmt(x): return str(jsnum(x))
def rnd(x): return math.floor(x + 0.5)

def dose_plan(volumeMl, strengthGPerL):
    if not (volumeMl > 0) or not (strengthGPerL > 0):
        return {"error": "volume and strength must be positive"}
    grams = rnd(volumeMl * strengthGPerL / 1000)
    return {"grams": grams, "spoons": rnd(grams / 15)}

def schedule_plan(intervalDays, minutesPerCycle):
    if not (intervalDays > 0) or not (minutesPerCycle > 0):
        return {"error": "interval and minutes must be positive"}
    cycles = math.ceil(365 / intervalDays)
    minutes = cycles * minutesPerCycle
    return {"cycles": cycles, "minutesYear": minutes, "hours": jsnum(rnd(minutes / 60 * 10) / 10)}

def cost_plan(gramsPerCycle, cyclesPerYear, kgPriceDollars, sachetsPerCycle, sachetPriceDollars):
    if not (gramsPerCycle > 0) or not (cyclesPerYear > 0) or not (kgPriceDollars > 0) or not (sachetsPerCycle > 0) or not (sachetPriceDollars > 0):
        return {"error": "grams, cycles, kilo price, sachets and sachet price must be positive"}
    home = rnd(gramsPerCycle * cyclesPerYear / 1000 * kgPriceDollars * 100)
    sachet = cyclesPerYear * sachetsPerCycle * sachetPriceDollars * 100
    return {"homeCents": home, "sachetCents": sachet, "savedCents": sachet - home}

def render_dose(r, volumeMl, strengthGPerL):
    return ("An appliance holding " + fmt(volumeMl) + " ml at a labeled " + fmt(strengthGPerL) + " g a liter: "
            + fmt(r["grams"]) + " g of citric acid - " + plural(r["spoons"], "heaped tablespoon") + ", topped up with water.")

def render_schedule(r, intervalDays, minutesPerCycle):
    return ("Descaling every " + fmt(intervalDays) + " days at a labeled " + fmt(minutesPerCycle) + " minutes a cycle: "
            + plural(r["cycles"], "cycle") + " a year, " + fmt(r["minutesYear"]) + " minutes - " + fmt(r["hours"]) + " hours of maintenance.")

def render_cost(r, gramsPerCycle, cyclesPerYear, kgPriceDollars, sachetsPerCycle, sachetPriceDollars):
    return (fmt(gramsPerCycle) + " g a cycle and " + plural(cyclesPerYear, "cycle") + " a year, citric acid at $"
            + fmt(kgPriceDollars) + " a kilo against " + plural(sachetsPerCycle, "sachet") + " a cycle at $"
            + fmt(sachetPriceDollars) + " each: homemade runs " + money(r["homeCents"]) + " against "
            + money(r["sachetCents"]) + " - " + money(r["savedCents"]) + " stays with you.")

cases = []
for a in [(1500, 20), (750, 20), (500, 25), (0, 20)]:
    r = dose_plan(*a)
    cases.append({"fn": "dosePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_dose(r, *a)})
for a in [(45, 20), (90, 25), (30, 15), (0, 20)]:
    r = schedule_plan(*a)
    cases.append({"fn": "schedulePlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_schedule(r, *a)})
for a in [(30, 9, 8, 2, 3), (15, 5, 10, 2, 4), (45, 13, 6, 2, 3), (0, 9, 8, 2, 3)]:
    r = cost_plan(*a)
    cases.append({"fn": "costPlan", "args": list(a), "result": r,
                  "render": None if "error" in r else render_cost(r, *a)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
