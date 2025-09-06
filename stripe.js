(function(){
  document.addEventListener('click',function(e){
    const a=e.target.closest('a[data-tier]');
    if(!a) return; if(typeof nfEventBeginCheckout==='function') nfEventBeginCheckout(a.dataset.tier);
  });
})();