const button=document.querySelector('.menu-button');
const nav=document.querySelector('.navlinks');
if(button&&nav){button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')!=='true';button.setAttribute('aria-expanded',String(open));nav.classList.toggle('is-open',open)});nav.addEventListener('click',e=>{if(e.target.closest('a')){button.setAttribute('aria-expanded','false');nav.classList.remove('is-open')}})}
function openLinkedQuestion(){if(location.hash){const item=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(item?.tagName==='DETAILS'){item.open=true;item.scrollIntoView({block:'start'});}}}
openLinkedQuestion();window.addEventListener('hashchange',openLinkedQuestion);

// Google Analytics 4: website visits (production domain only).
(() => {
  if (!['andreibursuc.com', 'www.andreibursuc.com'].includes(location.hostname)) return;
  if (window.__andreiAnalyticsLoaded) return;
  window.__andreiAnalyticsLoaded = true;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', 'G-E4E465K05F', {
    allow_google_signals: false,
    allow_ad_personalization_signals: false
  });
  const tag = document.createElement('script');
  tag.async = true;
  tag.src = 'https://www.googletagmanager.com/gtag/js?id=G-E4E465K05F';
  document.head.appendChild(tag);
})();
