window.nfConsent=window.nfConsent||{necessary:true,analytics:false};
function nfLoadGA4(){
  if(!window.nfConsent.analytics) return;
  var s=document.createElement('script');
  s.async=true; s.src='https://www.googletagmanager.com/gtag/js?id=G-XXXX';
  document.head.appendChild(s);
  window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);} gtag('js',new Date());
  gtag('config','G-XXXX',{anonymize_ip:true,allow_google_signals:false});
}
function nfEventViewItem(n){ if(window.gtag) gtag('event','view_item',{item_name:n}); }
function nfEventBeginCheckout(t){ if(window.gtag) gtag('event','begin_checkout',{items:[{item_name:t}]}); }
function nfEventPurchase(t,v){ if(window.gtag) gtag('event','purchase',{value:v,currency:'GBP',items:[{item_name:t}]}); }
