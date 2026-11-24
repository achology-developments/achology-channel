(function(){
	var sec=document.getElementById('home-kh'); if(!sec) return;
	var row=sec.querySelector('.hk-row'), p=sec.querySelector('.hk-prev'), n=sec.querySelector('.hk-next');
	function ends(){}
	function step(d){
		var it=row.querySelector('.hc-item:not([hidden])'); var w=(it?it.getBoundingClientRect().width:258)+24;
		var max=row.scrollWidth-row.clientWidth;
		if(d>0 && row.scrollLeft>=max-4){ row.scrollTo({left:0,behavior:'smooth'}); return; }   /* the belt runs round: past the last, back to the first */
		if(d<0 && row.scrollLeft<=4){ row.scrollTo({left:max,behavior:'smooth'}); return; }
		row.scrollBy({left:d*w,behavior:'smooth'});
	}
	if(p) p.addEventListener('click',function(){step(-1);}); if(n) n.addEventListener('click',function(){step(1);});
	row.addEventListener('scroll',function(){ clearTimeout(row._t); row._t=setTimeout(ends,80); });
	sec.querySelectorAll('.hk-tab').forEach(function(b){ b.addEventListener('click',function(){
		var k=b.dataset.k;
		sec.querySelectorAll('.hk-tab').forEach(function(x){ var on=x===b; x.classList.toggle('is-on',on); x.classList.toggle('bf-framed',on); x.setAttribute('aria-pressed',on?'true':'false'); });
		row.querySelectorAll('.hc-item').forEach(function(it){ var kk=it.dataset.kind==='book-note'?'book':it.dataset.kind; it.hidden=!(k==='all'||kk===k); });
		row.scrollLeft=0; ends();
	});});
	setTimeout(ends,300);
})();
