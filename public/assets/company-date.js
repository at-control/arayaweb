/* Company age follows the calendar year in Jakarta, regardless of visitor timezone. */
(() => {
  const yearFormatter = new Intl.DateTimeFormat('en', {timeZone:'Asia/Jakarta', year:'numeric'});
  const companyDate = (now = new Date()) => {
    const year = Number(yearFormatter.format(now));
    return {year, age:year - 2009, nextYear:Date.UTC(year, 11, 31, 17)};
  };
  if (typeof module !== 'undefined' && module.exports) module.exports = {companyDate};
  if (typeof document === 'undefined') return;

  let nextUpdate;
  const refreshDates = () => {
    clearTimeout(nextUpdate);
    const now = new Date();
    const {year, age, nextYear} = companyDate(now);
    document.querySelectorAll('[data-company-age]').forEach(element => { element.textContent = age; });
    document.querySelectorAll('[data-current-year]').forEach(element => { element.textContent = year; });
    document.documentElement.classList.add('dates-ready');
    // Browser timers have a maximum delay; long waits are split safely.
    nextUpdate = setTimeout(refreshDates, Math.min(nextYear - now.getTime() + 100, 2147483647));
  };
  refreshDates();
  document.addEventListener('visibilitychange', () => { if (!document.hidden) refreshDates(); });
  window.addEventListener('pageshow', refreshDates);
})();
