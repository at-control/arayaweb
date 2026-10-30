const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const file = require('node:path').join(__dirname, '../public/assets/measurement.js');
assert.ok(fs.existsSync(file), 'Consent and contact measurement runtime must exist');
const code = fs.readFileSync(file, 'utf8');
function fixture({saved, host='arayainternusa.co.id', target='production', broken=false, query='?utm_source=google&email=person@example.com'}={}) {
  const events={}, storage={}, scripts=[], cookies=[], queued=[], elements={}; let reloads=0;
  if(saved!==undefined) storage.araya_consent_v1=typeof saved==='string'?saved:JSON.stringify(saved);
  for(const id of ['consent-banner','consent-status']) elements[id]={hidden:true,dataset:{},textContent:'',focus(){}};
  const document={cookie:'_ga=one; _ga_X=two; unrelated=keep',
    currentScript:{dataset:{measurement:target}},head:{appendChild:s=>scripts.push(s)},
    getElementById:id=>elements[id],createElement:()=>({}),
    querySelectorAll:()=>[],addEventListener:(name,fn)=>events[name]=fn};
  Object.defineProperty(document,'cookie',{get:()=>cookies.length?'unrelated=keep':'_ga=one; _ga_X=two; unrelated=keep',set:v=>cookies.push(v)});
  const location={hostname:host,protocol:'https:',origin:'https://'+host,pathname:'/',search:query,href:'https://'+host+'/'+query,reload:()=>reloads++};
  const window={location,localStorage:{getItem:k=>{if(broken)throw Error('blocked');return storage[k]||null;},setItem:(k,v)=>{if(broken)throw Error('blocked');storage[k]=v;}},
    addEventListener:(name,fn)=>events[name]=fn,dataLayer:queued};
  vm.runInNewContext(code,{window,document,location,URL,Date,console,Set,JSON});
  function click(node){events.click({target:node});}
  function action(value){click({closest:s=>s==='[data-consent-action]'?{dataset:{consentAction:value}}:null});}
  function contact(href){const a={href,dataset:{contactLocation:'footer',serviceGroup:'unknown'},closest:s=>s==='a[href]'?a:null};click({closest:s=>s==='a[href]'?a:null});}
  return {window,document,events,storage,scripts,cookies,elements,action,contact,get reloads(){return reloads;}};
}
const now=Date.now(); const choice=analytics=>({version:1,analytics,at:now});
let f=fixture(); assert.equal(f.scripts.length,0,'Unknown consent must never load Google'); assert.equal(f.elements['consent-banner'].hidden,false);
f.contact('https://wa.me/6281326396262?text=private'); assert.equal(f.window.dataLayer.filter(x=>x.event==='contact_click').length,0,'No replay or events before consent');
f.action('reject'); assert.equal(f.scripts.length,0); assert.equal(JSON.parse(f.storage.araya_consent_v1).analytics,false);
f.action('accept'); assert.equal(f.scripts.length,1); assert.match(f.scripts[0].src,/GTM-NK3C3RVZ/);
const pageLocation=f.window.dataLayer.find(x=>x[0]==='set' && x[1]==='page_location')[2];
assert.equal(pageLocation,'https://arayainternusa.co.id/?utm_source=google','Keep campaign source but remove arbitrary personal URL fields');
const commands=f.window.dataLayer.filter(x=>x[0]==='consent');
assert.equal(commands[0][2].analytics_storage,'denied'); assert.equal(commands[1][2].analytics_storage,'granted'); assert.equal(commands[1][2].ad_storage,'denied');
f.action('accept'); assert.equal(f.scripts.length,1,'Acceptance must not install twice');
for(const href of ['https://wa.me/6281326396262?text=private','tel:+62317877990','mailto:cs@arayainternusa.com']) f.contact(href);
let hits=f.window.dataLayer.filter(x=>x.event==='contact_click'); assert.equal(hits.length,3); assert.deepEqual(hits.map(x=>x.contact_method),['whatsapp','phone','email']);
assert.ok(!JSON.stringify(hits).includes('private')); assert.ok(!JSON.stringify(hits).includes('cs@')); assert.ok(!JSON.stringify(hits).includes('7877990'));
for(const href of ['https://wa.me.evil.test/6281326396262','https://wa.me/123','tel:+621234','mailto:other@example.com','javascript:alert(1)']) f.contact(href);
assert.equal(f.window.dataLayer.filter(x=>x.event==='contact_click').length,3,'Only exact company contact targets count');
f.action('reject'); assert.equal(f.reloads,1); assert.equal(f.window['ga-disable-G-WMBDHTFPBJ'],true); assert.ok(f.cookies.some(x=>x.startsWith('_ga='))); assert.ok(!f.cookies.some(x=>x.startsWith('unrelated=')));
f=fixture({saved:choice(true)}); assert.equal(f.scripts.length,1,'Persisted acceptance loads once');
for(const saved of [choice(false),'broken',{...choice(true),at:now-181*86400000},{...choice(true),at:now+86400000}]) {f=fixture({saved});assert.equal(f.scripts.length,0);}
for(const opts of [{host:'localhost'},{host:'hakiimm8.github.io'},{host:'at-control.github.io'},{host:'arayainternusa.github.io'},{target:'preview'},{broken:true}]) {f=fixture({...opts,saved:choice(true)});assert.equal(f.scripts.length,0);}
f=fixture({saved:choice(true)}); f.events.storage({key:'araya_consent_v1',newValue:JSON.stringify(choice(false))}); assert.equal(f.reloads,1,'Withdrawal propagates between tabs');
f=fixture({saved:choice(true)}); f.events.storage({key:null,newValue:null}); assert.equal(f.reloads,1,'Clearing all storage must also withdraw consent');
f=fixture({broken:true}); f.action('accept'); f.contact('tel:+62317877990'); assert.equal(f.window.dataLayer.filter(x=>x.event==='contact_click').length,1,'Explicit consent applies within the page even if storage is unavailable');
f=fixture({saved:choice(true),query:'?utm_term=08123456789&utm_content=Jane-Smith&utm_campaign=Jane-Smith&utm_source=google&gclid=abcdef1234567890GHIJK'});
const attribution=f.window.dataLayer.find(x=>x[0]==='set' && x[1]==='page_location')[2];
assert.ok(!attribution.includes('08123456789')&&!attribution.includes('Jane-Smith'),'Free campaign text must not become a personal-data channel');
assert.ok(attribution.includes('utm_source=google')&&attribution.includes('gclid=abcdef1234567890GHIJK'),'Preserve controlled source and supported click identifiers');
console.log('PASS consent lifecycle, preview isolation, contact allowlists, no PII, persistence and withdrawal');
