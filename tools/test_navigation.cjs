const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require.resolve('../public/assets/site.js'), 'utf8');
const start = source.includes('// Shared header and main navigation.')
  ? source.indexOf('// Shared header and main navigation.')
  : source.indexOf('// Keep section navigation available');
const component = source.slice(start, source.indexOf('// Short text-only entrances'));

function fixture(path = '/arayaweb/index.html') {
  const events = {}, frames = [], styles = new Map();
  let edge = 140;
  const targets = Object.fromEntries(['about','services','clients','brands','contact'].map((id,i)=>[id,{top:500+i*500,getBoundingClientRect(){return {top:this.top,bottom:this.top+500};}}]));
  const link = (pathname, hash='', text='')=>({pathname,hash,textContent:text,attrs:new Map(),dataset:{},
    setAttribute(k,v){this.attrs.set(k,v);},removeAttribute(k){this.attrs.delete(k);},getAttribute(k){return this.attrs.get(k)??null;}});
  const links = [link('/arayaweb/index.html','','Home'),...['about','services','clients'].map(id=>link('/arayaweb/index.html','#'+id,id)),link('/arayaweb/noris/','','Noris'),link('/arayaweb/comap/','','ComAp'),link(path,'#contact','Contact')];
  if(path==='/arayaweb/future/') {links[4].pathname=path;links[4].textContent='Future Brand';}
  links.forEach((item,i)=>item.closest=selector=>selector==='.brand-menu' && [4,5].includes(i)?{}:null);
  const summary=link('', '', 'Brand Partners');
  const header={getBoundingClientRect:()=>({bottom:edge}),querySelector:()=>null};
  const nav={querySelectorAll:()=>links};
  const document={documentElement:{scrollHeight:5000,style:{setProperty:(k,v)=>styles.set(k,v)}},
    querySelector:s=>s==='.site-header'?header:s==='#main-navigation'?nav:s==='.brand-menu summary'?summary:null,
    querySelectorAll:s=>s==='.main-nav a'?links:[],getElementById:id=>targets[id]??null,
    addEventListener:(name,fn)=>events[name]=fn};
  const window={location:{pathname:path,hash:''},innerHeight:844,scrollY:0,
    addEventListener:(name,fn)=>events[name]=fn};
  const context={document,window,location:window.location,requestAnimationFrame:fn=>{frames.push(fn);return frames.length;},
    ResizeObserver:class{constructor(fn){events.observer=fn;}observe(){}}};
  vm.runInNewContext(component,context);
  const flush=()=>{while(frames.length)frames.shift()();};
  return {links,summary,styles,targets,events,flush,document,window,setEdge:v=>edge=v};
}

let f=fixture();
assert.equal(f.styles.get('--header-edge'),'140px','Header measurement must work without page-index');
assert.equal(f.links[0].getAttribute('aria-current'),'page');
for(const [id,index] of [['about',1],['services',2],['clients',3],['contact',6]]) {
  Object.values(f.targets).forEach(t=>t.top=1000);
  f.targets[id].top=150;
  f.events.scroll();f.flush();
  assert.equal(f.links[index].getAttribute('aria-current'),'location',id);
  assert.equal(f.links[0].getAttribute('aria-current'),null,'Home must not stay highlighted');
}
Object.values(f.targets).forEach(t=>t.top=1000);f.targets.brands.top=150;
f.events.scroll();f.flush();
assert.equal(f.summary.getAttribute('aria-current'),'location');
f.setEdge(72);f.events['navigation-layout']();
assert.equal(f.styles.get('--header-edge'),'72px','Menu collapse updates anchor offset synchronously');
f.setEdge(86);f.events.observer();f.flush();
assert.equal(f.styles.get('--header-edge'),'86px','Font/header resize is measured');
Object.values(f.targets).forEach(t=>t.top=1000);f.targets.about.top=100;
f.events.popstate();f.flush();
assert.equal(f.links[1].getAttribute('aria-current'),'location','Back/Forward updates active section');
f=fixture('/arayaweb/noris/');
assert.equal(f.links[4].getAttribute('aria-current'),'page');
assert.equal(f.summary.dataset.current,'page','Collapsed dropdown shows current brand');
f.targets.contact.top=150;f.events.hashchange();f.flush();
assert.equal(f.links[6].getAttribute('aria-current'),'location');
assert.equal(f.summary.dataset.current,'page','Brand page identity remains visible in Contact');
f=fixture('/arayaweb/');
assert.equal(f.links[0].getAttribute('aria-current'),'page','Directory and index.html URLs share identity');
f=fixture();f.setEdge(90);f.targets.services.top=255;
f.events.scroll();f.flush();
assert.equal(f.links[2].getAttribute('aria-current'),'location','Visible section enters the upper reading area');
f=fixture();f.document.documentElement.scrollHeight=1000;f.window.scrollY=156;f.targets.contact.top=400;
f.events.scroll();f.flush();
assert.equal(f.links[6].getAttribute('aria-current'),'location','Contact is current at the end of a tall viewport');
f=fixture('/arayaweb/future/');
assert.equal(f.summary.dataset.current,'page','Future brands inherit the parent indication');
console.log('PASS: independent header offset, section/brand selection, menu resize and history navigation.');
