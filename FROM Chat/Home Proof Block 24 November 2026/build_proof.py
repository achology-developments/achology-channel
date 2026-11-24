import re, json, html
sec = open('rvb_nlp.html').read()
cards = re.findall(r'<figure class="pfp-rv.*?</figure>', sec, re.S)
five = [c for c in cards if 'aria-label="5 out of 5 stars"' in c][0]
five = re.sub(r'--w:[0-9.]+%', '--w:100%', five)
# the corner mark becomes a real button, named by its own words, as course-page.js makes it (S523)
five = re.sub(r'<span class="pfp-rv__lab" aria-hidden="true">(.*?)</span>', r'<button type="button" class="pfp-rv__lab">\1</button>', five, count=1, flags=re.S)
five = five.replace('<button type="button" class="pfp-rv__lab"><svg viewBox="0 0 24 24">', '<button type="button" class="pfp-rv__lab"><svg viewBox="0 0 24 24" aria-hidden="true">')
ways = re.search(r'<ul class="rvb-ways">.*?</ul>', sec, re.S).group(0)
P = json.load(open('pool30.json'))
E = lambda s: html.escape(s, quote=False)
def card(x, held):
    c = five.replace('<figure class="pfp-rv"', '<figure class="pfp-rv%s"' % (' is-held' if held else ''), 1)
    c = re.sub(r'<blockquote data-fit="[^"]*">.*?</blockquote>', lambda m: '<p class="hpp-title">%s</p><blockquote data-fit="%s">%s</blockquote>' % (E(x['title']), html.escape(x['text']), E(x['text'])), c, flags=re.S)
    c = re.sub(r'(<span class="pfp-av__i">)[^<]*(</span>)', lambda m: m.group(1) + x['name'][0].upper() + m.group(2), c)
    c = re.sub(r'(<span class="pfp-rv__who">.*?<b>)[^<]*(</b>)', lambda m: m.group(1) + E(x['name']) + m.group(2), c, flags=re.S)
    c = re.sub(r'(<span class="pfp-rv__date">)[^<]*(</span>)', lambda m: m.group(1) + 'Verified student, ' + x['date'] + m.group(2), c)
    c = re.sub(r'(<span class="pfp-rv__course">)[^<]*(</span>)', lambda m: m.group(1) + E(x['course']) + m.group(2), c)
    return c
STAGES = [('start', 'Starting Out'), ('deeper', 'Going Deeper'), ('others', 'Helping Others Grow')]
cols = ''.join('<div class="hpp-col" data-hpp-stage="%s"><p class="hpp-tag"><span class="hpp-dot" aria-hidden="true"></span><span class="hpp-n">0%d</span> %s</p>%s</div>'
               % (k, i + 1, name, ''.join(card(x, n > 0) for n, x in enumerate(P[k]))) for i, (k, name) in enumerate(STAGES))
HEAD = ('<div class="pf-head pfp-head"><h2 class="d-title" id="home-proof-h">Voices From Every Stage <span class="pfp-tie">of the Road</span></h2>\n'
        '<p class="lead-bar d-sub">Real reviews from students at each stage, from a first course to using what they learned to help <span class="pfp-tie">other people.</span></p></div>')
block = ('<section class="d-block pf pf2 pfp rvb hpp hpp--1" id="home-proof" aria-labelledby="home-proof-h"><div class="d-inner">\n%s\n<div class="hpp-cols">%s</div>\n%s</div></section>'
         % (HEAD, cols, ways))
CSS = open('proof.css').read() + open('turn.css').read()
JS = open('turn.js').read()
page = open('site/previews/home-page-s558/home.html').read()
page = page.replace('</head>', '<style id="hpp-css">' + CSS + '</style></head>', 1)
i = page.find('<section class="r4'); j = page.find('</section>', i) + len('</section>')
k = page.find('<', j)
if page.startswith('<script', k): j = page.find('</script>', k) + len('</script>')
page = page[:j] + '\n' + block + '\n<script>' + JS + '</script>\n' + page[j:]
open('site/previews/home-page-s558/home-proof.html', 'w').write(page)
print('ok', page.count('class="pfp-rv'), 'cards')
