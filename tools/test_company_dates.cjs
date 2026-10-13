const assert = require('node:assert/strict');
const { companyDate } = require('../public/assets/company-date.js');

for (const [date, year, age] of [
  ['2026-10-14T00:00:00Z', 2026, 17],
  ['2026-12-31T16:59:59.999Z', 2026, 17],
  ['2026-12-31T17:00:00.000Z', 2027, 18],
  ['2027-12-31T17:00:00.000Z', 2028, 19],
  ['2028-02-29T12:00:00Z', 2028, 19],
]) {
  const now = new Date(date);
  const actual = companyDate(now);
  assert.equal(actual.year, year, date);
  assert.equal(actual.age, age, date);
  assert(actual.nextYear > now.getTime());
}
assert.equal(companyDate(new Date('2026-12-31T16:59:59.999Z')).nextYear,
  Date.parse('2026-12-31T17:00:00.000Z'));
console.log('PASS: Jakarta New Year boundary, successive years and leap year.');

// Exercise the actual page updater, including a tab kept open over midnight.
const vm = require('node:vm');
const fs = require('node:fs');
let clock = Date.parse('2026-12-31T16:59:59.999Z');
class ClockDate extends Date {
  constructor(...args) { super(...(args.length ? args : [clock])); }
}
const ages = [{}, {}, {}], years = [{}], listeners = {};
let scheduled, delay;
const context = {
  Date:ClockDate,
  document:{hidden:false, documentElement:{classList:{add:() => {}}},
    querySelectorAll:selector => selector === '[data-company-age]' ? ages : years,
    addEventListener:(name, listener) => { listeners[name] = listener; }},
  window:{addEventListener:(name, listener) => { listeners[name] = listener; }},
  setTimeout:(callback, milliseconds) => { scheduled = callback; delay = milliseconds; return 1; },
  clearTimeout:() => {},
};
vm.runInNewContext(fs.readFileSync(require.resolve('../public/assets/company-date.js'), 'utf8'), context);
assert(ages.every(node => node.textContent === 17));
assert.equal(years[0].textContent, 2026);
assert.equal(delay, 101);
clock = Date.parse('2026-12-31T17:00:00.100Z');
scheduled();
assert(ages.every(node => node.textContent === 18));
assert.equal(years[0].textContent, 2027);
assert(delay <= 2147483647);
clock = Date.parse('2027-12-31T17:00:00Z');
listeners.visibilitychange();
assert(ages.every(node => node.textContent === 19));
clock = Date.parse('2028-12-31T17:00:00Z');
listeners.pageshow();
assert(ages.every(node => node.textContent === 20));
console.log('PASS: all age fields, copyright, open-tab rollover, timer limit and tab resume.');
