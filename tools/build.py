from pathlib import Path
import json,html,re
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'content.json').read_text())
esc=html.escape
nav=[('index.html','Home'),('research.html','Research'),('publications.html','Publications'),('teaching.html','Teaching & Supervision'),('news.html','Talks & News'),('about.html','About / CV')]
profiles={'Google Scholar':'https://scholar.google.co.in/citations?user=yuB4f7IAAAAJ&hl=en','ORCID':'https://orcid.org/0000-0002-8360-5309','LinkedIn':'https://www.linkedin.com/in/soumen-ghosh-aaa58ba4/','GitHub':'https://github.com/soumenca'}
def link(label,url,cls=''):
 return f'<a class="{cls}" href="{esc(url,quote=True)}">{esc(label)}</a>'
def blocks(bs):
 out=''
 for b in bs:
  t=b['text'].replace('Academic engagement in research and teaching.','Appointed September 2026.').replace('AES HDR travel award (2023)','UQ HDR travel support to attend AES (2023)')
  if t.startswith('Google Scholar'):continue
  if t.startswith('For a current academic CV,'):t='Download my selected academic CV below. For collaboration enquiries or supervision discussions, contact soumen.ghosh@uq.edu.au.'
  tag=b['tag']
  if tag=='ul':out+='<ul>'+''.join('<li>'+esc(s)+'</li>' for s in t.splitlines() if s.strip())+'</ul>';continue
  ls=t.splitlines();txt='<br>'.join(('<strong>'+esc(s)+'</strong>') if i==0 and len(ls)>1 else esc(s) for i,s in enumerate(ls))
  txt=txt.replace('soumen.ghosh@uq.edu.au',link('soumen.ghosh@uq.edu.au','mailto:soumen.ghosh@uq.edu.au'))
  out+=f'<{tag}>{txt}</{tag}>\n'
 return out

