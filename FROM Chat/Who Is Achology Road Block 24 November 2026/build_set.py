import math
s=open('home/previews/home-page-s558/home.html').read()
D='#354149'; O='#ED6922'
arrow='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
H='Who Is<br class="r4__br"> <span class="policy-next__accent">Achology</span>?'
P1="Achology is an academy, a community and a movement of people learning to understand themselves and help others do the same."
P2="For a century, psychology's most useful ideas stayed inside universities and clinics. We take the ones you can learn from and use, and teach them in everyday words, so you can understand yourself, relate better to others and live a wiser, more responsible life."
HINGE='Nobody starts as an expert.<br class="r4__br2"> Everyone starts somewhere.'
ST=[("Starting Out","I want to understand why I feel and react the way I do.","Begin with free articles, workbooks and lessons that explain the ideas behind your thoughts, feelings and choices.","Start Learning for Free","/learn/"),
("Going Deeper","I&rsquo;ve worked on myself for years, and I want to go further.","Study at your own pace, then talk each idea through with other members of Achology at live events every week.","Explore the Academy","/academy/"),
("Helping Others Grow","I want to help the people who rely on me grow as well.","Whether you lead, mentor, parent or coach, train in the skills of helping and earn an independently verified certificate.","See How Certification Works","/certification/")]
def c(cx,cy,r,fill='#FBF9F6',sw=3): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{D}" stroke-width="{sw}"/>'
def pawn(x,y,sc,fill):
    return (f'<circle cx="{x:.1f}" cy="{y-3.6*sc:.1f}" r="{3.2*sc:.1f}" fill="{fill}"/>'
            f'<path d="M{x-6*sc:.1f} {y+7*sc:.1f} A{6*sc:.1f} {6.4*sc:.1f} 0 0 1 {x+6*sc:.1f} {y+7*sc:.1f} Z" fill="{fill}"/>')
def wave(i,n,scale,period):
    return f'<circle class="r4__wv" cx="48" cy="48" r="20" style="--s:{scale};--t:{period}s;--d:{-i*period/n:.2f}s"/>'
def marker(k):
    cx=cy=48; p=[]
    n,scale,period=[(1,1.7,3.6),(2,2.5,3.2),(3,3.6,3.0)][k]
    p.append('<g class="r4__waves">'+''.join(wave(i,n,scale,period) for i in range(n))+'</g>')
    p.append(f'<circle cx="48" cy="48" r="20" fill="{O}" fill-opacity=".16"/>')
    if k==2:
        for a in (-90,30,150):
            ca,sa=math.cos(math.radians(a)),math.sin(math.radians(a))
            p.append(pawn(cx+54*ca,cy+54*sa-1,1.55,D))
    p.append(pawn(cx,cy-1,2.1,O))
    return f'<svg class="r4__mk r4__mk--{k+1}" viewBox="0 0 96 96" overflow="visible" aria-hidden="true" focusable="false">{"".join(p)}</svg>'
def stage(k):
    t,th,tx,ln,href=ST[k]
    return (f'<li class="r4__st r4__st--{k+1}">{marker(k)}<h3 class="r4__t"><span class="r4__n">{k+1}</span>{t}</h3>'
            f'<p class="r4__th">&ldquo;{th}&rdquo;</p><p class="r4__tx">{tx}</p>'
            f'<a class="pw-hero__acc r4__go" href="{href}">{ln} {arrow}</a></li>')
mark='<img class="r4__mark" src="http://127.0.0.1:8558/images/achology-logo-mark.webp" alt="" aria-hidden="true">'
def block(v,ground='sand'):
    return (f'<section class="r4 r4--{v} r4--{ground}" aria-labelledby="h-{v}">{mark}'
      '<svg class="r4__road" aria-hidden="true" focusable="false"><path class="r4__guide"/><g class="r4__steps"></g></svg>'
      f'<div class="page-container r4__top"><h2 class="r4__h" id="h-{v}">{H}</h2><div class="r4__body">'
      f'<p class="r4__lead">{P1}</p><p class="r4__p">{P2}</p>'
      f'<a class="pw-hero__acc r4__go r4__about" href="/about/">Get to Know Achology {arrow}</a></div></div>'
      f'<div class="page-container r4__stage"><p class="r4__hinge">{HINGE}</p><ol class="r4__row">{"".join(stage(k) for k in range(3))}</ol></div></section>')
def tag(n,name,why,pick=False):
    return f'<div class="wb-tag"><div class="page-container"><b>Option {n}{" &middot; Chat&rsquo;s pick" if pick else ""}</b> &middot; {name} <span>{why}</span></div></div>'
css=open('road.css').read(); js=open('road.js').read()
i=s.find('<main'); i=s.find('>',i)+1; j=s.find('</main>')
inner=('<style>'+css+'</style>'+block('rise')+'<script>'+js+'</script>')
out=s[:i]+inner+s[j:]
out=out.replace('<title>','<title>Who Is Achology, the road (one block) | ',1)
open('home/previews/home-page-s558/who-road-set.html','w').write(out); print('built')
