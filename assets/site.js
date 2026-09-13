document.documentElement.classList.add('js');
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('#navigation');
toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.focus()}});
const search=document.querySelector('#publication-search');
if(search){const type=document.querySelector('#publication-type');const items=[...document.querySelectorAll('.publication')];function filter(){const q=search.value.trim().toLowerCase();let n=0;for(const item of items){const show=item.textContent.toLowerCase().includes(q)&&(!type.value||item.dataset.category===type.value);item.hidden=!show;if(show)n++}document.querySelector('#result-count').textContent=`${n} of ${items.length} selected outputs`;document.querySelector('#no-results').hidden=n!==0}search.addEventListener('input',filter);type.addEventListener('change',filter)}
