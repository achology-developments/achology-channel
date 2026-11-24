import re
php=open('courses-setup.php').read()
rows=re.findall(r"array\( '(\d{3})', '(\w+)', '([a-z\-]+)', ([\"'])(.+?)\4, (null|([\"'])(.+?)\7), '([\d,]+)', '([\d.+]+)', '\$(\d+)'",php)
COURSES={}
for r in rows:
    n,sch,slug,_,name,_,_,card,stud,hours,price=r
    COURSES[n]=dict(n=n,school=sch,slug=slug,name=name,card=card or name,hours=hours,students=stud)
assert len(COURSES)==28,len(COURSES)
SCHOOLS=[
 ('nlp','neuro-linguistic-programming','The School of Neuro-Linguistic Programming (NLP)','Neuro-Linguistic Programming','nlp',['001','002','003','004','005']),
 ('cbp','cognitive-behavioural-psychology','The School of Cognitive Behavioural Psychology (CBP)','Cognitive Behavioural Psychology','cbp',['001','006','007','008','023']),
 ('lc','life-coaching','The School of Life Coaching and Professional Helping','Life Coaching and Professional Helping','life-coaching',['001','009','010','011','012','022']),
 ('pc','person-centred-counselling','The School of Person-Centred Counselling and Psychology','Person-Centred Counselling and Psychology','person-centred',['001','011','013','014','024']),
 ('miw','mindfulness','The School of Mindfulness, Applied Insight and Wisdom (MIW)','Mindfulness, Applied Insight and Wisdom','mindfulness',['001','015','016','017','022']),
 ('mh','mental-health','The School of Mental Health, Wellness and Emotional Resilience','Mental Health, Wellness and Emotional Resilience','mental-health',['001','005','008','016','018']),
 ('pgd','personal-growth','The School of Personal Growth and Development (PGD)','Personal Growth and Development','personal-growth',['001','017','019','020','021','022','023','024','025','026','027','028']),
]
assert [len(s[5]) for s in SCHOOLS]==[5,5,6,5,5,5,12]
SLUG={s[0]:s[1] for s in SCHOOLS}
def curl(n):
    c=COURSES[n]; return '/academy/%s/%s/'%(SLUG[c['school']],c['slug'])
