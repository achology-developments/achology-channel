# The course finder's data: every product, from the theme's registry, DSRD 4 and DSRD 5, with Kain's agreed facets (Session 487).
import json, re
src = open('plan.py').read()
exec(src[:src.index('chips_subj')])   # COURSES, SCHOOLS, curl, ROUTE, DEPTH, SUBJ, ORDER_S, BANDS, price, LAB
def hrs(h): return float(h.rstrip('+'))
P = []
for n in sorted(COURSES):
    c = COURSES[n]
    depth = ['Practitioner', 'Master level'] if n == '001' else [DEPTH[n]]
    P.append(dict(id='c' + n, kind='Course', name=c['card'], url=curl(n), subjects=SUBJ[n], routes=[ROUTE[n]], depth=depth,
                  hours=hrs(c['hours']), hoursLabel=c['hours'] + ' hours', price=price[n], pays=5,
                  schools=[s[0] for s in SCHOOLS if n in s[5]], home=c['school'], students=int(c.get('students','0').replace(',','')) if isinstance(c.get('students'),str) else 0, img='/images/courses/course-%s-square-480.webp' % n))
BUNDLE = {'nlp': (1137, '162+'), 'cbp': (987, '121+'), 'lc': (1287, '150+'), 'pc': (1057, '145+'), 'miw': (987, '121+'), 'mh': (1027, '131+'), 'pgd': (1337, '183.5+')}
for s in SCHOOLS:
    members = s[5]
    subj = sorted({x for m in members for x in SUBJ[m]}, key=ORDER_S.index)
    P.append(dict(id='s' + s[0], kind='School bundle', name=s[2], url='/academy/%s/' % s[1], subjects=subj,
                  routes=sorted({ROUTE[m] for m in members}), depth=sorted({d for m in members for d in (['Practitioner', 'Master level'] if m == '001' else [DEPTH[m]])}),
                  hours=hrs(BUNDLE[s[0]][1]), hoursLabel=BUNDLE[s[0]][1] + ' hours, %d courses' % len(members), price=BUNDLE[s[0]][0], pays=6,
                  schools=[s[0]], home=s[0], img='/images/schools/hero-%s-240.webp' % s[0]))
allh = sum(hrs(c['hours']) for c in COURSES.values())
P.append(dict(id='pass', kind='The Whole Academy', name='The Achology Access All Areas Pass', url='/access-all-areas/', subjects=ORDER_S, routes=['Mental Wellness', 'Personal Development', 'Professional Certification'],
              depth=['Introductory', 'Practitioner', 'Master level'], hours=allh, hoursLabel='All 28 courses, 12 months of membership', price=2995, pays=12,
              schools=[s[0] for s in SCHOOLS], home=None, img='/images/schools/hero-pass-240.webp'))
P.append(dict(id='dimap-up', kind='Course and membership', name='The Diploma with 12 Months of Membership', url=curl('001'), subjects=SUBJ['001'], routes=['Professional Certification'],
              depth=['Practitioner', 'Master level'], hours=51, hoursLabel='51+ hours, 12 months of membership', price=399, pays=None,
              schools=[s[0] for s in SCHOOLS], home='nlp', img='/images/courses/course-001-square-480.webp'))
P.append(dict(id='memb-m', kind='Membership', name='Achology Membership, Monthly', url='/membership/', subjects=None, routes=None, depth=None, hours=None,
              hoursLabel='Live events every weekday, $34.50 a month after the first 30 days', price=7, monthly=7, pays=None, schools=None, home=None, img='/images/schools/hero-memb-240.webp'))
P.append(dict(id='memb-a', kind='Membership', name='Achology Membership, Annual', url='/membership/', subjects=None, routes=None, depth=None, hours=None,
              hoursLabel='12 months, with one free masterclass for life', price=345, pays=None, schools=None, home=None, img='/images/schools/hero-memb-240.webp'))
