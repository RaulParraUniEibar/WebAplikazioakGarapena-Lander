!function(){"use strict";var e={},t={};function n(r){var o=t[r];if(void 0!==o)return o.exports;var a=t[r]={id:r,loaded:!1,exports:{}},i=!0;try{e[r].call(a.exports,a,a.exports,n),i=!1}finally{i&&delete t[r]}return a.loaded=!0,a.exports}n.m=e,function(){var e=[];n.O=function(t,r,o,a){if(!r){var i=1/0;for(d=0;d<e.length;d++){r=e[d][0],o=e[d][1],a=e[d][2];for(var c=!0,u=0;u<r.length;u++)(!1&a||i>=a)&&Object.keys(n.O).every((function(e){return n.O[e](r[u])}))?r.splice(u--,1):(c=!1,a<i&&(i=a));if(c){e.splice(d--,1);var f=o();void 0!==f&&(t=f)}}return t}a=a||0;for(var d=e.length;d>0&&e[d-1][2]>a;d--)e[d]=e[d-1];e[d]=[r,o,a]}}(),n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,{a:t}),t},n.d=function(e,t){for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,r){return n.f[r](e,t),t}),[]))},n.u=function(e){return 614===e?"static/chunks/614-e781b035b9c03dbe.js":2089===e?"static/chunks/2089-762376daed5eb4a9.js":"static/chunks/"+e+"."+{237:"e7d24f199bc39288",418:"79e8a8d84e0accbd",2113:"42a9881d8095d616",2394:"780b7988c53bd02e",2741:"68011a8be8720fd9",2810:"7d7d8cbbb2bb8014",2914:"40d02cb1f48c261c",4031:"cee6c578394e1cba",5415:"d45a8ceb3e3f5b15",5778:"28b62ce00077d31e",9346:"ed0df1b4aca43714",9651:"8e00a265de6e8484"}[e]+".js"},n.miniCssF=function(e){return"static/css/"+{237:"abe634aa56875a28",346:"60ac1e2e2ed08632",418:"7d52ae2d4f21e495",1863:"d4fc2f867edc7f68",2394:"1073660096caa108",2810:"6369747597aa6940",2888:"efd5fbb46f45be73",2914:"481f630d91df3b51",3369:"34d7127047a0dfac",3579:"626d61c1c6f29113",4031:"4188ccb1d22d6ebb",4543:"60ac1e2e2ed08632",5305:"431fc86d6517158a",5405:"384d4449cd70d907",5778:"bc7b720fff8308b6",8248:"384d4449cd70d907",9346:"3f980f41a6932418",9502:"785ff93752d29c43"}[e]+".css"},n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}(),n.hmd=function(e){return(e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},function(){var e={},t="_N_E:";n.l=function(r,o,a,i){if(e[r])e[r].push(o);else{var c,u;if(void 0!==a)for(var f=document.getElementsByTagName("script"),d=0;d<f.length;d++){var s=f[d];if(s.getAttribute("src")==r||s.getAttribute("data-webpack")==t+a){c=s;break}}c||(u=!0,(c=document.createElement("script")).charset="utf-8",c.timeout=120,n.nc&&c.setAttribute("nonce",n.nc),c.setAttribute("data-webpack",t+a),c.src=n.tu(r)),e[r]=[o];var l=function(t,n){c.onerror=c.onload=null,clearTimeout(b);var o=e[r];if(delete e[r],c.parentNode&&c.parentNode.removeChild(c),o&&o.forEach((function(e){return e(n)})),t)return t(n)},b=setTimeout(l.bind(null,void 0,{type:"timeout",target:c}),12e4);c.onerror=l.bind(null,c.onerror),c.onload=l.bind(null,c.onload),u&&document.head.appendChild(c)}}}(),n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},function(){var e;n.tt=function(){return void 0===e&&(e={createScriptURL:function(e){return e}},"undefined"!==typeof trustedTypes&&trustedTypes.createPolicy&&(e=trustedTypes.createPolicy("nextjs#bundler",e))),e}}(),n.tu=function(e){return n.tt().createScriptURL(e)},n.p="https://public.slidesharecdn.com/_next/",function(){var e=function(e){return new Promise((function(t,r){var o=n.miniCssF(e),a=n.p+o;if(function(e,t){for(var n=document.getElementsByTagName("link"),r=0;r<n.length;r++){var o=(i=n[r]).getAttribute("data-href")||i.getAttribute("href");if("stylesheet"===i.rel&&(o===e||o===t))return i}var a=document.getElementsByTagName("style");for(r=0;r<a.length;r++){var i;if((o=(i=a[r]).getAttribute("data-href"))===e||o===t)return i}}(o,a))return t();!function(e,t,n,r){var o=document.createElement("link");o.rel="stylesheet",o.type="text/css",o.onerror=o.onload=function(a){if(o.onerror=o.onload=null,"load"===a.type)n();else{var i=a&&("load"===a.type?"missing":a.type),c=a&&a.target&&a.target.href||t,u=new Error("Loading CSS chunk "+e+" failed.\n("+c+")");u.code="CSS_CHUNK_LOAD_FAILED",u.type=i,u.request=c,o.parentNode.removeChild(o),r(u)}},o.href=t,document.head.appendChild(o)}(e,a,t,r)}))},t={2272:0};n.f.miniCss=function(n,r){t[n]?r.push(t[n]):0!==t[n]&&{237:1,418:1,2394:1,2810:1,2914:1,4031:1,5778:1,9346:1}[n]&&r.push(t[n]=e(n).then((function(){t[n]=0}),(function(e){throw delete t[n],e})))}}(),function(){var e={2272:0};n.f.j=function(t,r){var o=n.o(e,t)?e[t]:void 0;if(0!==o)if(o)r.push(o[2]);else if(2272!=t){var a=new Promise((function(n,r){o=e[t]=[n,r]}));r.push(o[2]=a);var i=n.p+n.u(t),c=new Error;n.l(i,(function(r){if(n.o(e,t)&&(0!==(o=e[t])&&(e[t]=void 0),o)){var a=r&&("load"===r.type?"missing":r.type),i=r&&r.target&&r.target.src;c.message="Loading chunk "+t+" failed.\n("+a+": "+i+")",c.name="ChunkLoadError",c.type=a,c.request=i,o[1](c)}}),"chunk-"+t,t)}else e[t]=0},n.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,a,i=r[0],c=r[1],u=r[2],f=0;if(i.some((function(t){return 0!==e[t]}))){for(o in c)n.o(c,o)&&(n.m[o]=c[o]);if(u)var d=u(n)}for(t&&t(r);f<i.length;f++)a=i[f],n.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return n.O(d)},r=self.webpackChunk_N_E=self.webpackChunk_N_E||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}(),n.nc=void 0}();