(function(){
  const KEY='nf_consent_v1';
  const prior=localStorage.getItem(KEY);
  window.nfConsent=prior?JSON.parse(prior):{necessary:true,analytics:false};
  function save(){localStorage.setItem(KEY,JSON.stringify(window.nfConsent));}
  function hide(){const b=document.getElementById('cookie-banner'); if(b) b.style.display='none';}
  function show(){const b=document.getElementById('cookie-banner'); if(b) b.style.display='block';}
  window.nfConsentShow=show;
  document.addEventListener('DOMContentLoaded',function(){
    if(!prior) show(); else { if(typeof nfLoadGA4==='function') nfLoadGA4(); }
    document.getElementById('btn-accept')?.addEventListener('click',()=>{window.nfConsent.analytics=true; save(); hide(); if(typeof nfLoadGA4==='function') nfLoadGA4();});
    document.getElementById('btn-reject')?.addEventListener('click',()=>{window.nfConsent.analytics=false; save(); hide();});
    document.getElementById('btn-customise')?.addEventListener('click',()=>{window.nfConsent.analytics=!window.nfConsent.analytics; save(); alert('Analytics '+(window.nfConsent.analytics?'enabled':'disabled')); if(window.nfConsent.analytics && typeof nfLoadGA4==='function') nfLoadGA4();});
  });
})();