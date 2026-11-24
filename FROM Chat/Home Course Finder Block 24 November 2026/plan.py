import re, html
from collections import Counter
exec(open('data.py').read())
E = lambda s: html.escape(s)
price = {r[0]: int(r[1]) for r in re.findall(r"array\( '(\d{3})'.*?'\$(\d+)'", open('courses-setup.php').read())}
ROUTE = {}
for n in ['005','006','008','016','018','019','020','021','026']: ROUTE[n] = 'Mental Wellness'
for n in ['002','010','011','017','022','023','024','025','027','028']: ROUTE[n] = 'Personal Development'
for n in ['001','003','004','007','009','012','013','014','015']: ROUTE[n] = 'Professional Certification'
DEPTH = {}
for n in ['002','005','006','008','011','016','017','019','020','021','022','023','024','025','026','027','028']: DEPTH[n] = 'Introductory'
for n in ['001','003','007','009','010','013','014','015','018']: DEPTH[n] = 'Practitioner'
for n in ['004','012']: DEPTH[n] = 'Master level'
DEPTH['001'] = 'Practitioner and Master level'  # Kain, Session 487: DiMAP in Master level too
SUBJ = {
 '001': ['Applied Psychology', 'Personal Growth', 'Professional Helping'],
 '002': ['Neuro-Linguistic Programming', 'Personal Growth'],
 '003': ['Neuro-Linguistic Programming', 'Professional Helping'],
 '004': ['Neuro-Linguistic Programming', 'Professional Helping'],
 '005': ['Neuro-Linguistic Programming', 'Personal Growth', 'Mental Health'],
 '006': ['Cognitive Behavioural Therapy', 'Cognitive Behavioural Psychology'],
 '007': ['Cognitive Behavioural Therapy', 'Cognitive Behavioural Psychology', 'Professional Helping'],
 '008': ['Cognitive Behavioural Therapy', 'Cognitive Behavioural Psychology', 'Mental Health'],
 '009': ['Life Coaching', 'Professional Helping'],
 '010': ['Life Coaching', 'Professional Helping'],
 '011': ['Professional Helping', 'Person-Centred Counselling'],
 '012': ['Professional Helping', 'Life Coaching'],
 '013': ['Hypnotherapy', 'Professional Helping'],
 '014': ['Person-Centred Counselling', 'Person-Centred Psychology', 'Professional Helping'],
 '015': ['Mindfulness', 'Professional Helping'],
 '016': ['Mindfulness', 'Mental Health', 'Personal Growth'],
 '017': ['Mindfulness', 'Leadership and Management'],
 '018': ['Mental Health', 'Emotional Resilience', 'Professional Helping'],
 '019': ['Confidence and Self-Esteem', 'Emotional Intelligence'],
 '020': ['Confidence and Self-Esteem', 'Personal Growth'],
 '021': ['Emotional Intelligence', 'Communication and Social Skills'],
 '022': ['Personal Growth', 'Goals and Productivity'],
 '023': ['Goals and Productivity'],
 '024': ['Communication and Social Skills'],
 '025': ['Goals and Productivity'],
 '026': ['Emotional Resilience', 'Mental Health'],
 '027': ['Relationships'],
 '028': ['Business'],
}
ORDER_S = ['Neuro-Linguistic Programming', 'Cognitive Behavioural Psychology', 'Cognitive Behavioural Therapy', 'Life Coaching', 'Professional Helping', 'Person-Centred Counselling',
           'Person-Centred Psychology', 'Hypnotherapy', 'Mindfulness', 'Mental Health', 'Emotional Resilience', 'Personal Growth',
           'Applied Psychology', 'Confidence and Self-Esteem', 'Emotional Intelligence', 'Communication and Social Skills',
           'Goals and Productivity', 'Leadership and Management', 'Relationships', 'Business']
assert len(ROUTE) == len(DEPTH) == len(SUBJ) == 28
cnt = Counter(s for v in SUBJ.values() for s in v)
assert set(cnt) == set(ORDER_S), set(cnt) ^ set(ORDER_S)
KAIN = set(ORDER_S[:12])
BANDS = [(10,'Up to 10 Hours'),(15,'Up to 15 Hours'),(20,'Up to 20 Hours'),(25,'Up to 25 Hours'),(30,'Up to 30 Hours'),(40,'Up to 40 Hours'),(50,'Up to 50 Hours')]
def band(h):
    v = float(h.rstrip('+'))
    for lim, lab in BANDS:
        if v <= lim: return lab
    return '50 Hours Plus'
