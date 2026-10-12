(function (root) {
  "use strict";
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }
  function money(c) { return "$" + Math.floor(c / 100) + "." + ("0" + (c % 100)).slice(-2); }

  function dosePlan(volumeMl, strengthGPerL) {
    if (!(volumeMl > 0) || !(strengthGPerL > 0)) return { error: "volume and strength must be positive" };
    var grams = Math.round(volumeMl * strengthGPerL / 1000);
    var spoons = Math.round(grams / 15);
    return { grams: grams, spoons: spoons };
  }

  function schedulePlan(intervalDays, minutesPerCycle) {
    if (!(intervalDays > 0) || !(minutesPerCycle > 0)) return { error: "interval and minutes must be positive" };
    var cycles = Math.ceil(365 / intervalDays);
    var minutesYear = cycles * minutesPerCycle;
    var hours = Math.round(minutesYear / 60 * 10) / 10;
    return { cycles: cycles, minutesYear: minutesYear, hours: hours };
  }

  function costPlan(gramsPerCycle, cyclesPerYear, kgPriceDollars, sachetsPerCycle, sachetPriceDollars) {
    if (!(gramsPerCycle > 0) || !(cyclesPerYear > 0) || !(kgPriceDollars > 0) || !(sachetsPerCycle > 0) || !(sachetPriceDollars > 0)) return { error: "grams, cycles, kilo price, sachets and sachet price must be positive" };
    var homeCents = Math.round(gramsPerCycle * cyclesPerYear / 1000 * kgPriceDollars * 100);
    var sachetCents = cyclesPerYear * sachetsPerCycle * sachetPriceDollars * 100;
    return { homeCents: homeCents, sachetCents: sachetCents, savedCents: sachetCents - homeCents };
  }

  function renderDose(r, volumeMl, strengthGPerL) {
    return "An appliance holding " + volumeMl + " ml at a labeled " + strengthGPerL + " g a liter: " + r.grams + " g of citric acid - " + plural(r.spoons, "heaped tablespoon") + ", topped up with water.";
  }

  function renderSchedule(r, intervalDays, minutesPerCycle) {
    return "Descaling every " + intervalDays + " days at a labeled " + minutesPerCycle + " minutes a cycle: " + plural(r.cycles, "cycle") + " a year, " + r.minutesYear + " minutes - " + r.hours + " hours of maintenance.";
  }

  function renderCost(r, gramsPerCycle, cyclesPerYear, kgPriceDollars, sachetsPerCycle, sachetPriceDollars) {
    return gramsPerCycle + " g a cycle and " + plural(cyclesPerYear, "cycle") + " a year, citric acid at $" + kgPriceDollars + " a kilo against " + plural(sachetsPerCycle, "sachet") + " a cycle at $" + sachetPriceDollars + " each: homemade runs " + money(r.homeCents) + " against " + money(r.sachetCents) + " - " + money(r.savedCents) + " stays with you.";
  }

  var api = { dosePlan: dosePlan, schedulePlan: schedulePlan, costPlan: costPlan, renderDose: renderDose, renderSchedule: renderSchedule, renderCost: renderCost };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.DescaleMath = api;
})(this);
