import json, html
exec(open('build_kh.py').read().split("def tile(")[0])   # icons, SV, LAB, ARR
C = json.load(open('kh-cards.json'))
E = lambda s: html.escape(s, quote=False)
KIND = {'article': 'article', 'book': 'book-note', 'quote': 'quote', 'workbook': 'workbook'}
def tile(k, c):
    lab = '<span class="pk-label"><i>%s</i>%s</span>' % (SV(IC[k]), LAB[k])
    body = '<span class="bx-tile__body">%s<span class="pk-title">%s</span><span class="bx-sub">%s</span>%s</span>' % (
        lab, E(c['title']), E(c['sum']), ('<span class="pk-meta">%s</span>' % c['meta']) if c.get('meta') else '')
    if k == 'article':
        pic = '<span class="bx-tile__img"><img src="%s" width="1360" height="649" alt="" loading="lazy" decoding="async"></span>' % c['img']; cls = 'bx-tile--article'
    elif k == 'book':
        pic = '<span class="bx-tile__img"><span class="bk"><img src="%s" width="240" height="368" alt="" loading="lazy" decoding="async"></span></span>' % c['img']; cls = 'bx-tile--book-note'
    elif k == 'workbook':
        pic = '<span class="bx-tile__img"><span class="wk"><img src="%s" width="232" height="300" alt="" loading="lazy" decoding="async"></span></span>' % c['img']; cls = 'bx-tile--workbook'
    else:
        pic = '<span class="bx-tile__img"><img src="%s" width="2400" height="1260" alt="" loading="lazy" decoding="async"></span>' % c['img']; cls = 'bx-tile--article hk-quote'
    return '<li class="bx-item hk-item" data-kind="%s"><a class="bx-tile %s" href="%s"> %s %s </a></li>' % (KIND[k], cls, c['href'], pic, body)
ORDER = ['article', 'quote', 'book', 'workbook']
items = [(k, C[k][i]) for i in range(5) for k in ORDER]
ARROWS = ('<div class="hk-arrows"><button type="button" class="hk-arrow hk-prev" aria-label="Previous">%s</button>'
          '<button type="button" class="hk-arrow hk-next" aria-label="Next">%s</button></div>') % (SV('<path d="M19 12H5"></path><path d="m12 19-7-7 7-7"></path>'), SV(ARR))
tabs = ['<button type="button" class="hk-tab is-on bf-framed" data-k="all" aria-pressed="true"><span>Everything</span></button>'] + [
    '<button type="button" class="hk-tab" data-k="%s" aria-pressed="false">%s<span>%ss</span></button>' % (k, SV(IC[k]), LAB[k]) for k in ORDER]
block = ('<section class="d-block hk" id="home-kh" aria-labelledby="home-kh-h"><div class="d-inner">'
         '<div class="hk-head"><h2 class="d-title" id="home-kh-h"><span class="hk-tie">Start Learning, Right Now,</span> <span class="hk-tie">with Achology’s Knowledge Hub</span></h2></div>'
         '<p class="lead-bar d-sub">Thought-provoking reading to support a deeper understanding of yourself and those around you.</p>'
         '<div class="hk-pills" role="group" aria-label="Choose a kind of reading">%s</div>'
         '<div class="hk-belt">%s<ul class="hk-row">%s</ul></div>'
         '<p class="hk-foot"><a class="btn btn-secondary" href="/learn/">Browse the Knowledge Hub</a></p></div></section>') % (''.join(tabs), ARROWS, ''.join(tile(k, c) for k, c in items))
CSS = open('kh3.css').read() + open('lib.css').read(); JS = open('kh2.js').read().replace('.hc-item', '.hk-item')
page = open('site/previews/home-page-s558/home-proof.html').read()
# the Knowledge Hub's book shelf setting, as every Knowledge Hub page carries it, so the signed shelves draw
page = page.replace('<html ', '<html data-hk-shelf="1" ', 1)
page = page.replace('</head>', '<script>document.documentElement.classList.add("bg-book");document.documentElement.setAttribute("data-lib",new URLSearchParams(location.search).get("L")||"13");</script><style id="hk-css">' + CSS + '</style></head>', 1)
i = page.find('id="home-proof"'); j = page.find('</section>', i) + len('</section>')
k2 = page.find('<', j)
if page.startswith('<script', k2): j = page.find('</script>', k2) + len('</script>')
page = page[:j] + '\n' + block + '<script>' + JS + '</script>\n' + page[j:]
open('site/previews/home-page-s558/home-kh-final.html', 'w').write(page)
print('ok', len(items))
