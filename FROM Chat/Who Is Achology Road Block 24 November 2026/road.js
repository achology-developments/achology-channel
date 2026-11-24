(function(){
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function curve(pts){var d='M'+pts[0].x+' '+pts[0].y;for(var i=1;i<pts.length;i++){var a=pts[i-1],b=pts[i];if(Math.abs(b.x-a.x)>=Math.abs(b.y-a.y)){var h=(b.x-a.x)/2;d+=' C'+(a.x+h)+' '+a.y+' '+(b.x-h)+' '+b.y+' '+b.x+' '+b.y;}else{var v=(b.y-a.y)/2;d+=' C'+a.x+' '+(a.y+v)+' '+b.x+' '+(b.y-v)+' '+b.x+' '+b.y;}}return d;}
function build(sec){var sr=sec.getBoundingClientRect();var c=[].map.call(sec.querySelectorAll('.r4__mk'),function(m){var r=m.getBoundingClientRect();return {x:r.left-sr.left+r.width/2,y:r.top-sr.top+r.height/2};});
var w=sec.clientWidth,h=sec.clientHeight,svg=sec.querySelector('.r4__road');var vertical=Math.abs(c[1].x-c[0].x)<20;var pts;
if(vertical){var st=sec.querySelector('.r4__row').getBoundingClientRect();pts=[{x:c[0].x,y:st.top-sr.top-24}].concat(c).concat([{x:c[2].x,y:h}]);}
else{var lift=Math.max(c[0].y-c[2].y,0);var y0=c[0].y+(lift?lift*0.6:0),y1=c[2].y-(lift?lift*0.6:0);pts=[{x:0,y:y0}].concat(c).concat([{x:w,y:Math.max(y1,24)}]);}
var d=curve(pts);svg.setAttribute('viewBox','0 0 '+w+' '+h);var g=svg.querySelector('.r4__guide');g.setAttribute('d',d);var L=g.getTotalLength();
var stops=c.map(function(p){var best=0,bd=1e9;for(var s=0;s<=L;s+=4){var q=g.getPointAtLength(s);var dd=(q.x-p.x)*(q.x-p.x)+(q.y-p.y)*(q.y-p.y);if(dd<bd){bd=dd;best=s;}}return best;});
var grp=svg.querySelector('.r4__steps');grp.innerHTML='';var NS='http://www.w3.org/2000/svg';var steps=[];var STEP=vertical?20:24,SIDE=4.5;var k=0;
for(var s=STEP/2;s<L-2;s+=STEP){var near=stops.some(function(t,i){return Math.abs(t-s)<[30,46,70][i];});if(near)continue;var p=g.getPointAtLength(s),q=g.getPointAtLength(Math.min(L,s+1));var ang=Math.atan2(q.y-p.y,q.x-p.x);var side=(k++%2)?SIDE:-SIDE;var x=p.x-Math.sin(ang)*side,y=p.y+Math.cos(ang)*side;var e=document.createElementNS(NS,'ellipse');e.setAttribute('cx',x.toFixed(1));e.setAttribute('cy',y.toFixed(1));e.setAttribute('rx',4.6);e.setAttribute('ry',2.6);e.setAttribute('transform','rotate('+(ang*180/Math.PI).toFixed(1)+' '+x.toFixed(1)+' '+y.toFixed(1)+')');e.setAttribute('class','r4__fp');grp.appendChild(e);steps.push({el:e,at:s});}
sec._set=function(t){var len=stops[2]*t;steps.forEach(function(f){f.el.classList.toggle('is-walked',f.at<=len);});sec.querySelectorAll('.r4__st').forEach(function(st,i){st.classList.toggle('is-reached',len>=stops[i]-2);});};tick(sec);}
function tick(sec){if(!sec._set)return;if(reduce){sec._set(1);return;}var r=sec.querySelector('.r4__row').getBoundingClientRect(),vh=window.innerHeight;var t=(vh*0.85-r.top)/(r.height+vh*0.25);sec._set(Math.max(0,Math.min(1,t)));}
function all(){document.querySelectorAll('.r4').forEach(build);}
document.addEventListener('DOMContentLoaded',function(){all();if(document.fonts)document.fonts.ready.then(all);setTimeout(all,600);});
window.addEventListener('resize',all);
window.addEventListener('scroll',function(){document.querySelectorAll('.r4').forEach(tick);},{passive:true});
})();
