const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require.resolve('../public/assets/site.js'), 'utf8');
const block = source.slice(source.indexOf('// Home on the current page'), source.indexOf('// Short text-only entrances'));
let handler, destination, scroll, prevented;
const link = {origin:'https://example.com',pathname:'/index.html',hash:'',search:'',closest:()=>true};
vm.runInNewContext(block, {
  document:{addEventListener:(name,fn)=>handler=fn},
  location:{origin:link.origin,pathname:'/',search:''},
  history:{pushState:(state,title,url)=>destination=url},
  window:{scrollTo:options=>scroll=options,matchMedia:()=>({matches:false})}
});
const event = {target:{closest:()=>link},button:0,preventDefault:()=>prevented=true};
handler(event);
assert.equal(prevented,true);
assert.equal(destination,'/index.html');
assert.equal(scroll.top,0);
assert.equal(scroll.behavior,'smooth');
prevented=false;
handler({...event,ctrlKey:true});
assert.equal(prevented,false,'Modified clicks keep normal browser behaviour');
link.pathname='/comap/';
handler(event);
assert.equal(prevented,false,'Cross-page links must still navigate');
console.log('PASS Home returns without reload; modified and cross-page links preserved.');
