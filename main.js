(function(){
  const form=document.querySelector('#lead-form');
  if(form){
    form.addEventListener('submit',e=>{
      e.preventDefault();
      const email=form.querySelector('input[type=email]').value.trim();
      const name=form.querySelector('input[name=name]')?.value.trim()||'';
      if(!email){alert('Enter a valid email.');return;}
      localStorage.setItem('nf_lead', JSON.stringify({email,name,ts:Date.now()}));
      const msg=document.getElementById('lead-msg');
      if(msg){msg.textContent='Thanks. Check your inbox for the whitepaper.'}
      if(window.nfEventViewItem){nfEventViewItem('lead_submit');}
    });
  }
})();