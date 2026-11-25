/* Session 488: swaps the Home community block for design ?opt=1..4. Before (no opt) is the plain draft. */
(function () {
  var m = location.search.match(/[?&]opt=(\d)/); if (!m) return;
  var W = {
    h: '<em>Achology</em> Is a Collaborative Learning Community',
    lead: 'Members study the same courses, practise together at live events and, in time, learn to lead those events themselves.',
    s: [
      ['Learn Together', "Every weekday, members meet online to talk through what they're studying and try it out with each other. You don't need to know anything first, only to be willing to take part."],
      ['Learn to Lead', 'Members who train as hosts run the workshops and discussions. Leading a group builds facilitation skills you only learn by doing, and counts toward your next member level.'],
      ['Serve at the Centre', 'Accredited members can apply to coach, mentor and run events at The Centre of Human Development, by Achology, a new home for people who want to grow, opening in 2027.']
    ],
    centre: '<a class="cx-link" href="/centre-of-human-development/">Discover the Centre of Human Development</a>',
    event: '<a class="cx-link" href="/events/">Join a Free Event This Week</a>',
    levels: ['Verified Member', 'Certified Achologist', 'Achologist Adept', 'Senior Achologist I', 'Senior Achologist II', 'Master Achologist']
  };
  var IC = {
    together: '<svg class="cx-ic" viewBox="0 0 56 56" aria-hidden="true"><circle cx="15" cy="20" r="4.5"/><circle cx="28" cy="15" r="4.5"/><circle cx="41" cy="20" r="4.5"/><path d="M8 34c1-5 4-8 7-8s6 3 7 8M21 29c1-5 4-8 7-8s6 3 7 8M34 34c1-5 4-8 7-8s6 3 7 8"/><path d="M8 42h40"/><circle class="o" cx="28" cy="42" r="3"/></svg>',
    lead: '<svg class="cx-ic" viewBox="0 0 56 56" aria-hidden="true"><circle cx="28" cy="10" r="4.5"/><path d="M21 26c1-6 4-9 7-9s6 3 7 9"/><circle cx="13" cy="36" r="4"/><circle cx="28" cy="40" r="4"/><circle cx="43" cy="36" r="4"/><path d="M7 48c1-4 3-6 6-6s5 2 6 6M22 52c1-4 3-6 6-6s5 2 6 6M37 48c1-4 3-6 6-6s5 2 6 6"/><circle class="o" cx="28" cy="10" r="2"/></svg>',
    centre: '<svg class="cx-ic" viewBox="0 0 56 56" aria-hidden="true"><circle class="o" cx="44" cy="10" r="4.5"/><path d="M8 46h40M10 24 28 13l18 11M12 24h32M15 27v16M23 27v16M33 27v16M41 27v16M11 43h34"/></svg>'
  };
  function rail(cls) { return '<ol class="cx-rail ' + (cls || '') + '" aria-label="The six member levels">' + W.levels.map(function (l) { return '<li>' + l + '</li>'; }).join('') + '</ol>'; }
  function head() { return '<h2 class="cx-h" id="cx-h">' + W.h + '</h2><p class="cx-lead">' + W.lead + '</p>'; }

  function pawn(x, y, s, cls) { s = s || 1; return '<g class="' + (cls || 'pawn') + '"><circle cx="' + x + '" cy="' + (y - 7 * s) + '" r="' + 5 * s + '"/><path d="M' + (x - 8 * s) + ' ' + (y + 9 * s) + 'c0-6 3.5-10 ' + 8 * s + '-10s' + 8 * s + ' 4 ' + 8 * s + ' 10z"/></g>'; }
  function ring(cx, cy, r, n, start) { var o = ''; for (var i = 0; i < n; i++) { var a = (start + i * 360 / n) * Math.PI / 180; o += pawn(cx + r * Math.cos(a), cy + r * Math.sin(a), .8); } return o; }

  var O = {};
  /* 1. The Widening Circle: the member at the centre, each ring a wider circle of people */
  O[1] = function () {
    var c = 260, svg = '<svg viewBox="0 0 520 520" role="img" aria-label="A member at the centre of three widening circles: learning together, leading a group, and the Centre of Human Development">'
      + '<circle class="ring" cx="260" cy="260" r="92"/><circle class="ring" cx="260" cy="260" r="164"/><circle class="ring r3" cx="260" cy="260" r="236"/>'
      + '<circle class="halo" cx="260" cy="260" r="40"/>' + pawn(c, c + 4, 1.6, 'pawn me')
      + ring(c, c, 92, 5, -90) + ring(c, c, 164, 8, -68)
      + '<g transform="translate(436 96)"><circle class="badge" r="16"/><text class="bn" text-anchor="middle" y="5">3</text></g>'
      + '<g transform="translate(376 144)"><circle class="badge" r="16"/><text class="bn" text-anchor="middle" y="5">2</text></g>'
      + '<g transform="translate(325 195)"><circle class="badge" r="16"/><text class="bn" text-anchor="middle" y="5">1</text></g>'
      + '<g class="bld" transform="translate(232 -2)"><path d="M0 48h56M2 26 28 12l26 14M4 26h48M8 29v17M18 29v17M38 29v17M48 29v17"/></g><circle class="sun" cx="282" cy="2" r="6"/>'
      + '<text class="lab" x="260" y="-18" text-anchor="middle">The Centre of Human Development</text>'
      + '</svg>';
    return '<div class="cx-in"><div>' + head()
      + '<ol class="c1-steps">' + W.s.map(function (s, i) { return '<li><span class="cx-n">' + (i + 1) + '</span><div><p class="cx-ov">' + s[0] + '</p><p class="cx-p">' + s[1] + '</p></div></li>'; }).join('') + '</ol>'
      + '<div class="c1-links">' + W.centre + W.event + '</div></div>'
      + '<div class="c1-art">' + svg + '</div>'
      + '<div class="c1-rail">' + rail() + '</div></div>';
  };
  /* 2. Stepping Stones: three rooms that rise, the last one opening onto the Centre */
  O[2] = function () {
    var ic = [IC.together, IC.lead, IC.centre];
    return '<div class="cx-in"><div class="c2-top"><div>' + head() + '</div>'
      + '<div class="c2-cta"><p>Four of these live events are free for anyone, every week.</p><a class="cx-btn cx-ghost" href="/events/">Join a Free Event This Week</a></div></div>'
      + '<div class="c2-stones"><svg class="c2-path" viewBox="0 0 1104 72" preserveAspectRatio="none" aria-hidden="true"><path d="M60 140 C 220 40, 320 120, 540 90 S 900 20, 1050 0"/></svg>'
      + W.s.map(function (s, i) {
        return '<div class="c2-stone">' + ic[i] + '<p class="cx-ov"><span class="cx-n">' + (i + 1) + '</span>' + (i === 2 ? '<span class="c2-soon">Opening 2027</span>' : '') + '</p><h3 class="cx-t3">' + s[0] + '</h3><p class="cx-p">' + s[1] + '</p><span class="spacer"></span>' + (i === 2 ? W.centre : '') + '</div>';
      }).join('') + '</div>'
      + '<div class="c2-rail">' + rail() + '</div></div>';
  };
  /* 3. Statement and Path: the promise on the left, the road down the right, ending at the Centre */
  O[3] = function () {
    return '<div class="cx-in"><div class="c3-left">' + head() + '<a class="cx-btn" href="/events/">Join a Free Event This Week</a></div>'
      + '<ol class="c3-path">'
      + '<li class="c3-step"><span class="cx-n">1</span><div><h3 class="cx-t3">' + W.s[0][0] + '</h3><p class="cx-p">' + W.s[0][1] + '</p></div></li>'
      + '<li class="c3-step"><span class="cx-n">2</span><div><h3 class="cx-t3">' + W.s[1][0] + '</h3><p class="cx-p">' + W.s[1][1] + '</p><ol class="c3-levels" aria-label="The six member levels">' + W.levels.map(function (l) { return '<li>' + l + '</li>'; }).join('') + '</ol></div></li>'
      + '<li class="c3-dest"><span class="cx-n">3</span><span class="c3-yr" aria-hidden="true"><span class="yr">2027</span></span><p class="cx-ov">Opening 2027</p><h3 class="cx-t3">' + W.s[2][0] + '</h3><p class="cx-p">' + W.s[2][1] + '</p>' + W.centre + '</li>'
      + '</ol></div>';
  };
  /* 4. One Ground, Four Rooms: a bento of the promise and its three parts */
  O[4] = function () {
    return '<div class="cx-in"><div class="c4-grid">'
      + '<div class="c4-tile c4-a">' + head() + W.event + '</div>'
      + '<div class="c4-tile c4-b">' + IC.together + '<p class="cx-ov"><span class="cx-n">1</span></p><h3 class="cx-t3">' + W.s[0][0] + '</h3><p class="cx-p">' + W.s[0][1] + '</p></div>'
      + '<div class="c4-tile c4-c">' + IC.lead + '<p class="cx-ov"><span class="cx-n">2</span></p><h3 class="cx-t3">' + W.s[1][0] + '</h3><p class="cx-p">' + W.s[1][1] + '</p>'
      + '<div class="c4-mini" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span></div><div class="c4-mini-l"><span>Verified Member</span><span>Master Achologist</span></div></div>'
      + '<div class="c4-tile c4-d"><span class="yr" aria-hidden="true">2027</span><div><p class="cx-ov" style="margin-top:0"><span class="cx-n">3</span>Opening 2027</p><h3 class="cx-t3">' + W.s[2][0] + '</h3><p class="cx-p">' + W.s[2][1] + '</p><p style="margin:24px 0 0">' + W.centre + '</p></div>'
      + '<svg viewBox="0 0 200 160" aria-hidden="true"><path class="rays" d="M150 34a30 30 0 0 0-60 0M164 34a44 44 0 0 0-88 0"/><circle class="sun" cx="120" cy="34" r="14"/><g class="bld" transform="translate(30 50)"><path d="M0 100h140M6 46 70 14l64 32M10 46h120M20 52v44M44 52v44M70 52v44M96 52v44M120 52v44M8 96h124"/></g></svg></div>'
      + '</div></div>';
  };


  /* 5. Four Rooms, refined */
  O[5] = function () {
    return '<div class="cx-in"><div class="c5-grid">'
      + '<div class="c5-intro">' + head() + '<p class="c5-act"><a class="cx-btn cx-ghost" href="/events/">Join a Free Event This Week</a></p></div>'
      + '<div class="c5-room c5-r1"><div class="c5-top"><svg class="c5-bc" viewBox="-14 -38 124 124" overflow="visible" aria-hidden="true" focusable="false"><g class="c5-wv"><circle cx="48" cy="48" r="20" style="--s:1.9;--t:3.6s;--d:0s"/></g><circle cx="48" cy="48" r="20" fill="#ED6922" fill-opacity=".16"/><circle cx="6" cy="52.9" r="5.5" fill="#FFC08F"/><path d="M-4.3 71.2 A10.3 11.0 0 0 1 16.3 71.2 Z" fill="#FFC08F"/><circle cx="90" cy="52.9" r="5.5" fill="#FFC08F"/><path d="M79.7 71.2 A10.3 11.0 0 0 1 100.3 71.2 Z" fill="#FFC08F"/><circle cx="48" cy="39.4" r="6.7" fill="#ED6922"/><path d="M35.4 61.7 A12.6 13.4 0 0 1 60.6 61.7 Z" fill="#ED6922"/></svg><span class="c5-no">01</span></div><h3 class="cx-t3">' + W.s[0][0] + '</h3><p class="cx-p">' + W.s[0][1] + '</p></div>'
      + '<div class="c5-room c5-r2"><div class="c5-top"><svg class="c5-bc" viewBox="-14 -26 124 124" overflow="visible" aria-hidden="true" focusable="false"><g class="c5-wv"><circle cx="48" cy="48" r="20" style="--s:3.2;--t:3.0s;--d:0s"/><circle cx="48" cy="48" r="20" style="--s:3.2;--t:3.0s;--d:-1s"/><circle cx="48" cy="48" r="20" style="--s:3.2;--t:3.0s;--d:-2s"/></g><circle cx="48" cy="48" r="20" fill="#ED6922" fill-opacity=".16"/><circle cx="48" cy="-10.364" r="4.958" fill="#FFC08F"/><path d="M38.7 6.1 A9.3 9.9 0 0 1 57.3 6.1 Z" fill="#FFC08F"/><circle cx="94.8" cy="71.136" r="4.958" fill="#FFC08F"/><path d="M85.5 87.6 A9.3 9.9 0 0 1 104.1 87.6 Z" fill="#FFC08F"/><circle cx="1.2" cy="71.136" r="4.958" fill="#FFC08F"/><path d="M-8.1 87.6 A9.3 9.9 0 0 1 10.5 87.6 Z" fill="#FFC08F"/><circle cx="48" cy="39.4" r="6.7" fill="#ED6922"/><path d="M35.4 61.7 A12.6 13.4 0 0 1 60.6 61.7 Z" fill="#ED6922"/></svg><span class="c5-no">02</span></div><h3 class="cx-t3">' + W.s[1][0] + '</h3><p class="cx-p">' + W.s[1][1] + '</p>'
      + '<div class="c5-ladder" role="img" aria-label="Six member levels, from Verified Member to Master Achologist"><div class="c5-bars"><span></span><span></span><span></span><span></span><span></span><span></span></div><div class="c5-ends"><span>Verified Member</span><span>Master Achologist</span></div></div></div>'
      + '<div class="c5-room c5-r3"><div class="c5-top"><span class="c5-no">03 &nbsp;·&nbsp; Opening 2027</span></div>'
      + '<svg class="c5-art" viewBox="0 0 184 150" aria-hidden="true"><path class="rays" d="M140 40a32 32 0 0 0-64 0M156 40a48 48 0 0 0-96 0"/><circle class="sun" cx="108" cy="40" r="14"/><g class="bld" transform="translate(22 58)"><path d="M0 84h140M6 38 70 8l64 30M10 38h120M20 44v36M44 44v36M70 44v36M96 44v36M120 44v36M8 80h124"/></g><path class="ground" d="M4 146h176"/></svg>'
      + '<h3 class="cx-t3">' + W.s[2][0] + '</h3><p class="cx-p">' + W.s[2][1] + '</p><p class="c5-go"><a class="cx-link" href="/centre-of-human-development/">Discover the Centre of Human Development</a></p></div>'
      + '</div></div>';
  };

  /* 6. Four Rooms in order (Kain, Session 488): heading and line across the top, then 1, 2, 3 in one row */
  O[6] = function () {
    var h = O[5]();
    h = h.replace('<div class="c5-grid">', '<div class="c6-head"><h2 class="cx-h" id="cx-h">' + W.h + '</h2><p class="cx-lead">' + W.lead + '</p></div><div class="c5-grid c6-grid">');
    h = h.replace(/<div class="c5-intro">[\s\S]*?<\/p><\/div>/, '');
    h = h.replace('<span class="c5-no">01</span></div><h3 class="cx-t3">' + W.s[0][0] + '</h3><p class="cx-p">' + W.s[0][1] + '</p></div>',
      '<span class="c5-no">01</span></div><h3 class="cx-t3">' + W.s[0][0] + '</h3><p class="cx-p">' + W.s[0][1] + '</p><p class="c5-go"><a class="cx-link" href="/events/">Join a Free Event This Week</a></p></div>');
    h = h.replace('<span class="c5-no">03 &nbsp;·&nbsp; Opening 2027</span>', '<span class="c5-no">Opening 2027</span><span class="c5-no">03</span>');
    return h;
  };

  /* 7. Four Rooms in order, with this week's four free tickets under them (Kain, Session 488) */
  O[7] = function () {
    var h = O[6]();
    h = h.replace('<p class="c5-go"><a class="cx-link" href="/events/">Join a Free Event This Week</a></p>', '<p class="c5-go"><a class="cx-link c7-down" href="#c7-free">See This Week\'s Free Events</a></p>');
    var arrow = '<span class="c7-disc" aria-hidden="true"></span>';
    var ev = [['Monday', '2:00 pm', 'Thought-Provoking Group Discussion'], ['Wednesday', '6:00 pm', 'Live Personal Development Tutorial'], ['Thursday', '9:30 am', 'Thought-Provoking Group Discussion'], ['Friday', '2:30 pm', 'Applied Psychology Skills Workshop']];
    var t = '<div class="c7-free" id="c7-free"><div class="c7-head"><h3 class="c7-h">Join a Complimentary <em>Achology</em> Event This Week</h3>'
      + '<p class="c7-under">All times listed below are in your local time zone, so please choose whichever option is most convenient for you.</p></div>'
      + '<ul class="c7-evs">' + ev.map(function (e) {
        return '<li class="c7-ev"><a class="c7-cover" href="/events/" tabindex="-1" aria-hidden="true"></a>'
          + '<div class="c7-stub"><span class="c7-day">' + e[0] + '</span><span class="c7-time">' + e[1] + '</span><span class="c7-acc">Free</span></div>'
          + '<div class="c7-paper"><span class="c7-name">' + e[2] + '</span><a class="c7-go" href="/events/">Join This Event ' + arrow + '</a></div></li>';
      }).join('') + '</ul></div>';
    return h.replace(/<\/div><\/div>$/, '</div>' + t + '</div>');
  };

  /* 8. the same, with Kain's signed tickets exactly as on the Membership page: two across, paper then stub (Session 488) */
  O[8] = function () {
    return O[7]().replace('<ul class="c7-evs">', '<ul class="c7-evs c8-evs">');
  };

  function swap() {
    var sec = document.getElementById('home-community'); if (!sec) return;
    var n = +m[1]; if (!O[n]) return;
    sec.className = 'cx c' + n + (n >= 6 ? ' c5 c6' : '') + (n === 8 ? ' c7' : ''); sec.setAttribute('aria-labelledby', 'cx-h');
    sec.innerHTML = O[n]();
  }
  var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = '/com488/com.css?v=' + Date.now(); document.head.appendChild(l);
  if (document.readyState !== 'loading') swap(); else document.addEventListener('DOMContentLoaded', swap);
})();