STARS = {'001': '4.78', '002': '4.58', '003': '4.62', '004': '4.81', '005': '4.77', '006': '4.48', '007': '4.58', '008': '4.78', '009': '4.69', '010': '4.58', '011': '4.87', '012': '4.91', '013': '4.74', '014': '4.79', '015': '4.73', '016': '4.46', '017': '4.67', '018': '4.77', '019': '4.69', '020': '4.58', '021': '4.49', '022': '4.79', '023': '4.67', '024': '4.58', '025': '4.48', '026': '4.79', '027': '4.71', '028': '4.55'}
BSTAR = {'nlp': ('4.68', '269,269'), 'cbp': ('4.63', '245,286'), 'lc': ('4.71', '201,167'), 'pc': ('4.77', '130,570'), 'miw': ('4.74', '172,937'), 'mh': ('4.75', '84,006'), 'pgd': ('4.68', '176,343')}
for p in P:
    if p['id'].startswith('c') and len(p['id']) == 4:
        p['stars'] = STARS[p['id'][1:]]; p['studentsLabel'] = COURSES[p['id'][1:]]['students']
    elif p['id'].startswith('s') and p['id'][1:] in BSTAR:
        p['stars'], p['studentsLabel'] = BSTAR[p['id'][1:]]
    elif p['id'] in ('pass', 'dimap-up'):
        p['stars'], p['studentsLabel'] = ('4.66', '695,578') if p['id'] == 'pass' else (STARS['001'], COURSES['001']['students'])
PL = json.load(open('plans.json'))
for p in P:
    if p['id'] in PL: p['plans'] = PL[p['id']]['plans']
# THE FORMULA (Kain, Session 487): line 1 what it is; line 2 the name; line 3 always stars | students | hours of
# on-demand teaching | membership included, leaving out only what does not apply.
for p in P:
    p.pop('inside', None)
    if p['kind'] == 'Course':
        p['line1'] = ' and '.join(p['depth']).replace('Master level', 'Master Level') + ' Course'
        p['hrs'] = COURSES[p['id'][1:]]['hours']; p['memb'] = '3 Months Membership'
    elif p['kind'] == 'School bundle':
        p['line1'] = 'School Bundle, %d Courses' % len([s for s in SCHOOLS if s[0] == p['id'][1:]][0][5])
        p['hrs'] = BUNDLE[p['id'][1:]][1]; p['memb'] = '12 Months Membership'
    elif p['id'] == 'pass':
        p['line1'] = 'Full Academy Curriculum'; p['badge'] = True; p['hrs'] = '600+'; p['memb'] = '12 Months Membership'
    elif p['id'] == 'dimap-up':
        p['line1'] = 'Course and Membership'; p['hrs'] = '51+'; p['memb'] = '12 Months Membership'
    elif p['id'] == 'memb-m':
        p['line1'] = 'Membership'; p['live'] = 'Live Events Every Weekday'; p['memb'] = 'Cancel Anytime'
    elif p['id'] == 'memb-a':
        p['line1'] = 'Membership'; p['live'] = 'Live Events Every Weekday'; p['memb'] = 'One Free Masterclass for Life'
    if p['id'] == 'pass': p['name'] = 'The Achology Access All Areas Pass'
FACETS = dict(
    subject=dict(label='Subject', any='Any subject', opts=ORDER_S, multi=True),
    route=dict(label='What You Want', any='Anything', opts=['Mental Wellness', 'Personal Development', 'Professional Certification'], multi=True),
    depth=dict(label='Depth', any='Any depth', opts=['Introductory', 'Practitioner', 'Master level'], multi=True),
    time=dict(label='Time', any='Any length', opts=[b[1] for b in BANDS] + ['50 Hours Plus'], multi=False, lims=[b[0] for b in BANDS] + [9999]),
    price=dict(label='Price', any='Any price', opts=['Under $100', 'Under $250', 'Under $500', 'Under $1000', 'Under $1,500', 'Up to $2,995'], multi=False, lims=[100, 250, 500, 1000, 1500, 2995]),
    school=dict(label='School', any='Any school', opts=[s[2] for s in SCHOOLS], keys=[s[0] for s in SCHOOLS], multi=True),
)
DATA = dict(products=P, facets=FACETS)
open('finder-data.js', 'w').write('window.FINDER=' + json.dumps(DATA) + ';')
print(len(P), 'products')
