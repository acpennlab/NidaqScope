var _JUPYTERLAB;(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["dask-labextension"]=(()=>{"use strict";var e,r,t,n,a,o,i,l,u,s,f,d,p,c,h,v,b,m,g={317:(e,r,t)=>{var n={"./index":()=>Promise.all([t.e(177),t.e(42)]).then((()=>()=>t(42))),"./extension":()=>Promise.all([t.e(177),t.e(42)]).then((()=>()=>t(42)))},a=(e,r)=>(t.R=r,r=t.o(n,e)?n[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var n=t.S.default,a="default";if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[a]=e,t.I(a,r)}};t.d(r,{get:()=>a,init:()=>o})}},y={};function w(e){if(y[e])return y[e].exports;var r=y[e]={id:e,exports:{}};return g[e].call(r.exports,r,r.exports,w),r.exports}return w.m=g,w.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return w.d(r,{a:r}),r},w.d=(e,r)=>{for(var t in r)w.o(r,t)&&!w.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},w.f={},w.e=e=>Promise.all(Object.keys(w.f).reduce(((r,t)=>(w.f[t](e,r),r)),[])),w.u=e=>e+"."+{42:"6533f19f6fe458803231",177:"f5c107520ff0e5a32466",214:"85c64e924ab3ebb70903"}[e]+".js",w.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),w.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="dask-labextension:",w.l=(t,n,a)=>{if(e[t])e[t].push(n);else{var o,i;if(void 0!==a)for(var l=document.getElementsByTagName("script"),u=0;u<l.length;u++){var s=l[u];if(s.getAttribute("src")==t||s.getAttribute("data-webpack")==r+a){o=s;break}}o||(i=!0,(o=document.createElement("script")).charset="utf-8",o.timeout=120,w.nc&&o.setAttribute("nonce",w.nc),o.setAttribute("data-webpack",r+a),o.src=t),e[t]=[n];var f=(r,n)=>{o.onerror=o.onload=null,clearTimeout(d);var a=e[t];if(delete e[t],o.parentNode&&o.parentNode.removeChild(o),a&&a.forEach((e=>e(n))),r)return r(n)},d=setTimeout(f.bind(null,void 0,{type:"timeout",target:o}),12e4);o.onerror=f.bind(null,o.onerror),o.onload=f.bind(null,o.onload),i&&document.head.appendChild(o)}},w.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{w.S={};var e={},r={};w.I=(t,n)=>{n||(n=[]);var a=r[t];if(a||(a=r[t]={}),!(n.indexOf(a)>=0)){if(n.push(a),e[t])return e[t];w.o(w.S,t)||(w.S[t]={});var o=w.S[t],i="dask-labextension",l=(e,r,t)=>{var n=o[e]=o[e]||{},a=n[r];(!a||!a.loaded&&i>a.from)&&(n[r]={get:t,from:i})},u=[];switch(t){case"default":l("@lumino/polling","1.0.4",(()=>Promise.all([w.e(214),w.e(177)]).then((()=>()=>w(32))))),l("dask-labextension","5.2.0",(()=>Promise.all([w.e(177),w.e(42)]).then((()=>()=>w(42)))))}return e[t]=u.length?Promise.all(u).then((()=>e[t]=1)):1}}})(),(()=>{var e;w.g.importScripts&&(e=w.g.location+"");var r=w.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),w.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),n=t[1]?r(t[1]):[];return t[2]&&(n.length++,n.push.apply(n,r(t[2]))),t[3]&&(n.push([]),n.push.apply(n,r(t[3]))),n},n=(e,r)=>{e=t(e),r=t(r);for(var n=0;;){if(n>=e.length)return n<r.length&&"u"!=(typeof r[n])[0];var a=e[n],o=(typeof a)[0];if(n>=r.length)return"u"==o;var i=r[n],l=(typeof i)[0];if(o!=l)return"o"==o&&"n"==l||"s"==l||"u"==o;if("o"!=o&&"u"!=o&&a!=i)return a<i;n++}},a=e=>{if(1===e.length)return"*";if(0 in e){var r="",t=e[0];r+=0==t?">=":-1==t?"<":1==t?"^":2==t?"~":t>0?"=":"!=";for(var n=1,o=1;o<e.length;o++)n--,r+="u"==(typeof(l=e[o]))[0]?"-":(n>0?".":"")+(n=2,l);return r}var i=[];for(o=1;o<e.length;o++){var l=e[o];i.push(0===l?"not("+u()+")":1===l?"("+u()+" || "+u()+")":2===l?i.pop()+" "+i.pop():a(l))}return u();function u(){return i.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var n=e[0],a=n<0;a&&(n=-n-1);for(var i=0,l=1,u=!0;;l++,i++){var s,f,d=l<e.length?(typeof e[l])[0]:"";if(i>=r.length||"o"==(f=(typeof(s=r[i]))[0]))return!u||("u"==d?l>n&&!a:""==d!=a);if("u"==f){if(!u||"u"!=d)return!1}else if(u)if(d==f)if(l<=n){if(s!=e[l])return!1}else{if(a?s>e[l]:s<e[l])return!1;s!=e[l]&&(u=!1)}else if("s"!=d&&"n"!=d){if(a||l<=n)return!1;u=!1,l--}else{if(l<=n||f<d!=a)return!1;u=!1}else"s"!=d&&"n"!=d&&(u=!1,l--)}}var p=[],c=p.pop.bind(p);for(i=1;i<e.length;i++){var h=e[i];p.push(1==h?c()|c():2==h?c()&c():h?o(h,r):!c())}return!!c()},i=(e,r)=>{var t=w.S[e];if(!t||!w.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},l=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&n(e,r)?r:e),0)},u=(e,r,t)=>"Unsatisfied version "+r+" of shared singleton module "+e+" (required "+a(t)+")",s=(e,r,t,n)=>{var a=l(e,t);return o(n,a)||"undefined"!=typeof console&&console.warn&&console.warn(u(t,a,n)),d(e[t][a])},f=(e,r,t)=>{var a=e[r];return(r=Object.keys(a).reduce(((e,r)=>!o(t,r)||e&&!n(e,r)?e:r),0))&&a[r]},d=e=>(e.loaded=1,e.get()),c=(p=e=>function(r,t,n,a){var o=w.I(r);return o&&o.then?o.then(e.bind(e,r,w.S[r],t,n,a)):e(r,w.S[r],t,n,a)})(((e,r,t,n)=>(i(e,t),s(r,0,t,n)))),h=p(((e,r,t,n,a)=>{var o=r&&w.o(r,t)&&f(r,t,n);return o?d(o):a()})),v={},b={168:()=>c("default","@lumino/signaling",[1,1,4,3]),797:()=>c("default","@lumino/coreutils",[1,1,5,3]),39:()=>c("default","@jupyterlab/console",[1,3,2,5]),148:()=>h("default","@lumino/polling",[1,1,0,4],(()=>w.e(214).then((()=>()=>w(32))))),215:()=>c("default","@jupyterlab/apputils",[1,3,2,5]),233:()=>c("default","@jupyterlab/settingregistry",[1,3,2,5]),271:()=>c("default","react",[1,17,0,1]),396:()=>c("default","@jupyterlab/statedb",[1,3,2,5]),451:()=>c("default","@jupyterlab/coreutils",[1,5,2,5]),456:()=>c("default","react-dom",[1,17,0,1]),513:()=>c("default","@lumino/dragdrop",[1,1,7,1]),525:()=>c("default","@jupyterlab/mainmenu",[1,3,2,5]),539:()=>c("default","@jupyterlab/application",[1,3,2,5]),563:()=>c("default","@jupyterlab/ui-components",[1,3,2,5]),582:()=>c("default","@jupyterlab/notebook",[1,3,2,5]),608:()=>c("default","@lumino/domutils",[1,1,2,3]),706:()=>c("default","@lumino/widgets",[1,1,19,0]),850:()=>c("default","@lumino/algorithm",[1,1,3,3]),978:()=>c("default","@jupyterlab/services",[1,6,2,5])},m={42:[39,148,215,233,271,396,451,456,513,525,539,563,582,608,706,850,978],177:[168,797]},w.f.consumes=(e,r)=>{w.o(m,e)&&m[e].forEach((e=>{if(w.o(v,e))return r.push(v[e]);var t=r=>{v[e]=0,g[e]=t=>{delete y[e],t.exports=r()}},n=r=>{delete v[e],g[e]=t=>{throw delete y[e],r}};try{var a=b[e]();a.then?r.push(v[e]=a.then(t).catch(n)):t(a)}catch(e){n(e)}}))},(()=>{var e={754:0};w.f.j=(r,t)=>{var n=w.o(e,r)?e[r]:void 0;if(0!==n)if(n)t.push(n[2]);else if(177!=r){var a=new Promise(((t,a)=>{n=e[r]=[t,a]}));t.push(n[2]=a);var o=w.p+w.u(r),i=new Error;w.l(o,(t=>{if(w.o(e,r)&&(0!==(n=e[r])&&(e[r]=void 0),n)){var a=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+a+": "+o+")",i.name="ChunkLoadError",i.type=a,i.request=o,n[1](i)}}),"chunk-"+r)}else e[r]=0};var r=(r,t)=>{for(var n,a,[o,i,l]=t,u=0,s=[];u<o.length;u++)a=o[u],w.o(e,a)&&e[a]&&s.push(e[a][0]),e[a]=0;for(n in i)w.o(i,n)&&(w.m[n]=i[n]);for(l&&l(w),r&&r(t);s.length;)s.shift()()},t=self.webpackChunkdask_labextension=self.webpackChunkdask_labextension||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),w(317)})();