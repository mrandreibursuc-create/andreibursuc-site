const button=document.querySelector('.menu-button');
const nav=document.querySelector('.navlinks');
if(button&&nav){button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')!=='true';button.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open)});nav.addEventListener('click',e=>{if(e.target.closest('a')){button.setAttribute('aria-expanded','false');nav.classList.remove('is-open')}})}
function openLinkedQuestion(){if(location.hash){const item=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(item?.tagName==='DETAILS'){item.open=true;item.scrollIntoView({block:'start'});}}}
openLinkedQuestion();window.addEventListener('hashchange',openLinkedQuestion);
