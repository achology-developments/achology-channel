import json, html
exec(open('build4.py').read().split("CH = '<div")[0])
CH = '<div class="cf-chosen" hidden></div>'
PRESETS = [('New to all of this', {'depth': ['Introductory']}), ('I want to help others', {'route': ['Professional Certification']}),
           ('Looking after my mental health', {'route': ['Mental Wellness']}), ('Short courses', {'time': 1}), ('Under $100', {'price': 0})]
HAIR = '<i class="cf-hair" aria-hidden="true"></i>'
QS = '<div class="cf-qs2" role="group" aria-label="Quick starts"><span class="cf-qs2-l">Not sure where to start? Try</span>%s</div>' % HAIR.join(
    "<button type=\"button\" class=\"cf-q2\" aria-pressed=\"false\" data-preset='%s'>%s</button>" % (json.dumps(p), E(l)) for l, p in PRESETS)
blocks = sec(5, 'cfE', bar() + QS + CH)
CSS = open('finder.css').read() + open('finder-great2.css').read(); JS = open('finder-data.js').read() + open('finder3.js').read()
page = open('site/previews/home-page-s558/home-base.html').read()
page = page.replace('</head>', '<style id="cf-css">' + CSS + '</style></head>', 1)
mark = '<section class="d-block pf pf2 pfp rvb hpp hpp--1" id="home-proof"'
page = page.replace(mark, blocks + '<script>' + JS + '</script>\n' + mark, 1)
open('site/previews/home-page-s558/home-finder-v6.html', 'w').write(page)
print('ok')
