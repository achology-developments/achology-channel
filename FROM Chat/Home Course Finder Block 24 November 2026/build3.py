import json, html
D = json.loads(open('finder-data.js').read()[len('window.FINDER='):-1])
FA = D['facets']
E = lambda s: html.escape(s, quote=True)
ORDER = ['subject', 'route', 'depth', 'time', 'price', 'school']
CHEV_D = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg>'
TITLE = 'Find the Right Course or Learning Path for You'
LINE = 'Select as many options as you like to find relevant courses, schools and learning plans, each with a direct link to explore further.'
QUEST = {'subject': 'What would you like to learn?', 'route': 'What do you want from it?', 'depth': 'How deep would you like to go?',
         'time': 'How much time can you give it?', 'price': 'What would you like to pay?', 'school': 'Is there a school you have in mind?'}

def chips(k, cls='cf-chip'):
    f = FA[k]
    vals = f.get('keys') or (list(range(len(f['opts']))) if not f['multi'] else f['opts'])
    out = ''.join('<button type="button" class="%s" data-k="%s" data-v="%s" aria-pressed="false">%s</button>' % (cls, k, E(str(v)), E(o)) for v, o in zip(vals, f['opts']))
    if k == 'price':
        out += '<label class="cf-month"><span>Up to</span> $<input type="number" inputmode="decimal" min="1" step="1" placeholder="__" aria-label="Most you would like to pay a month"> <span>a Month</span></label>'
    return out

def head(n):
    return '<div class="cf-head"><h2 class="d-title" id="cf%d-h">%s</h2><p class="lead-bar d-sub">%s</p></div>' % (n, TITLE, LINE)

def section(n, inner, extra='', tail=''):
    return ('<section class="d-block cf cf%d" data-g="%d" id="home-finder-%d" aria-labelledby="cf%d-h"%s><div class="d-inner">%s%s<div class="cf-out" aria-live="polite"></div>%s</div></section>'
            % (n, n, n, n, extra, head(n), inner, tail))

# 1. THE FILTER BAR (Harvard's course finder): six menus in a row, choices shown as pills beneath
def opt1():
    menus = ''.join(('<details class="cf-dd"><summary>%s <span class="cf-sum" data-sum="%s" hidden></span>%s</summary>'
                     '<div class="cf-pop"><p class="cf-pop-h">%s</p><div class="cf-chips">%s</div></div></details>') % (E(FA[k]['label']), k, CHEV_D, E(QUEST[k]), chips(k)) for k in ORDER)
    return '<div class="cf1-bar">%s</div><div class="cf-chosen" hidden></div>' % menus

# 2. ONE QUESTION AT A TIME (MasterClass's opening question): six short questions, skip any
def opt2():
    qs = ''.join(('<div class="cf2-q" data-q="%s"><p class="cf2-ask">%s</p><div class="cf-chips cf2-chips">%s</div></div>') % (k, E(QUEST[k]), chips(k)) for k in ORDER)
    return ('<div class="cf2-card"><p class="cf2-n"></p>%s<div class="cf2-foot"><button type="button" class="cf2-back">Back</button>'
            '<span class="cf2-hint">Skip any question you like.</span><button type="button" class="btn btn-primary cf2-next">Next question</button></div></div>'
            '<div class="cf-chosen" hidden></div>') % qs

# 3. THE SIDE PANEL (Harvard and Coursera's catalogue): every choice down the left, results on the right
def opt3():
    groups = ''.join(('<details class="cf3-g"%s><summary>%s <span class="cf-sum" data-sum="%s" hidden></span>%s</summary><div class="cf-chips cf3-chips">%s</div></details>')
                     % (' open' if k in ('subject',) else '', E(FA[k]['label']), k, CHEV_D, chips(k, 'cf-chip cf3-chip')) for k in ORDER)
    return '<div class="cf3-wrap"><aside class="cf3-side" aria-label="Your choices">%s<div class="cf-chosen" hidden></div></aside>' % groups

# 4. THE SENTENCE (a sentence with blanks to fill): reads like the visitor speaking
def opt4():
    def blank(k):
        return ('<span class="cf4-dd"><button type="button" class="cf4-btn" aria-expanded="false"><span data-blank="%s">%s</span>%s</button><span class="cf-pop" hidden><span class="cf-pop-h">%s</span><span class="cf-chips">%s</span></span></span>'
                % (k, E(FA[k]['any']), CHEV_D, E(QUEST[k]), chips(k)))
    s = ('<div class="cf4-say">I&rsquo;d like to learn %s for %s, going %s deep, in %s, for %s, from %s.</div>'
         % (blank('subject'), blank('route'), blank('depth'), blank('time'), blank('price'), blank('school')))
    return s + '<div class="cf-chosen" hidden></div>'

blocks = section(1, opt1()) + section(2, opt2()) + section(3, opt3(), '', '</div>') + section(4, opt4(), ' data-single="1"')
CSS = open('finder.css').read(); JS = open('finder-data.js').read() + open('finder.js').read()
page = open('site/previews/home-page-s558/home-base.html').read()
page = page.replace('</head>', '<style id="cf-css">' + CSS + '</style></head>', 1)
mark = '<section class="d-block pf pf2 pfp rvb hpp hpp--1" id="home-proof"'
assert page.count(mark) == 1
page = page.replace(mark, blocks + '<script>' + JS + '</script>\n' + mark, 1)
open('site/previews/home-page-s558/home-finder.html', 'w').write(page)
print('ok')
