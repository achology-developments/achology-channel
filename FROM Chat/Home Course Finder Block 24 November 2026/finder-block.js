/* The course finder, Home block 3 (Chat, Session 487). One engine, four ways to drive it. */
(function () {
  var F = window.FINDER, P = F.products, FA = F.facets;
  var g = new URLSearchParams(location.search).get('g'); document.documentElement.setAttribute('data-g', g === null ? '5' : g);
  var Q = new URLSearchParams(location.search), FL = { qs: Q.get('qs') === '1', pm: Q.get('pm') === '1', st: Q.get('st') === '1' };
  Object.keys(FL).forEach(function (k) { document.documentElement.classList.toggle('cf-has-' + k, FL[k]); });
  var STAR = '<svg class="cf-star" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>';
  var KIND = { 'Course': 0, 'Course and membership': 1, 'School bundle': 2, 'The Whole Academy': 3, 'Membership': 4 };
  var EXACT = { c001: [5, 59.80], c019: [5, 19.40], c020: [5, 19.40], c021: [5, 19.40], c022: [5, 19.40], c023: [5, 19.40], c024: [5, 19.40], c025: [5, 19.40], c026: [5, 19.40], c027: [5, 19.40], scbp: [6, 164.50], pass: [12, 249.58] };
  var ORDER = ['subject', 'route', 'depth', 'time', 'price', 'school'];
  function money(v) { return '$' + (Math.round(v * 100) / 100).toLocaleString('en-US', { minimumFractionDigits: v % 1 ? 2 : 0, maximumFractionDigits: 2 }); }
  function monthly(p) { if (p.id === 'memb-m') return 34.5; if (!p.plans || !p.plans.length) return null; return p.plans[p.plans.length - 1][1]; }
  var WORD = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'];
  function cnt(n) { return n < 10 ? WORD[n] : String(n); }
  function payLine(p) {
    if (p.id === 'memb-m') return 'Then $34.50 a month';
    if (p.id === 'memb-a') return 'Paid Once a Year';
    if (!p.plans) return 'Paid Once';
    var last = p.plans[p.plans.length - 1];
    return 'Or ' + cnt(last[0]) + ' Monthly Payments of ' + money(last[1]);
  }
  function newState() { return { subject: [], route: [], depth: [], time: null, price: null, month: null, school: [] }; }
  function fits(p, s, skip) {
    skip = skip || {};
    var memb = p.kind === 'Membership';
    if (!skip.subject && s.subject.length && !memb && !s.subject.some(function (x) { return p.subjects.indexOf(x) > -1; })) return false;
    if (!skip.route && s.route.length && !memb && !s.route.some(function (x) { return p.routes.indexOf(x) > -1; })) return false;
    if (!skip.depth && s.depth.length && (memb || !s.depth.some(function (x) { return p.depth.indexOf(x) > -1; }))) return false;
    if (!skip.time && s.time !== null) { if (p.hours === null) return false; var lim = FA.time.lims[s.time]; if (s.time === FA.time.opts.length - 1 ? p.hours <= 50 : p.hours > lim) return false; }
    if (!skip.price && s.price !== null) { var pl = FA.price.lims[s.price]; if (s.price === FA.price.lims.length - 1 ? p.price > pl : p.price >= pl) return false; }
    if (!skip.price && s.month !== null) { var m = monthly(p); if (m === null ? p.price > s.month : m > s.month) return false; }
    if (!skip.school && s.school.length && !memb && !s.school.some(function (x) { return p.schools.indexOf(x) > -1; })) return false;
    return true;
  }
  function score(p, s) { return s.subject.filter(function (x) { return p.subjects && p.subjects.indexOf(x) > -1; }).length; }
  function results(s) {
    var list = P.filter(function (p) { return fits(p, s); }), note = '';
    if (!list.length) {
      var chosen = ORDER.filter(function (k) { return k === 'price' ? (s.price !== null || s.month !== null) : (Array.isArray(s[k]) ? s[k].length : s[k] !== null); });
      for (var i = chosen.length - 1; i >= 0 && !list.length; i--) {
        var sk = {}; sk[chosen[i]] = true;
        list = P.filter(function (p) { return fits(p, s, sk); });
        if (list.length) note = 'Nothing fits every choice. These are the nearest, without your ' + FA[chosen[i]].label.toLowerCase() + ' choice.';
      }
    }
    var none = !ORDER.some(function (k) { return Array.isArray(s[k]) ? s[k].length : s[k] !== null; }) && s.month === null;
    list.sort(function (a, b) {
      if (none) { var TOP = { c001: -4, pass: -3, 'memb-m': -2 }, pa = a.id in TOP ? TOP[a.id] : KIND[a.kind], pb = b.id in TOP ? TOP[b.id] : KIND[b.kind]; if (pa !== pb) return pa - pb; if (a.students || b.students) return (b.students || 0) - (a.students || 0); }
      return (score(b, s) - score(a, s)) || (KIND[a.kind] - KIND[b.kind]) || (a.price - b.price);
    });
    return { list: list, note: note };
  }
  var CHEV = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 18 6-6-6-6"></path></svg>';
  function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function kindOf(p) { return p.line1; }
  /* line 3, the formula: stars | students | hours of on-demand teaching | membership included */
  function figs(p) {
    var bits = [];
    if (p.stars) { bits.push(STAR + '<span>' + p.stars + '</span>'); bits.push('<span>' + p.studentsLabel + ' Students</span>'); }
    if (p.hrs) bits.push('<span>' + p.hrs + ' Hours of On-Demand Teaching</span>');
    if (p.live) bits.push('<span>' + p.live + '</span>');
    if (p.memb) bits.push('<span>' + esc(p.memb) + '</span>');
    return '<span class="cf-figs">' + bits.join('<i class="cf-hair" aria-hidden="true"></i>') + '</span>';
  }
  function row(p, s) {
    var sc = p.home ? ' style="--sc:var(--school-' + p.home + '-primary);--st:var(--school-' + p.home + '-text,var(--school-' + p.home + '-primary))"' : '';
    return '<li><a class="cf-row" href="' + p.url + '"' + sc + '><span class="cf-pic"><img src="' + p.img + '" alt="" width="56" height="56" loading="lazy" decoding="async"></span><span class="cf-main"><span class="cf-kind' + (p.badge ? ' cf-badge' : '') + '">' + esc(kindOf(p)) + '</span><span class="cf-name">' + esc(p.name) + '</span>' + figs(p) + '</span>' +
      priceHtml(p, s) + '<span class="cf-go">' + CHEV + '</span></a></li>';
  }
  function priceHtml(p, s) {
    var big = p.id === 'memb-m' ? '$7 <i>First Month</i>' : money(p.price), small = payLine(p);
    if (s.monthlyView) {
      if (p.id === 'memb-m') { big = '$7 <i>First Month</i>'; small = 'Then $34.50 a month'; }
      else if (p.id === 'memb-a') { big = '$345 <i>a Year</i>'; small = 'Paid once'; }
      else if (p.plans) {
        var ns = p.plans.map(function (x) { return x[0]; });
        big = 'From ' + money(p.plans[p.plans.length - 1][1]) + ' <i>a Month</i>';
        small = 'Pay over ' + (ns.length > 1 ? ns.slice(0, -1).join(', ') + ' or ' + ns[ns.length - 1] : ns[0]) + ' months';
      } else { small = 'Paid once'; }
    }
    return '<span class="cf-price"><b>' + big + '</b><small>' + esc(small) + '</small></span>';
  }
  function render(root, s) {
    var r = results(s), out = root.querySelector('.cf-out'), all = root.classList.contains('cf-all');
    var n = r.list.length, shown = all ? r.list : r.list.slice(0, 6);
    var any = ORDER.some(function (k) { return Array.isArray(s[k]) ? s[k].length : s[k] !== null; }) || s.month !== null;
    out.innerHTML = '<div class="cf-top"><p class="cf-count">' + (any ? '<b>' + n + '</b> ' + (n === 1 ? 'fits' : 'fit') + ' your choices<button type="button" class="cf-clear">Clear all</button>' : 'All <b>' + n + '</b> courses, schools and plans') + '</p>' +
      '<div class="cf-seg" role="tablist" aria-label="How to show prices"><button type="button" role="tab" data-view="full" aria-selected="' + (s.monthlyView ? 'false' : 'true') + '">Pay In Full</button><button type="button" role="tab" data-view="monthly" aria-selected="' + (s.monthlyView ? 'true' : 'false') + '">Pay Monthly</button></div></div>' +
      (r.note ? '<p class="cf-note">' + r.note + '</p>' : '') + '<ul class="cf-list">' + shown.map(function (p) { return row(p, s); }).join('') + '</ul>' +
      (n > 6 ? '<p class="cf-more"><button type="button" class="cf-toggle">' + (all ? 'Show fewer' : 'Show all ' + n) + '</button></p>' : '');
    root.querySelectorAll('[data-k]').forEach(function (b) {
      var k = b.getAttribute('data-k'), v = b.getAttribute('data-v');
      if (v === null) return;
      var on = Array.isArray(s[k]) ? s[k].indexOf(v) > -1 : String(s[k]) === v;
      if (k === 'price' && s.month !== null) on = false;
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    root.querySelectorAll('[data-sum]').forEach(function (el) {
      var k = el.getAttribute('data-sum'), c = Array.isArray(s[k]) ? s[k].length : (s[k] !== null || (k === 'price' && s.month !== null) ? 1 : 0);
      el.textContent = c ? String(c) : ''; el.hidden = !c;
    });
    root.querySelectorAll('[data-blank]').forEach(function (el) {
      var k = el.getAttribute('data-blank'), f = FA[k], t;
      if (Array.isArray(s[k])) t = s[k].length ? (k === 'school' ? s[k].map(function (x) { return f.opts[f.keys.indexOf(x)]; }) : s[k]).join(' or ') : f.any;
      else if (k === 'price' && s.month !== null) t = 'up to ' + money(s.month) + ' a month';
      else t = s[k] === null ? f.any : f.opts[s[k]];
      el.textContent = t;
    });
    var chosen = root.querySelector('.cf-chosen');
    if (chosen) {
      var bits = [];
      ORDER.forEach(function (k) {
        var f = FA[k];
        if (Array.isArray(s[k])) s[k].forEach(function (v) { bits.push([k, v, k === 'school' ? f.opts[f.keys.indexOf(v)] : v]); });
        else if (s[k] !== null) bits.push([k, String(s[k]), f.opts[s[k]]]);
      });
      if (s.month !== null) bits.push(['month', '', 'Up to ' + money(s.month) + ' a Month']);
      chosen.innerHTML = bits.map(function (b) { return '<button type="button" class="cf-pill" data-x="' + b[0] + '" data-xv="' + esc(b[1]) + '">' + esc(b[2]) + ' <span aria-hidden="true">&times;</span><span class="screen-reader-text"> remove</span></button>'; }).join('') +
        (bits.length ? '<button type="button" class="cf-clear">Clear all</button>' : '');
      chosen.hidden = !bits.length;
    }
    hairs(root);
  }
  /* a short hairline shows only between two things on the same line, never at a line's start or end */
  function hairs(scope) {
    scope.querySelectorAll('.cf-hair').forEach(function (h) { h.style.display = ''; });
    scope.querySelectorAll('.cf-hair').forEach(function (h) {
      var a = h.previousElementSibling, b = h.nextElementSibling;
      if (!a || !b || Math.abs(a.getBoundingClientRect().top - b.getBoundingClientRect().top) > 4) h.style.display = 'none';
    });
  }
  window.addEventListener('resize', function () { document.querySelectorAll('.cf').forEach(hairs); });
  function toggle(s, k, v) {
    if (k === 'time' || k === 'price') { var i = +v; s[k] = s[k] === i ? null : i; if (k === 'price') s.month = null; return; }
    var a = s[k], j = a.indexOf(v); if (j > -1) a.splice(j, 1); else a.push(v);
  }
  document.querySelectorAll('.cf').forEach(function (root) {
    var s = newState(); root._s = s;
    root.addEventListener('click', function (e) {
      var b = e.target.closest('[data-k][data-v]');
      if (b) { toggle(s, b.getAttribute('data-k'), b.getAttribute('data-v')); if (root.getAttribute('data-single') && !Array.isArray(s[b.getAttribute('data-k')])) { var d = b.closest('details'); if (d) d.open = false; } render(root, s); return; }
      var x = e.target.closest('.cf-pill');
      if (x) { var k = x.getAttribute('data-x'), v = x.getAttribute('data-xv'); if (k === 'month') s.month = null; else if (Array.isArray(s[k])) s[k].splice(s[k].indexOf(v), 1); else s[k] = null; render(root, s); return; }
      if (e.target.closest('.cf-clear')) { var n = newState(); Object.keys(n).forEach(function (k) { s[k] = n[k]; }); var m = root.querySelector('.cf-month input'); if (m) m.value = ''; render(root, s); return; }
      var sv = e.target.closest('.cf-seg [data-view]'); if (sv) { s.monthlyView = sv.getAttribute('data-view') === 'monthly'; render(root, s); root.querySelector('.cf-seg [aria-selected="true"]').focus(); return; }
      var q = e.target.closest('[data-preset]');
      if (q) { var n2 = newState(); n2.monthlyView = s.monthlyView; var pr = JSON.parse(q.getAttribute('data-preset')); Object.keys(pr).forEach(function (k) { n2[k] = pr[k]; }); Object.keys(n2).forEach(function (k) { s[k] = n2[k]; }); root.querySelectorAll('[data-preset]').forEach(function (o) { o.setAttribute('aria-pressed', o === q ? 'true' : 'false'); }); render(root, s); return; }
      if (e.target.closest('.cf-toggle')) { root.classList.toggle('cf-all'); render(root, s); return; }
    });
    root.addEventListener('input', function (e) {
      if (!e.target.matches('.cf-month input')) return;
      var v = parseFloat(e.target.value); s.month = isNaN(v) || v <= 0 ? null : v; if (s.month !== null) s.price = null; render(root, s);
    });
    // option 4: the sentence's blanks
    root.querySelectorAll('.cf4-btn').forEach(function (b) {
      b.addEventListener('click', function () {
        var pop = b.nextElementSibling, open = pop.hidden;
        root.querySelectorAll('.cf4-dd .cf-pop').forEach(function (p) { p.hidden = true; p.previousElementSibling.setAttribute('aria-expanded', 'false'); });
        pop.hidden = !open; b.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
    });
    root.addEventListener('click', function (e) { var c = e.target.closest('.cf4-dd [data-k][data-v]'); if (c && !Array.isArray(s[c.getAttribute('data-k')])) { var pp = c.closest('.cf-pop'); pp.hidden = true; pp.previousElementSibling.setAttribute('aria-expanded', 'false'); } });
    // one open menu at a time
    root.querySelectorAll('details.cf-dd').forEach(function (d) { d.addEventListener('toggle', function () { if (d.open) root.querySelectorAll('details.cf-dd').forEach(function (o) { if (o !== d) o.open = false; }); }); });
    // option 2: one question at a time
    var steps = root.querySelectorAll('.cf2-q');
    if (steps.length) {
      var at = 0, show = function () { steps.forEach(function (q, i) { q.hidden = i !== at; }); root.querySelector('.cf2-n').textContent = 'Question ' + (at + 1) + ' of ' + steps.length; root.querySelector('.cf2-back').disabled = at === 0; root.querySelector('.cf2-next').textContent = at === steps.length - 1 ? 'Start again' : 'Next question'; };
      root.querySelector('.cf2-next').addEventListener('click', function () { if (at === steps.length - 1) { at = 0; root.querySelector('.cf-clear') && root.querySelector('.cf-clear').click(); } else at++; show(); });
      root.querySelector('.cf2-back').addEventListener('click', function () { if (at) at--; show(); });
      show();
    }
    render(root, s);
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.cf4-dd')) document.querySelectorAll('.cf4-dd .cf-pop').forEach(function (p) { p.hidden = true; }); if (!e.target.closest('details.cf-dd')) document.querySelectorAll('details.cf-dd[open]').forEach(function (d) { d.open = false; }); });
})();