LAB = {s[0]: s[3] for s in SCHOOLS}
chips_subj = ''.join('<span%s>%s <i>%d</i></span>' % ('' if s in KAIN else ' class="new"', E(s), cnt[s]) for s in ORDER_S)
rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><b>%s</b></td><td>%s hours, %s</td><td>$%d</td><td>%s</td></tr>' % (
    n, E(COURSES[n]['card']), E(', '.join(SUBJ[n])), ROUTE[n], DEPTH[n], COURSES[n]['hours'], band(COURSES[n]['hours']), price[n], E(LAB[COURSES[n]['school']]))
    for n in sorted(COURSES))
page = '''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Home Course Finder Plan</title>
<style>
body{margin:0;background:#faf8f5;color:#354149;font:17px/1.6 -apple-system,system-ui,sans-serif}
main{max-width:900px;margin:0 auto;padding:56px 28px 96px}
h1{font-size:34px;line-height:1.2;margin:0 0 8px}h2{font-size:22px;margin:48px 0 8px}
.sub{color:#5E6B75;margin:0 0 32px}
.box{background:#fff;border:1px solid #eceae6;border-radius:14px;padding:22px 26px;margin:16px 0}
.box h3{margin:0 0 6px;font-size:18px}.box p{margin:6px 0}
.chips span{display:inline-block;margin:4px 6px 4px 0;padding:6px 12px;border-radius:999px;background:#f3f1ee;font-size:15px}
.chips span i{font-style:normal;color:#8A9199;font-size:13px;margin-left:4px}
.chips span.new{background:#fff;box-shadow:inset 0 0 0 1px #ED6922}
.mine{border-left:4px solid #ED6922}.tag{display:inline-block;font-size:13px;font-weight:600;color:#B8460F;margin-bottom:4px}
.key{font-size:14px;color:#5E6B75}
table{width:100%;border-collapse:collapse;font-size:13.5px;background:#fff}
th,td{text-align:left;padding:9px 8px;border-bottom:1px solid #eeeded;vertical-align:top}th{background:#f3f1ee;font-size:13px}
.ask{background:#354149;color:#fff;border-radius:14px;padding:22px 26px;margin:40px 0 0}.ask p{margin:6px 0}
</style></head><body><main>
<h1>The Course Finder on the Home Page</h1>
<p class="sub">Block 3. Plain words first, no design yet. Every price is from DSRD 4. Your subjects, full names, Session 487, 24 November 2026.</p>

<h2>What it does</h2>
<p>A visitor presses as many or as few buttons as they like, in any order. The block shows every Achology product that fits, right there, with a count. All roads lead to the right course: if nothing fits exactly, it shows the nearest ones and says so. It never shows an empty result.</p>
<p>It is the place the hero's button, "Find the Right Course for You", leads to.</p>

<h2>The choices, all optional</h2>
<div class="box mine"><span class="tag">Your list, plus eight I found in the course titles</span><h3>1. Which subject?</h3>
<p>What the person wants to learn. Each course carries every subject it covers, so one course can show under several. The number is how many courses each subject brings up.</p>
<p class="chips">''' + chips_subj + '''</p>
<p class="key">Grey: your twelve. Orange outline: the eight I added from the course titles, yours to keep or cut.</p></div>
<div class="box"><h3>2. What do you want from it?</h3>
<p>Your own three routes, in your words from the Pricing page (DSRD 4 section 2).</p>
<p class="chips"><span>Mental Wellness</span><span>Personal Development</span><span>Professional Certification</span></p></div>
<div class="box"><h3>3. How deep?</h3>
<p>No record gives a level for each course, and every course page says a beginner can start today. Sorted from each course's name, then checked by Kain: 17 introductory, 9 practitioner, 3 master level. The Diploma sits in both practitioner and master level (Kain, Session 487).</p>
<p class="chips"><span>Introductory</span><span>Practitioner</span><span>Master level</span></p></div>
<div class="box"><h3>4. How much time?</h3>
<p>Kain's eight, word for word, from each course's hours in DSRD 5. Each band shows every course up to that length.</p>
<p class="chips"><span>Up to 10 Hours</span><span>Up to 15 Hours</span><span>Up to 20 Hours</span><span>Up to 25 Hours</span><span>Up to 30 Hours</span><span>Up to 40 Hours</span><span>Up to 50 Hours</span><span>50 Hours Plus</span></p>
<ul><li><b>Up to 10 Hours</b>: 4 courses</li><li><b>Up to 15 Hours</b>: 15</li><li><b>Up to 20 Hours</b>: 18</li><li><b>Up to 25 Hours</b>: 18 (no course is between 20 and 25 hours)</li><li><b>Up to 30 Hours</b>: 19</li><li><b>Up to 40 Hours</b>: 24</li><li><b>Up to 50 Hours</b>: 27</li><li><b>50 Hours Plus</b>: 1, the Diploma</li></ul></div>
<div class="box"><h3>5. What would you like to pay?</h3>
<p>In full, or per month. Per month uses each product's own instalments, so "$30 a month" shows everything whose monthly payment is $30 or less, with the number of payments beside it and the full price shown too.</p>
<p class="chips"><span>Under $100</span><span>Under $250</span><span>Under $500</span><span>Under $1000</span><span>Under $1,500</span><span>Up to $2,995</span><span>Up to $__ a Month</span></p>
<p>Kain's seven, word for word. What each one adds:</p>
<ul><li><b>Under $100</b>: the nine masterclasses, and the $7 membership start</li>
<li><b>Under $250</b>: the $149, $199 and $249 courses</li>
<li><b>Under $500</b>: the $299 courses, annual membership ($345), the DiMAP upgrade ($399)</li>
<li><b>Under $1000</b>: two school bundles ($987)</li>
<li><b>Under $1,500</b>: the other five school bundles ($1,027 to $1,337)</li>
<li><b>Up to $2,995</b>: the Access All Areas Pass</li></ul>
<p>Per month, the pass comes up for anyone ready to pay about $250 a month: 12 payments of $249.58, read from its checkout. At $500 a month it shows as 6 payments of $499.17, and at $1,000 as 3 of $998.33.</p></div>
<div class="box"><h3>6. Which school?</h3>
<p>For people who think in schools, as at a university. The seven schools, by their full names.</p>
<p class="chips">''' + ''.join('<span>%s</span>' % E(s[2]) for s in SCHOOLS) + '''</p></div>

<h2>Everything it can show</h2>
<div class="box"><p><b>28 courses</b>, $97 to $299. Each: 3 or 5 monthly payments, no interest. Each comes with 3 months of membership.</p>
<p><b>7 school bundles</b>, $987 to $1,337, each with 12 months of membership. Each: 2, 4 or 6 monthly payments.</p>
<p><b>The Access All Areas Pass</b>, $2,995: all 28 courses and 12 months of membership. Or 3, 6 or 12 monthly payments, such as 12 x $249.58.</p>
<p><b>Achology Membership, monthly</b>: $7 for the first 30 days, then $34.50 a month.</p>
<p><b>Achology Membership, annual</b>: $345 a year, with one free masterclass for life.</p>
<p><b>The DiMAP upgrade</b>: the Diploma with 12 months of membership, $399.</p></div>
<p>Each result shows its name, how deep and how long it is, the full price, the monthly option, and one link to its own page.</p>

<h2>One thing Code must do first</h2>
<div class="box"><p>The monthly amounts must be read from each product's own checkout, never worked out (DSRD 4 section 1.1). Code has read four so far. The finder needs all 37: 28 courses, 7 bundles, the pass and the upgrade.</p></div>

<h2>The 28 courses and their subjects</h2>
<table><tr><th>No.</th><th>Course</th><th>Subjects (mine)</th><th>Route</th><th>Depth (mine)</th><th>Length</th><th>Price</th><th>School</th></tr>''' + rows + '''</table>

<div class="ask"><p><b>For you to check:</b> the subject list, and each course's subjects in the table.</p><p>Once the words are right, I show you four rendered designs of the block.</p></div>
</main></body></html>'''
assert not re.search(r'(?i)\bhold', page) and '–' not in page and '—' not in page
open('site/previews/course-finder-plan.html', 'w').write(page)
open("/Users/kainramsay/Documents/CLAUDE | Anthropic Ai/Claude Code (Projects)/0001. Achology Website Upgrade 2026/02. Project Delivery System/Home Course Finder Plan 24 November 2026.html", 'w').write(page)
print('ok', dict(cnt))