def page(name,title,desc,body,home=False):
 navigation=''.join(f'<a href="{f}"'+(' aria-current="page"' if f==name else '')+f'>{label}</a>' for f,label in nav)
 profile=''.join(link(k,v) for k,v in profiles.items())
 fulltitle='Soumen Ghosh | Medical Imaging AI' if home else title+' | Soumen Ghosh'
 doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{fulltitle}</title><meta name="description" content="{esc(desc,quote=True)}"><meta name="theme-color" content="#123c43"><meta property="og:title" content="{fulltitle}"><meta property="og:description" content="{esc(desc,quote=True)}"><meta property="og:type" content="website"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/site.css"><script src="assets/site.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="nav-wrap"><a class="wordmark" href="index.html">Soumen Ghosh<span>Researcher · Brisbane</span></a><button class="menu-toggle" aria-expanded="false" aria-controls="navigation">Menu <span aria-hidden="true">☰</span></button><nav id="navigation" aria-label="Main navigation">{navigation}</nav></div></header><main id="main">{body}</main><footer><div class="footer-inner"><div><a class="wordmark" href="index.html">Soumen Ghosh, PhD</a><p>Medical Imaging AI &amp; Quantitative Imaging</p><a href="mailto:soumen.ghosh@uq.edu.au">soumen.ghosh@uq.edu.au</a></div><div class="footer-links">{profile}<a href="assets/Soumen_Ghosh_CV.pdf">Academic CV (PDF)</a></div></div><div class="footer-bottom">Brisbane, Australia<span>Updated September 2026</span></div></footer></body></html>'''
 (root/name).write_text(doc)

def heading(kicker,title,intro=''):
 return f'<div class="page-heading"><p class="eyebrow">{kicker}</p><h1>{title}</h1>'+ (f'<p class="lede">{intro}</p>' if intro else '')+'</div>'
research_cards=[('01','Neuroimaging & neurological disease','Structural and diffusion MRI, epilepsy lesion detection and imaging biomarkers of neurodegeneration.'),('02','Occupational lung disease & thoracic imaging','Quantitative CT and the relationship between lung structure, disease and pulmonary function.'),('03','Clinical AI evaluation & translation','Robust validation, multi-site data and reproducible methods that support clinical interpretation.')]
cards=''.join(f'<a class="theme-card" href="research.html#theme-{i}"><span class="number">{n}</span><h3>{esc(t)}</h3><p>{esc(d)}</p><span class="card-link">Explore theme <span aria-hidden="true">↗</span></span></a>' for i,(n,t,d) in enumerate(research_cards,1))
home=f'''<section class="hero"><div class="hero-copy"><p class="eyebrow">Soumen Ghosh, PhD</p><h1>Medical Imaging AI<br><span>&amp; Quantitative Imaging</span></h1><p class="lede">I develop and evaluate imaging AI and quantitative biomarkers for neurological and occupational lung disease.</p><div class="button-row">{link('Explore my research','research.html','button primary')}{link('Download CV (PDF)','assets/Soumen_Ghosh_CV.pdf','button secondary')}</div></div><aside class="profile"><img src="https://avatars.githubusercontent.com/u/30767731?v=4" width="240" height="240" alt="Soumen Ghosh" fetchpriority="high"><p>Brisbane, Australia</p><a href="mailto:soumen.ghosh@uq.edu.au">Get in touch ↗</a></aside></section><section class="affiliations" aria-label="Current appointments"><div><span>Senior Researcher</span><strong>I-MED Radiology Network</strong></div><div><span>Honorary Fellow</span><strong>The University of Queensland</strong></div><div><span>Adjunct Lecturer</span><strong>Charles Darwin University</strong></div></section><section class="section"><div class="section-top"><div><p class="eyebrow">Research focus</p><h2>From imaging methods to clinical evidence.</h2></div></div><div class="theme-grid">{cards}</div></section><section class="section split"><div><p class="eyebrow">Latest updates</p><h2>Research &amp; academic news</h2><a class="text-link" href="news.html">All talks &amp; news ↗</a></div><div class="news-list"><article><time>September 2026</time><h3>Adjunct Lecturer appointment at CDU</h3><p>I have joined Charles Darwin University as an Adjunct Lecturer.</p></article><article><time>September 2026</time><h3>CRIL-U-Net accepted at MICAD 2026</h3><p>Compact ratio-interaction learning for focal cortical dysplasia segmentation from T1w and FLAIR MRI.</p><a href="publications.html">View publication details ↗</a></article></div></section><section class="collaboration"><p class="eyebrow">Work with me</p><h2>Clinical questions. Collaborative research.</h2><p>I welcome collaborations with clinicians, imaging scientists and AI researchers, and enquiries about student research in medical imaging AI.</p><div class="button-row">{link('Contact me','mailto:soumen.ghosh@uq.edu.au','button primary')}{link('Teaching & supervision','teaching.html','button secondary')}</div></section>'''
page('index.html','Home','Soumen Ghosh: medical imaging AI and quantitative imaging researcher at I-MED, with academic appointments at UQ and CDU.',home,True)
rs=data['research'];intro=rs[0]['text'];content='';idx=0
for b in rs[1:]:
 if b['tag']=='h2':idx+=1;content+=f'<h2 id="theme-{idx}">{esc(b["text"])}</h2>'
 else:content+=blocks([b])
page('research.html','Research','Neuroimaging, occupational lung disease and clinical AI evaluation.',heading('Research','Imaging methods.<br>Clinical questions.',esc(intro))+'<div class="reading-layout"><aside class="section-nav" aria-label="Research themes">'+''.join(f'<a href="#theme-{i}">{esc(t)}</a>' for i,(_,t,_) in enumerate(research_cards,1))+'</aside><div class="prose">'+content+'</div></div>')
# Bibliographic links remain attached to the corresponding paper, including repeated labels.
refs={2:('Preprint','https://arxiv.org/abs/2608.03185'),3:('Read on arXiv','https://arxiv.org/abs/2607.15605'),4:('Read on arXiv','https://arxiv.org/abs/2404.10290'),6:('Read article','https://doi.org/10.3389/fneur.2024.1383773'),7:('Read article','https://doi.org/10.1186/s13550-024-01100-x'),9:('arXiv version','https://arxiv.org/abs/2508.18612'),10:('Publisher','https://doi.org/10.1109/ICARCV.2018.8581147'),11:('Publisher','https://doi.org/10.1007/978-3-319-69900-4_32'),12:('Publisher','https://doi.org/10.1007/978-3-319-49397-8_4')}
category='';pubs='';count=0
for i,b in enumerate(data['publications']):
 if b['tag']=='h2':category=b['text'];continue
 if i==0:continue
 ls=b['text'].splitlines();title=ls[0];details=ls[1:]
 if i in refs:
  label,url=refs[i];details=[s.replace(label+'.','').strip() for s in details];source=link(label+' ↗',url,'text-link')
 else:source=''
 pubs+=f'<article class="publication" data-category="{esc(category,quote=True)}"><p class="pub-type">{esc(category)}</p><h2>{esc(title)}</h2>'+''.join('<p>'+esc(s)+'</p>' for s in details if s)+source+'</article>';count+=1
cats=['Recent papers & preprints','Journal articles','Published conference papers','Selected conference abstracts']
filters='<div class="filters"><label>Search publications<input id="publication-search" type="search" placeholder="Title, author or year…"></label><label>Publication type<select id="publication-type"><option value="">All outputs</option>'+''.join(f'<option>{esc(c)}</option>' for c in cats)+'</select></label></div>'
page('publications.html','Publications','Selected papers, preprints and conference abstracts, with authors and source links.',heading('Publications','Research outputs.','Selected publications in medical imaging and machine learning. Browse the broader record on '+link('Google Scholar',profiles['Google Scholar'])+'.')+filters+f'<p id="result-count" role="status">{count} selected outputs</p><div class="publications">'+pubs+'</div><p id="no-results" hidden>No matching publications. Try another title, author or year.</p>')
page('teaching.html','Teaching & Supervision','Teaching experience and research supervision in medical imaging AI.',heading('Teaching & supervision','Learning through research.')+'<div class="prose standalone">'+blocks(data['teaching'])+'</div>')
page('news.html','Talks & News','Academic appointments, research updates, invited talks and conference contributions.',heading('Talks & news','Sharing research.<br>Connecting ideas.')+'<div class="prose standalone news-prose">'+blocks(data['talks'])+'</div>')
page('about.html','About / CV','Biography, academic appointments, education and downloadable CV for Soumen Ghosh.',heading('About / CV','Soumen Ghosh, PhD.','Medical imaging AI researcher based in Brisbane, Australia.')+'<div class="cv-banner"><div><strong>Selected academic CV</strong><p>Appointments, education, teaching and selected research outputs · September 2026</p></div>'+link('Download PDF','assets/Soumen_Ghosh_CV.pdf','button primary')+'</div><div class="prose standalone">'+blocks(data['about'])+'</div>')
print('Built six static pages')
