import json, html
exec(open('build3.py').read().split("blocks = section(1")[0])
def bar():
    parts = ''.join(('<details class="cf-dd"><summary><span class="cfb-l">%s <span class="cf-sum" data-sum="%s" hidden></span></span><span class="cfb-v" data-blank="%s">%s</span>%s</summary>'
                     '<div class="cf-pop"><p class="cf-pop-h">%s</p><div class="cf-chips">%s</div></div></details>') % (E(FA[k]['label']), k, k, E(FA[k]['any']), CHEV_D, E(QUEST[k]), chips(k)) for k in ORDER)
    return '<div class="cfb-bar">%s</div>' % parts
def sec(n, cls, inner):
    return section(n, inner).replace('class="d-block cf cf%d"' % n, 'class="d-block cf cf%d %s"' % (n, cls), 1)
CH = '<div class="cf-chosen" hidden></div>'
blocks = (sec(1, 'cfA', bar() + CH) + sec(2, 'cfB', '<div class="cfb-panel">' + bar() + CH + '</div>') +
          sec(3, 'cfC', bar() + CH) + sec(4, 'cfD', bar() + CH) + sec(5, 'cfE', bar() + CH))
CSS = open('finder.css').read(); JS = open('finder-data.js').read() + open('finder.js').read()
page = open('site/previews/home-page-s558/home-base.html').read()
page = page.replace('</head>', '<style id="cf-css">' + CSS + '</style></head>', 1)
mark = '<section class="d-block pf pf2 pfp rvb hpp hpp--1" id="home-proof"'
page = page.replace(mark, blocks + '<script>' + JS + '</script>\n' + mark, 1)
open('site/previews/home-page-s558/home-finder-look.html', 'w').write(page)
print('ok')
